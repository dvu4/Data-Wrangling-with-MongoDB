import xml.etree.cElementTree as ET
from collections import defaultdict
import pprint
import re


# indicate file to be read
osmfile = "boston_massachusetts.osm"

badZipCode = ["MA", "Mass Ave"]

zip_code_re = re.compile(r"(\d{5})(-\d{4})?$") #5 digits in a row @ end of string
                                           #and optionally dash plus 4 digits
                                           #return different parts of the match and an optional clause (?) 
                                           #for the dash and four digits at the end of the string ($)

# find the zipcodes
def get_postcode(element):
    if (element.attrib['k'] == "addr:postcode"):
        postcode = element.attrib['v']
        return postcode

    
# update zipcodes
def update_postal(postcode, rex):
     '''
     This function takes a string with zip code as an argument 
     and replace these wrong zip code with the fixed zip code.
     Args:
        postcode(string): zip code to update.
        rex(regex): a compiled regular expression to match against the zip code.
    '''
    
    if postcode is not None:
        zip_code = re.search(rex,postcode)
        if zip_code:
            postcode = zip_code.group(1)
                   
    return postcode


def audit(osmfile):
     '''
     This function return a dictionary with the key is the zip code 
     and the value is the number of that zip code in osm file.
     Args:
        filename(osm): openstreetmap file.
    '''
    osm_file = open(osmfile, "r")
    data_dict = defaultdict(int)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if get_postcode(tag):
                    postcode = get_postcode(tag)
                    data_dict[postcode] += 1 
    return data_dict


# test the zipcode audit and dict creation
def test():
    zip_code_types = audit(osmfile)
    pprint.pprint(dict(zip_code_types))
    
    for raw_zip_code in zip_code_types:
    if raw_zip_code not in badZipCode:
        better_zip_code = update_postal(raw_zip_code, rex = zip_code_re)
        print raw_zip_code, "=>", better_zip_code

if __name__ == '__main__':
    test()