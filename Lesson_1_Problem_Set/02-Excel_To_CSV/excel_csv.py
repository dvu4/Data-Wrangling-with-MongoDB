# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile
from csv import DictWriter
'''
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"
'''

DATADIR = "/Users/ducvu/Documents"
DATAFILE = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

'''
## solution
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = {}
    # process all rows that contain station data
    for n in range (1, 9):
        station = sheet.cell_value(0, n)
        cv = sheet.col_values(n, start_rowx=1, end_rowx=None)

        maxval = max(cv)
        maxpos = cv.index(maxval) + 1
        maxtime = sheet.cell_value(maxpos, 0)
        realtime = xlrd.xldate_as_tuple(maxtime, 0)
        data[station] = {"maxval": maxval,
                         "maxtime": realtime}

    print data
    return data

def save_file(data, filename):
    with open(filename, "w") as f:
        w = csv.writer(f, delimiter='|')
        w.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for s in data:
            year, month, day, hour, _ , _= data[s]["maxtime"]
            w.writerow([s, year, month, day, hour, data[s]["maxval"]])
'''    

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = []
    data1 = []
    max_val = []
    max_index = []
    maxtime = []
    maxt = []
    year = []
    month = []
    date = []
    hour = []
    station = []
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    
    #cell = sheet.cell(0,1)
    #print cell
    #print cell.value
    #print type(cell.value)
    
    for i in range(1,10):
        #print str(sheet.cell(0,i).value)
        station.append(str(sheet.cell(0,i).value))
        
        load = sheet.col_values(i, start_rowx=1,end_rowx=7295)
        max_val.append(max(load))
        max_index.append(load.index(max_val[i-1])+1)
        maxtime.append(sheet.cell_value(max_index[i-1], 0))
        maxt.append(xlrd.xldate_as_tuple(maxtime[i-1], 0))
        
        year.append(list(maxt[i-1])[0])
        month.append(list(maxt[i-1])[1])
        date.append(list(maxt[i-1])[2])
        hour.append(list(maxt[i-1])[3])
        
    '''
    print "the max value is:",max_val
    print "the max index is:",max_index
    print "Time in Excel format:\n",
    for i in maxtime:
        print i
    print "Convert time to a Python datetime tuple, from the Excel float: \n",
    for j in maxt:
        print j

    print "year:",year
    print "month:",month
    print "date:",date
    print "station:", station
    '''
    
    for i in range(len(station)):
        d = {
             'Max_Load': max_val[i],
             'Year': year[i],
             'Month': month[i],
             'Day': date[i],
             'Hour': hour[i]
        }
        data1.append(d)


    for i in range(len(station)):
        d = {
              station[i] : data1[i]
        }
        data.append(d)
        

    for i in range(len(data)):
        print data[i]
     

    return data


    '''
    data.append(['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load'])

    stations = sheet.row_values(0, start_colx=1, end_colx=9)

    max_load = 0

    for i in range(len(stations)):
        station_values = sheet.col_values(i + 1, start_rowx=1)

        max_row = station_values.index(max(station_values)) + 1
        Year, Month, Day, Hour, Minute, Second = xlrd.xldate_as_tuple(sheet.cell_value(max_row,0), 0)
        data.append([stations[i], Year, Month, Day, Hour, max(station_values)])
    return data
    '''

   
def save_file(data, filename):
    # YOUR CODE HERE
    '''
    for i in range(len(data)):
        for k,v in data[i].items():
            print k
            for k1,v1 in v.items():
                print k1,v1
    '''
    # approach1
    with open(filename, 'w') as csvfile:
        fieldnames = ('Station','Year', 'Month', 'Day', 'Hour', 'Max_Load')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        for d in data:
            k,v = d.items()[0]
            v['Station']=k
            writer.writerow(v)

  
    '''
    # approach2
    subkeys=["Year","Month","Day","Hour","Max_Load"]
    with open(filename, "w") as f:
        f.write("Station|Year|Month|Day|Hour|Max Load\n")
        for elem in data:
            for key in elem.keys():
                f.write(key)
                f.write("|")
                for k, subkey in enumerate(subkeys):
                    f.write(str(elem[key][subkey]))
                    if k < len(subkeys)-1:
                        f.write("|")
                f.write("\n")
    '''
    '''                
    # approach3
    with open(filename, 'wb') as f:
        f.write('|'.join(["Station", "Max Load", "Hour", "Date", "Month", "Year"]) + '\n')
        f.writelines('{}|{}|{}|{}|{}|{}'.format(k, *v.values()) + '\n' for l in data for k,v in l.items())
    '''

    '''
    with open(filename, 'wb') as of:
        writer = csv.writer(of, delimiter='|')

        for row in data:
            writer.writerow(row)
    '''
   

'''    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]

        
test()
'''
#open_zip(datafile)
datafile = os.path.join(DATADIR, DATAFILE)
data = parse_file(datafile)
save_file(data, outfile)

'''
toCSV = [{'name':'bob','age':25,'weight':200},
         {'name':'jim','age':31,'weight':180}]
keys = toCSV[0].keys()
with open('people.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)
'''


list_of_dict=[{'COAST': {'Max_Load': 18779, 'Month': 8, 'Day': 13, 'Hour': 17, 'Year': 2013}}, 
 {'EAST': {'Max_Load': 2380, 'Month': 8, 'Day': 5, 'Hour': 17, 'Year': 2013}}, 
 {'FAR_WEST': {'Max_Load': 2281, 'Month': 6, 'Day': 26, 'Hour': 17, 'Year': 2013}}, 
 {'NORTH': {'Max_Load': 1544, 'Month': 8, 'Day': 7, 'Hour': 17, 'Year': 2013}}, 
 {'NORTH_C': {'Max_Load': 24415, 'Month': 8, 'Day': 7, 'Hour': 18, 'Year': 2013}}, 
 {'SOUTHERN': {'Max_Load': 5494.157645, 'Month': 8, 'Day': 8, 'Hour': 16, 'Year': 2013}}, 
 {'SOUTH_C': {'Max_Load': 11433, 'Month': 8, 'Day': 8, 'Hour': 18, 'Year': 2013}}, 
 {'WEST': {'Max_Load': 1862, 'Month': 8, 'Day': 7, 'Hour': 17, 'Year': 2013}}, 
 {'ERCOT': {'Max_Load': 67595, 'Month': 8, 'Day': 7, 'Hour': 17, 'Year': 2013}}]


with open('names.csv', 'w') as csvfile:
    fieldnames = ('Station','Year', 'Month', 'Day', 'Hour', 'Max_Load')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter='|')
    writer.writeheader()
    for d in list_of_dict:
          k,v=d.items()[0]
          v['Station']=k
          writer.writerow(v)
