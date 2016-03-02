
# coding: utf-8

# # Wrangling  OpenStreetMap Data  with MongoDB
# ###  by Duc Vu in fulfillment of Udacity’s Data Analyst Nanodegree, Project 3

# OpenStreetMap is an open project that lets eveyone use and create a free editable map of the world.

# ## 1. Chosen Map Area

# In this project, I choose to analyze data from Boston, Massachusetts want to show you to fix one type of error, that is the address of the street. And not only that, I also will show you how to put the data that has been audited into MongoDB instance. We also use MongoDB's Agregation Framework to get overview and analysis of the data

# In[23]:

from IPython.display import HTML
HTML('<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://www.openstreetmap.org/export/embed.html?bbox=-71.442,42.1858,-70.6984,42.4918&amp;layer=mapnik"></iframe><br/>')


# The dataset is here https://s3.amazonaws.com/metro-extracts.mapzen.com/boston_massachusetts.osm.bz2

# In[24]:

filename = 'boston_massachusetts.osm'


# I used the Overpass API to download the OpenStreetMap XML for the corresponding bounding box:

# ## 2. Auditing the Data

#  In this project, I will parse through the downloaded OSM XML file with ElementTree and find the number of each type of element since the XML file are too large to work with in memory.

# In[27]:

import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    '''
    this function will return a dictionary with the tag name as the key 
    and number of times this tag can be encountered in the map as value.
    '''
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags:
            tags[elem.tag] +=1
        else:
            tags[elem.tag]= 1
                
    return tags
tags = count_tags(filename)
pprint.pprint(tags)


# Before processing the data and add it into MongoDB, I should check the "k" value for each 'tag' and see if they can be valid keys in MongoDB, as well as see if there are any other potential problems.
# 
# I have built 3 regular expressions to check for certain patterns in the tags to change the data model
# and expand the "addr:street" type of keys to a dictionary like this:
# 
# 
# Here are three regular expressions: lower, lower_colon, and problemchars.
# 
# - lower: matches strings containing lower case characters
# - lower_colon: matches strings containing lower case characters and a single colon within the string
# - problemchars: matches characters that cannot be used within keys in MongoDB
#  
#  
# - example: {"address": {"street": "Some value"}}
# 
# So, we have to see if we have such tags, and if we have any tags with problematic characters.
# Please complete the function 'key_type'.

# In[29]:

import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    '''
     this function counts number of times the unusual tag element can be encountered in the map.
    Args:
        element(string): tag element in the map.
        keys(int): number of that encountered tag in the map
    '''
    if element.tag == "tag":

        if lower.search(element.attrib['k']):
            keys["lower"] += 1
        elif lower_colon.search(element.attrib['k']):
            keys["lower_colon"] += 1
        elif problemchars.search(element.attrib['k']):
            keys["problemchars"] +=1
        else:
            keys["other"] +=1
        

    return keys


def process_map(filename):
    '''
     this function will return a dictionary with the unexpexted tag element as the key 
     and number of times this string can be encountered in the map as value.
    Args:
        filename(osm): openstreetmap file.
    '''
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

'''
#Below unit testing runs process_map with file example.osm
def test():
    keys = process_map('example.osm')
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}


if __name__ == "__main__":
    test()

'''

keys = process_map(filename)
pprint.pprint(keys)


# Now I will redefine process_map to build a set of unique userid's found within the XML. I will then output the length of this set, representing the number of unique users making edits in the chosen map area.

# In[30]:

def process_map(filename):
    '''
    This function will return a set of unique user IDs ("uid") 
    making edits in the chosen map area (i.e Boston area).
    Args:
        filename(osm): openstreetmap file.
    '''
    users = set()
    for _, element in ET.iterparse(filename):
        #print element.attrib
        
        try:
            users.add(element.attrib['uid'])
        except KeyError:
            continue
        '''
        if "uid" in element.attrib:
            users.add(element.attrib['uid'])
        '''
    return users

'''
#Below unit testing runs process_map with file example.osm
def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6

if __name__ == "__main__":
    test()
'''

    
    
users = process_map(filename)
#pprint.pprint(users)
print len(users)


# ## 3. Problems Encountered in the Map

