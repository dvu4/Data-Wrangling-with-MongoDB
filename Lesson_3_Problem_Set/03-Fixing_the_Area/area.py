#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

import re
CITIES = 'cities.csv'


# ALTERNATIVE 1
def fix_area(area):
    
    # YOUR CODE HERE
    if area != 'NULL':
        area = re.sub(r'[{}|]', r' ',area).strip().split()
        
        if len(area) > 1:
            area = float(max(area, key =len))
            '''
            if len(area[0]) == len(area[1]):
                area = float(max(area[0],area[1])) 
            else:
                area = float(max(area, key =len))
            '''
        else:
            area = float(area[0])
        
                             
    else:
        area= None
            
    #print area
    return area


'''
#ALTERNATIVE 2
def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def fix_area(area):

    if is_float(area):
        return area
    elif area[0] == "{":
        areas = area.replace('{','').replace('}','').split('|')
        return float(max(areas, key = lambda x: len(x.split('e')[0])))
    else:
        return None        

    return area
'''

def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #print reader.fieldnames

        #skipping the extra matadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            #print line['name']
            print line['populationTotal']
            #print line['areaMetro']
            #print line['postalCode']
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[8]["areaLand"] == 55166700.0
    assert data[3]["areaLand"] == None


if __name__ == "__main__":
    test()
