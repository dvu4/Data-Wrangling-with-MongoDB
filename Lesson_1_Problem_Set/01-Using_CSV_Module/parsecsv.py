#!/usr/bin/env python
"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""
import csv
import os

DATADIR = ""
DATAFILE = "745090.csv"


def parse_file(datafile):
    name = " "
    data = []

    '''
    da = []
    with open(datafile,'rb') as f:
        #pass
        name = f.readline().replace('"','').strip("\n").split(",")[1]
        print name
        f.next()
        da = list(csv.reader(f, delimiter = " ", quotechar='|'))
        for r in da:
            print('|'.join(r)) # convert list to string
    data = ['|'.join(r).split(",") for r in da]
    '''
    '''
    # approach 2

    with open(datafile, 'rb') as f:
        reader = csv.reader(f)
        name = reader.next()[1]
        print name
        reader.next()

        for row in reader:
            data.append(row)

    return (name, data)
    
    
    '''
    # Solution
    with open(datafile,'rb') as f:
        reader = csv.reader(f)
        name = reader.next()[1]
        print name
        header = reader.next()
        data = [row for row in reader]
        #for r in data:
        #    print r

    
    # Do not change the line below
    return (name, data)


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()
'''
datafile = os.path.join(DATADIR, DATAFILE)
name, data = parse_file(datafile)

assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
assert data[0][1] == "01:00"
assert data[2][0] == "01/01/2005"
assert data[2][5] == "2"
'''
