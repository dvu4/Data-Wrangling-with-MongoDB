#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it, clean it, 
come up with a data model, insert it into a MongoDB and then run some queries against your database.
The set contains data about Arachnid class.
Your task in this exercise is to parse the file, process only the fields that are listed in the
FIELDS dictionary as keys, and return a dictionary of cleaned values. 

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
  eg removing "*" prefixes etc
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:
{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}
"""
import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS = {'rdf-schema#label': 'label',
          'URI': 'uri',
          'rdf-schema#comment': 'description',
          'synonym': 'synonym',
          'name': 'name',
          'family_label': 'family',
          'class_label': 'class',
          'phylum_label': 'phylum',
          'order_label': 'order',
          'kingdom_label': 'kingdom',
          'genus_label': 'genus'}
'''
#APPROACH 1
def process_file(filename, fields):

    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:

          line['rdf-schema#label'] = re.sub('\(.+\)', '', line['rdf-schema#label']).strip()
          if line['rdf-schema#label'] == 'NULL':
            line['rdf-schema#label'] = None

          if line['name'] == 'NULL' or re.search(r'\W', line['name']):
            line['name'] = line['rdf-schema#label']

          if line['synonym'] == 'NULL':
            line['synonym'] = None
          else:
            line['synonym'] = parse_array(line['synonym'])
            for syn in line['synonym']:
              syn.replace('*', "")

          item = {}
          item['classification'] = {}

          for key in fields:

            if line[key] == 'NULL':
              line[key] = None

            if re.search(r'_label', key):
              item['classification'][fields[key]] = line[key]
            else:
              item[fields[key]] = line[key]

          data.append(item)

    return data
'''

#APPROACH 2
def process_file(filename, fields):
    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        # header = reader.fieldnames
        #print header
        for i in range(3):
            l = reader.next()

        for line in reader:
            # YOUR CODE HERE
            field_dict = {}
            class_dict = {}
            for i in process_fields:
                #print i, line[i]
                #print fields[i], '\n'
                if i == "rdf-schema#label":
                    line[i] = re.sub(r'\s[(][a-z]+[)]', r'', line[i])
                    #line[i] = re.sub(r'[(][a-z]+[)]',r'', line[i]).strip()
                    #line[i] = line[i].replace("(spider)","").replace("(mites)","")

                elif i == "name":
                    #line[i] = re.sub(r'^[^a-zA-Z0-9]+[a-zA-Z0-9]+|NULL', line["rdf-schema#label"], line[i])
                    line[i] = re.sub(r'^\W+\w+|NULL', line["rdf-schema#label"], line[i])

                elif line[i] == "NULL":
                    line[i] = None

                elif i == "synonym":
                    d = []
                    line[i] = parse_array(line[i])
                    for j in line[i]:
                        #j = re.sub(r'^[*]', r'',j).lstrip()
                        j = re.sub(r'^\*', r'', j).lstrip()
                        d.append(j)
                    line[i] = d

                elif i in ['family_label', 'class_label', 'phylum_label', 'order_label', 'kingdom_label',
                           'genus_label']:
                    class_dict[fields[i]] = line[i]

            for i in process_fields:
                if i not in ['family_label', 'class_label', 'phylum_label', 'order_label', 'kingdom_label',
                             'genus_label']:
                    field_dict[fields[i]] = line[i]
                else:
                    field_dict["classification"] = class_dict

            data.append(field_dict)
            #pass

            #print data
            #for i in data:
            #print i["label"]
            #print i["name"]
            #print i["synonym"]
    # print len(data) # 76
    #print data[0] # first_entry
    #print "My first entry:"
    pprint.pprint(data[0])
    #print data[17]["name"] # "Ogdenia"
    #print data[48]["label"] # "Hydrachnidiae"
    #print data[14]["synonym"] # ["Cyrene Peckham & Peckham"]
    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)


    first_entry = {
        'classification': {
            'class': 'Arachnid',
            'family': 'Orb-weaver spider',
            'kingdom': 'Animal',
            'order': 'Spider',
            'phylum': 'Arthropod'},
        'description': 'The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced.',
        'label': 'Argiope',
        'name': 'Argiope',
        'synonym': None,
        'uri': 'http://dbpedia.org/resource/Argiope_(spider)'}

    '''
    assert data[0] == {
                        "synonym": None, 
                        "name": "Argiope", 
                        "classification": {
                            "kingdom": "Animal", 
                            "family": "Orb-weaver spider", 
                            "order": "Spider", 
                            "phylum": "Arthropod", 
                            "genus": None, 
                            "class": "Arachnid"
                        }, 
                        "uri": "http://dbpedia.org/resource/Argiope_(spider)", 
                        "label": "Argiope", 
                        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
                    }
    '''
    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]


if __name__ == "__main__":
    test()