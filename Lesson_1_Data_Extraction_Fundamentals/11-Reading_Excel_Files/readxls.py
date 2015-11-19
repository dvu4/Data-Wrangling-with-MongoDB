#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min and max values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""
'''
import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()
'''
import xlrd
import os
import numpy
import pprint

DATADIR = "/Users/ducvu/Documents"
DATAFILE = "2013_ERCOT_Hourly_Load_Data.xls"



def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)


    '''
    #print sheet.col_values(1, start_rowx=1,end_rowx=7295)
    coast = sheet.col_values(1, start_rowx=1,end_rowx=7295)
    max_val = max(coast)
    max_index = coast.index(max_val)+1
    min_val = min(coast)
    min_index = coast.index(min_val)+1
    #avg_val = numpy.mean(coast)
    #avg_val = float(sum(coast)/len(coast))
    avg_val = sum(coast)/float(len(coast))
    
    print "The max of COAST is:",max_val,"\n"
    print "The max of index is:",max_index+1,"\n"
    print "The min of COAST is:",min_val,"\n"
    print "The min of index is:",min_index+1,"\n"
    print "The average of COAST is:",avg_val,"\n"
    
    print "\nDATES:"
    print "Type of data in cell (row 1, col 0):", 
    print sheet.cell_type(max_index+1, 0)
    maxtime = sheet.cell_value(max_index, 0)
    print "Time in Excel format:",
    print maxtime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    #print xlrd.xldate_as_tuple(maxtime, 0)
    maxt = xlrd.xldate_as_tuple(maxtime, 0)
    print maxt
    
    print sheet.cell_type(min_index+1, 0)
    mintime = sheet.cell_value(min_index, 0)
    print "Time in Excel format:",
    print mintime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    #print xlrd.xldate_as_tuple(mintime, 0)
    mint = xlrd.xldate_as_tuple(mintime, 0)
    print mint

    data = {
            'maxtime': maxt,
            'maxvalue': max_val,
            'mintime': mint,
            'minvalue': min_val,
            'avgcoast': avg_val
    }
    return data
    '''
    
    # approach 2
    '''
    coast = sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows +1)
    max_row = coast.index(max(coast)) + 1
    min_row = coast.index(min(coast)) + 1
    print 'max row is:', max_row
    print 'min row is:', min_row
    
    data = {
            'maxtime': xlrd.xldate_as_tuple(sheet.cell_value(max_row, 0), 0),
            'maxvalue': sheet.cell_value(max_row, 1),
            'mintime': xlrd.xldate_as_tuple(sheet.cell_value(min_row, 0), 0),
            'minvalue': sheet.cell_value(min_row, 1),
            'avgcoast': sum(coast)/len(coast)
    }
    return data
    '''
    # SOLUTION
    coast = sheet.col_values(1, start_rowx=1, end_rowx=None)
    maxval = max(coast)
    minval = min(coast)

    maxpos = coast.index(maxval) + 1
    minpos = coast.index(minval) + 1

    maxtime = sheet.cell_value(maxpos, 0)
    realmaxtime = xlrd.xldate_as_tuple(maxtime, 0)
    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)

    data = {
            'maxtime' : realmaxtime,
            'maxvalue': maxval,
            'mintime' : realmintime,
            'minvalue': minval,
            'avgcoast': sum(coast)/ float(len(coast))
            }
    return data

    
    

def test():
    #open_zip(datafile)
    datafile = os.path.join(DATADIR, DATAFILE)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)
    pprint.pprint(data)


test()
'''
datafile = os.path.join(DATADIR, DATAFILE)
data = parse_file(datafile)
'''