# The majority of this project will be devoted to auditing and cleaning street names in the OSM XML file by changing the variable 'mapping' to reflect the changes needed to fix the unexpected or abbreviated street types to the appropriate ones in the expected list. I will find these abbreviations and replace them with their full text form. 

# In[31]:

from collections import defaultdict

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]


# In[32]:

def audit_street_type(street_types, street_name, rex):
    '''
     This function will take in the dictionary of street types, a string of street name to audit, 
     a regex to match against that string, and the list of expected street types.
     Args:
        street_types(dictionary): dictionary of street types.
        street_name(string):  a string of street name to audit.
        rex(regex): a compiled regular expression to match against the street_name.
    '''
    #m = street_type_re.search(street_name)
    m = rex.search(street_name)
    #print m
    #print m.group()
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


# Let's define a function that not only audits tag elements where k="addr:street", but whichever tag elements match the is_street_name function. The audit function also takes in a regex and the list of expected matches

# In[33]:

def audit(osmfile,rex):
    '''
     This function changes the variable 'mapping' to reflect the changes needed to fix
    the unexpected street types to the appropriate ones in the expected list.
     Args:
        filename(osm): openstreetmap file.
        rex(regex): a compiled regular expression to match against the street_name.
    '''
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'],rex)

    return street_types


# The function is_street_name determines if an element contains an attribute k="addr:street". I will use is_street_name as the tag filter when I call the audit function to audit street names.

# In[34]:

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


# Now print the output of audit

# In[35]:

st_types = audit(filename, rex = street_type_re)
pprint.pprint(dict(st_types))


# From the results of the audit, I will create a dictionary to map abbreviations to their full, clean representations.

# In[13]:

# UPDATE THIS VARIABLE
mapping = { "ave" : "Avenue",
            "Ave" : "Avenue",
            "Ave.": "Avenue",
            "Ct" : "Court",
            "HIghway": "Highway",
            "Hwy": "Highway",
            "LEVEL": "Level",
            "Pkwy": "Parkway",
            "Pl": "Place",
            "rd." : "Road",
            "Rd" : "Road",
            "Rd." : "Road",
            "Sq." : "Square", 
            "st": "Street",
            "St": "Street",
            "St.": "Street",
            "St,": "Street", 
            "ST": "Street",
            "Street." : "Street",               
            }


# The first result of audit gives me a list of some abbreviated street types (as well as unexpected clean street types, cardinal directions, and highway numbers). So I need to build an update_name function to replace these abbreviated street types.

# In[14]:

def update_name(name, mapping,rex):
    '''
     This function takes a string with street name as an argument 
     and replace these abbreviated street types with the fixed name.
     Args:
        name(string): street name to update.
        mapping(dictionary): a mapping dictionary.
        rex(regex): a compiled regular expression to match against the street_name.
    '''
    write the update_name function, to actually fix the street name.
    
    #m = street_type_re.search(name)
    m = rex.search(name)
    if m:
        street_type = m.group()
        new_street_type = mapping[street_type]
        name = re.sub(rex, new_street_type, name) # re.sub(old_pattern, new_pattern, file)
        #name = street_type_re.sub(new_street_type, name)
    return name


# Let's see how this update_name works.

# In[15]:

for st_type, ways in st_types.iteritems():
    if st_type in mapping:
        for name in ways:
            better_name = update_name(name, mapping, rex = street_type_re)
            print name, "=>", better_name


# It seems that all the abbreviated street types updated as expected.
# 
# But I can see there is still an issue: cardinal directions (North, South, East, and West) appear to be universally abbreviated.  Therefore , I will traverse the cardinal_directions dictionary and apply the updates for both street type and cardinal direction

# In[16]:

cardinal_dir_re = re.compile(r'^[NSEW]\b\.?', re.IGNORECASE)


# Here is the result of audit the cardinal directions with this new regex 'cardinal_dir_re'

# In[17]:

dir_st_types = audit(filename, rex = cardinal_dir_re)
pprint.pprint(dict(dir_st_types))


# I will create a dictionary to map abbreviations (N, S, E and W) to their full representations of cardinal directions.

# In[18]:

cardinal_directions_mapping =     {
        "E" : "East",
        "N" : "North",
        "S" : "South",
        "W" : "West"
    }


# Look like all expected cardinal directions have been replaced.

# In[19]:

