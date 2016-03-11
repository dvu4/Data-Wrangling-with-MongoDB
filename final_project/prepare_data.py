#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:

{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}

You have to complete the function 'shape_element'.
We have provided a function that will parse the map file, and call the function with the element
as an argument. You should return a dictionary, containing the shaped data for that element.
We have also provided a way to save the data in a file, so that you could use
mongoimport later on to import the shaped data into MongoDB.

Note that in this exercise we do not use the 'update street name' procedures
you worked on in the previous exercise. If you are using this code in your final
project, you are strongly encouraged to use the code from previous exercise to
update the street names before you save them to JSON.

In particular the following things should be done:
- you should process only 2 types of top level tags: "node" and "way"
- all attributes of "node" and "way" should be turned into regular key/value pairs, except:
    - attributes in the CREATED array should be added under a key "created"
    - attributes for latitude and longitude should be added to a "pos" array,
      for use in geospacial indexing. Make sure the values inside "pos" array are floats
      and not strings.
- if second level tag "k" value contains problematic characters, it should be ignored
- if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
- if second level tag "k" value does not start with "addr:", but contains ":", you can process it
  same as any other tag.
- if there is a second ":" that separates the type/direction of a street,
  the tag should be ignored, for example:

<tag k="addr:housenumber" v="5158"/>
<tag k="addr:street" v="North Lincoln Avenue"/>
<tag k="addr:street:name" v="Lincoln"/>
<tag k="addr:street:prefix" v="North"/>
<tag k="addr:street:type" v="Avenue"/>
<tag k="amenity" v="pharmacy"/>

  should be turned into:

{...
"address": {
    "housenumber": 5158,
    "street": "North Lincoln Avenue"
}
"amenity": "pharmacy",
...
}

- for "way" specifically:

  <nd ref="305896090"/>
  <nd ref="1719825889"/>

should be turned into
"node_refs": ["305896090", "1719825889"]
"""

# indicate file to be read
osmfile = "boston_massachusetts.osm"

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$') #
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
     '''
     This function will parse the map file and return a dictionary, 
     containing the shaped data for that element.
     Args:
        element(string): element in the map.
    '''
    node = {}
    if element.tag == "node" or element.tag == "way" :
        # YOUR CODE HERE
        node["type"] = element.tag

        #for key in element.attrib.keys()
        for key in element.attrib:
            #print key

            if key in CREATED:
                if "created" not in node:
                    node["created"] = {}
                node["created"][key] = element.attrib[key]

            elif key in ["lat","lon"]:
                if "pos" not in node:
                    node["pos"] = [None, None]
                if key == "lat":
                    node["pos"][0] = float(element.attrib[key])
                elif key == "lon":
                    node["pos"][1] = float(element.attrib[key])
            else:
                node[key] = element.attrib[key]

            for tag in element.iter("tag"):
                tag_key = tag.attrib["k"]   # key
                tag_value = tag.attrib["v"] # value
                if not problemchars.match(tag_key):
                    if tag_key.startswith("addr:"):# Single colon beginning with addr
                        if "address" not in node:
                            node["address"] = {}
                        sub_addr = tag_key[len("addr:"):]
                        if not lower_colon.match(sub_addr): # Tags with no colon
                            node["address"][sub_addr] = tag_value
                    elif lower_colon.match(tag_key): # Single colon not beginnning with "addr:"
                        node[tag_key] = tag_value
                    else:
                        node[tag_key] = tag_value # Tags with no colon, not beginnning with "addr:"

        for nd in element.iter("nd"):
            if "node_refs" not in node:
                node["node_refs"] = []
            node["node_refs"].append(nd.attrib["ref"])

        print node
        return node
    else:
        return None

'''
def shape_element(element):
    node = {}
    # you should process only 2 types of top level tags: "node" and "way"
    if element.tag == "node" or element.tag == "way" :
        for key in element.attrib.keys():
            val = element.attrib[key]
            node["type"] = element.tag
            if key in CREATED:
                if not "created" in node.keys():
                    node["created"] = {}
                node["created"][key] = val
            elif key == "lat" or key == "lon":
                if not "pos" in node.keys():
                    node["pos"] = [0.0, 0.0]
                old_pos = node["pos"]
                if key == "lat":
                    new_pos = [float(val), old_pos[1]]
                else:
                    new_pos = [old_pos[0], float(val)]
                node["pos"] = new_pos
            else:
                node[key] = val
            for tag in element.iter("tag"):
                tag_key = tag.attrib['k']
                tag_val = tag.attrib['v']
                if problemchars.match(tag_key):
                    continue
                elif tag_key.startswith("addr:"):
                    if not "address" in node.keys():
                        node["address"] = {}
                    addr_key = tag.attrib['k'][len("addr:") : ]
                    if lower_colon.match(addr_key):
                        continue
                    else:
                        node["address"][addr_key] = tag_val
                elif lower_colon.match(tag_key):
                    node[tag_key] = tag_val
                else:
                    node[tag_key] = tag_val
        for tag in element.iter("nd"):
            if not "node_refs" in node.keys():
                node["node_refs"] = []
            node_refs = node["node_refs"]
            node_refs.append(tag.attrib["ref"])
            node["node_refs"] = node_refs
        print node
        return node
    else:
        return None
'''
'''
def shape_element(element):
    node = {}

    if element.tag == "node" or element.tag == "way" :

      node['type'] = element.tag

      # Parse attributes
      for a in element.attrib:
        if a in CREATED:
          if 'created' not in node:
            node['created'] = {}
          node['created'][a] = element.attrib[a]

        elif a in ['lat', 'lon']:
          if 'pos' not in node:
            node['pos'] = [None, None]

          if a == 'lat':
            node['pos'][0] = float(element.attrib[a])
          else:
            node['pos'][1] = float(element.attrib[a])

        else:
          node[a] = element.attrib[a]

      # Iterate tag children
      for tag in element.iter("tag"):
        if not problemchars.search(tag.attrib['k']):
          # Tags with single colon
          if lower_colon.search(tag.attrib['k']):

            # Single colon beginning with addr
            if tag.attrib['k'].find('addr') == 0:
              if 'address' not in node:
                node['address'] = {}

              sub_attr = tag.attrib['k'].split(':', 1)
              node['address'][sub_attr[1]] = tag.attrib['v']

            # All other single colons processed normally
            else:
              node[tag.attrib['k']] = tag.attrib['v']

          # Tags with no colon
          elif tag.attrib['k'].find(':') == -1:
            node[tag.attrib['k']] = tag.attrib['v']

      # Iterate nd children
      for nd in element.iter("nd"):
        if 'node_refs' not in node:
          node['node_refs'] = []
        node['node_refs'].append(nd.attrib['ref'])

      print node
      return node
    else:
      return None
'''


def process_map(osmfile, pretty = False):
    '''
    This fucntion will parse the XML, shape the elements, and write to a json file
    '''
    # You do not need to change this file
    file_out = "{0}.json".format(osmfile)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data


# test the audit
def test():
    # NOTE: if you are running this code on your computer, with a larger dataset,
    # call the process_map procedure with pretty=False. The pretty=True option adds
    # additional spaces to the output, making it significantly larger.
    data = process_map(osmfile, True)
    pprint.pprint(data)


if __name__ == "__main__":
    test()
    
### Check the size of XML and JSON files   
import os
print "The downloaded XML file is {} MB".format(os.path.getsize(filename)/1.0e6) # convert from bytes to megabytes
print "The json file is {} MB".format(os.path.getsize(filename + ".json")/1.0e6) # convert from bytes to megabytes