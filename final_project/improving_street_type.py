"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

osmfile = "boston_massachusetts.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons"]


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

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

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



def update_name(name, mapping,rex):
    '''
     This function takes a string with street name as an argument 
     and replace these abbreviated street types with the fixed name.
     Args:
        name(string): street name to update.
        mapping(dictionary): a mapping dictionary.
        rex(regex): a compiled regular expression to match against the street_name.
    '''

    #m = street_type_re.search(name)
    m = rex.search(name)
    if m:
        street_type = m.group()
        new_street_type = mapping[street_type]
        name = re.sub(rex, new_street_type, name) # re.sub(old_pattern, new_pattern, file)
        #name = street_type_re.sub(new_street_type, name)
    return name

def test():
    st_types = audit(osmfile)
    pprint.pprint(dict(st_types))
    
        
    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping, rex = street_type_re)
            print name, "=>", better_name
            

if __name__ == '__main__':
    test()