for st_type, ways in dir_st_types.iteritems():
    if st_type in cardinal_directions_mapping:
        for name in ways:
            better_name = update_name(name, cardinal_directions_mapping, rex = cardinal_dir_re)
            print name, "=>", better_name


# Then I will count the total number of nodes and ways that contain a tag child with k="addr:street"

# In[203]:

osm_file = open(filename, "r")
address_count = 0

for event, elem in ET.iterparse(osm_file, events=("start",)):
    if elem.tag == "node" or elem.tag == "way":
        for tag in elem.iter("tag"): 
            if is_street_name(tag):
                address_count += 1

address_count


# ## 4. Preparing for MongoDB

# Before importing the XML data into MongoDB, I have to transform the shape of data into json documents structured (a list of dictionaries) like this
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
# Here are the rules:
# - process only 2 types of top level tags: "node" and "way"
# - all attributes of "node" and "way" should be turned into regular key/value pairs, except:
#     - attributes in the CREATED array should be added under a key "created"
#     - attributes for latitude and longitude should be added to a "pos" array,
#       for use in geospacial indexing. Make sure the values inside "pos" array are floats
#       and not strings.
# - if second level tag "k" value contains problematic characters, it should be ignored
# - if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"
# - if second level tag "k" value does not start with "addr:", but contains ":", you can process it
#   same as any other tag.
# - if there is a second ":" that separates the type/direction of a street,
#   the tag should be ignored, for example:
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
  <nd ref="1719825889"/>should be turned into# "node_refs": ["305896090", "1719825889"]
# In[5]:

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def shape_element(element):
    '''
     This function will parse the map file and return a dictionary, 
     containing the shaped data for that element.
     Args:
        element(string): element in the map.
    '''
    node = {}
    # create an address dictionary
    address = {}
    
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
                            address[sub_addr] = tag_value 
                            node["address"] = address
                            #node["address"][sub_addr] = tag_value
                    elif lower_colon.match(tag_key): # Single colon not beginnning with "addr:"
                        node[tag_key] = tag_value
                    else:
                        node[tag_key] = tag_value # Tags with no colon, not beginnning with "addr:"

        for nd in element.iter("nd"):
            if "node_refs" not in node:
                node["node_refs"] = []
            node["node_refs"].append(nd.attrib["ref"])

        return node
    else:
        return None


# It's time to parse the XML, shape the elements, and write to a json file

# In[ ]:

import codecs
import json

def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
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

process_map(filename)


# ## 5. Data Overview

# Check the size of XML and JSON files

# In[194]:

import os
print "The downloaded XML file is {} MB".format(os.path.getsize(filename)/1.0e6) # convert from bytes to megabytes


# In[195]:

print "The json file is {} MB".format(os.path.getsize(filename + ".json")/1.0e6) # convert from bytes to megabytes


# #### Execute mongod to run MongoDB
# Use the subprocess module to run shell commands.

# In[196]:

import signal
import subprocess

# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.
pro = subprocess.Popen("mongod", preexec_fn = os.setsid) 


# http://sharats.me/the-ever-useful-and-neat-subprocess-module.html

# #### Connect database with pymongo

# In[26]:

from pymongo import MongoClient

db_name = "osm"

client = MongoClient('localhost:27017')
db = client[db_name]


# When we have to import a large amounts of data, mongoimport is recommended.
# 
# First build a mongoimport command, then use subprocess.call to execute

# In[27]:

# Build mongoimport command
collection = filename[:filename.find(".")]
print collection
working_directory = "/Users/ducvu/Documents/ud032-master/final_project/"

json_file = filename + ".json"
print json_file
mongoimport_cmd = "mongoimport --db " + db_name +                   " --collection " + collection +                   " --file " + working_directory + json_file
print mongoimport_cmd 

# Before importing, drop collection if it exists
if collection in db.collection_names():
    print "dropping collection"
    db[collection].drop()

# Execute the command
print "Executing: " + mongoimport_cmd
subprocess.call(mongoimport_cmd.split())


# ### Get the collection from the database

# In[84]:

boston_db = db[collection]


# ### Number of Documents

# In[85]:

boston_db.find().count()


# ### Number of Unique Users

# In[86]:

len(boston_db.distinct('created.user'))


# ### Number of Nodes and Ways

# In[190]:

node_way = boston_db.aggregate([
        {"$group" : {"_id" : "$type", "count" : {"$sum" : 1}}}])

pprint.pprint(list(node_way))


# ### Number of Nodes

# In[90]:

boston_db.find({"type":"node"}).count()


# ### Number of Ways

# In[91]:

boston_db.find({"type":"way"}).count()


# ### Top Contributing User

# In[191]:

top_user = boston_db.aggregate([
    {"$match":{"type":"node"}},
    {"$group":{"_id":"$created.user","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":1}
])

#print(list(top_user))
pprint.pprint(list(top_user))


# ### Number of users having only 1 post

# In[168]:

type_buildings = boston_db.aggregate([
    {"$group":{"_id":"$created.user","count":{"$sum":1}}},
    {"$group":{"_id":{"postcount":"$count"},"num_users":{"$sum":1}}},
    {"$project":{"_id":0,"postcount":"$_id.postcount","num_users":1}},
    {"$sort":{"postcount":1}},
    {"$limit":1}
])

pprint.pprint(list(type_buildings))


# ### Number of Documents Containing a Street Address

# In[197]:

boston_db.find({"address.street" : {"$exists" : 1}}).count()


# ### Zip codes

# In[179]:

zipcodes = boston_db.aggregate([
        {"$match" : {"address.postcode" : {"$exists" : 1}}}, \
        {"$group" : {"_id" : "$address.postcode", "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}}])

#for document in zipcodes:
#    print(document)
    
pprint.pprint(list(zipcodes))


# ### Top 5 Most Common Cities

# In[201]:

cities = boston_db.aggregate([{"$match" : {"address.city" : {"$exists" : 1}}},                            {"$group" : {"_id" : "$address.city", "count" : {"$sum" : 1}}},                            {"$sort" : {"count" : -1}},                            {"$limit" : 5}])

#for city in cities :
#    print city
    
pprint.pprint(list(cities))


# ### Top 10 Amenities

# In[192]:

amenities = boston_db.aggregate([
        {"$match" : {"amenity" : {"$exists" : 1}}}, \
        {"$group" : {"_id" : "$amenity", "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}}, \
        {"$limit" : 10}])

#for document in amenities:
#    print document

pprint.pprint(list(amenities))


# In[198]:

amenities = boston_db.aggregate([
    {"$match":{"amenity":{"$exists":1},"type":"node"}},
    {"$group":{"_id":"$amenity","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":10}
])

pprint.pprint(list(amenities))


# ### Most common building types

# In[173]:

type_buildings = boston_db.aggregate([
    {'$match': {'building': {'$exists': 1}}}, 
    {'$group': { '_id': '$building','count': {'$sum': 1}}},
    {'$sort': {'count': -1}}, {'$limit': 20}
])

pprint.pprint(list(type_buildings))


# ### Top Religions with Denominations

# In[139]:

religions = boston_db.aggregate([
        {"$match" : {"amenity" : "place_of_worship"}}, \
        {"$group" : {"_id" : {"religion" : "$religion", "denomination" : "$denomination"}, "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}}])

#for document in religions:
#    print document

pprint.pprint(list(religions))


# ### Top 10 Leisures

# In[154]:

leisures = boston_db.aggregate([{"$match" : {"leisure" : {"$exists" : 1}}},                            {"$group" : {"_id" : "$leisure", "count" : {"$sum" : 1}}},                            {"$sort" : {"count" : -1}},                            {"$limit" : 10}])

#for document in leisures:
#    print document

pprint.pprint(list(leisures))


# ### Top 15 Universities

# In[202]:

universities = boston_db.aggregate([
        {"$match" : {"amenity" : "university"}}, \
        {"$group" : {"_id" : {"name" : "$name"}, "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}},
        {"$limit":15}
    ])

pprint.pprint(list(universities))


# ### Top 10 Schools

# In[147]:

schools = boston_db.aggregate([
        {"$match" : {"amenity" : "school"}}, \
        {"$group" : {"_id" : {"name" : "$name"}, "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}},
        {"$limit":10}
    ])

pprint.pprint(list(schools))


# ### Top Prisons 

# In[153]:

prisons = boston_db.aggregate([
        {"$match" : {"amenity" : "prison"}}, \
        {"$group" : {"_id" : {"name" : "$name"}, "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}}])

pprint.pprint(list(prisons))


# ### Top 10 Hospitals

# In[189]:

hospitals = boston_db.aggregate([
        {"$match" : {"amenity" : "hospital"}}, \
        {"$group" : {"_id" : {"name" : "$name"}, "count" : {"$sum" : 1}}}, \
        {"$sort" : {"count" : -1}},
        {"$limit":10}
    ])


pprint.pprint(list(hospitals))


# ### Most popular cuisines in fast foods

# In[169]:

fast_food = boston_db.aggregate([
    {"$match":{"cuisine":{"$exists":1},"amenity":"fast_food"}},
    {"$group":{"_id":"$cuisine","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":10}
])

pprint.pprint(list(fast_food))


# ### Most popular gas station brands

# In[170]:

gas_station_brands = boston_db.aggregate([
    {"$match":{"brand":{"$exists":1},"amenity":"fuel"}},
    {"$group":{"_id":"$brand","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":10}
])

pprint.pprint(list(gas_station_brands))


# ### Most popular banks

# In[171]:

banks = boston_db.aggregate([
    {"$match":{"name":{"$exists":1},"amenity":"bank"}},
    {"$group":{"_id":"$name","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":10}
])

pprint.pprint(list(banks))


# ### Most popular restaurants

# In[172]:

restaurants = boston_db.aggregate([
    {"$match":{"name":{"$exists":1},"amenity":"restaurant"}},
    {"$group":{"_id":"$name","count":{"$sum":1}}},
    {"$sort":{"count":-1}},
    {"$limit":10}
])

pprint.pprint(list(restaurants))


# ## 6. Additional Ideas

# Analyzing the data of Boston I found out that not all nodes or ways include this information since its geographical position is represented within regions of a city. What could be done in this case, is check if each node or way belongs to a city based on the latitude and longitude and ensure that the property "address.city" is properly informed. By doing so, we could get statistics related to cities in a much more reliable way. In fact, I think this is the biggest benefit to anticipate problems and implement improvements to the data you want to analyze. Real world data are very susceptible to being incomplete, noisy and inconsistent which means that if you have low-quality of data the results of their analysis will also be of poor quality.
# 
#   I think that extending this open source project to include data such as user reviews of establishments, subjective areas of what bound a good and bad neighborhood, housing price data, school reviews, walkability/bikeability, quality of mass transit, and on would form a solid foundation of robust recommender systems. These recommender systems could aid users in anything from finding a new home or apartment to helping a user decide where to spend a weekend afternoon.
#   
# Another alternative to help in the absence of information in the region would be the use of gamification or crowdsource information to make more people help in the map contribution. Something like the mobile apps similar to Waze and Minutely have already done to make the users responsible for improving the app and  social network around the app.
# 

# ## 7.  Conclusion         

# This review of the data is cursory, but it seems that the Boston area is incomplete, though I believe it has been well cleaned and represented after this project.

# ## 8.  References

# <a href="http://wiki.openstreetmap.org/wiki/Main_Page">OpenStreetMap Wiki Page</a>
# 
# <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">OpenStreetMap Wiki Page - OSM XML
# </a>
# 
# <a href="http://wiki.openstreetmap.org/wiki/Map_Features">OpenStreetMap Map Features</a>
# 
# <a href="https://docs.python.org/2/library/re.html#search-vs-match">Python Regular Expressions</a>
# 
# <a href="https://docs.mongodb.org/v2.4/reference/operator/">MongoDB Operators</a>
# 
# <a href="http://www.choskim.me/how-to-install-mongodb-on-apples-mac-os-x/">Install MongoDB on Apple's Mac OS X</a>
# 
# <a href="https://books.google.com/books?id=_VkrAQAAQBAJ&pg=PA241&lpg=PA241&dq=execute+mongodb+command+in+ipython&source=bl&ots=JqnwlwRvkN&sig=h-TrwspKAmHt1g1ELItnWkDmRHs&hl=en&sa=X&ved=0ahUKEwiJnaiikIrLAhUM8CYKHZ8mBrcQ6AEILzAD#v=onepage&q=execute%20mongodb%20command%20in%20ipython&f=false/">Install MongoDB</a>
# 
# <a href="http://michaelcrump.net/how-to-run-html-files-in-your-browser-from-github/"> Run HTML files in your Browser from GitHub </a>
# 
# 
