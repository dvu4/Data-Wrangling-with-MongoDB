# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = "/Users/ducvu/Documents"
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    '''
    data = []
    da = []
    with open(datafile, "r") as f:
        for line in f:
            print line
            da.append(line.strip('\n'))
        
    keys = da.pop(0).split(',')
    print "\n the keys are:",keys,"\n"
    for line in da:
        values = line.split(',')
        print "the values are:",values, "\n"
        data.append(dict(zip(keys,values))
    return data
    '''

    
    data = []
    values = []
    with open(datafile, "r") as f:
        keys = f.readline().strip("\n").split(",")
        print "\n the keys are:",keys,"\n"
        #f.next()
        for line in f:
            print line
            value = line.strip("\n").split(',')
            values.append(value)
    #print "\n the values are:",values,"\n"

    for v in values:
        print "the values are:",v, "\n"
        data.append(dict(zip(keys,v)))
    return data
        
    # solution
    '''
    data = []                
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break

        fields = line.split(",")
        entry = {}

        for i, value in enumerate(fields):
            entry[header[i].strip()] = value.strip()

        data.append(entry)
        counter += 1
    return data
    '''


    # approach 3
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")

        for line in f:
            data.append(dict(zip(header,line.strip().split(","))))
    return data

'''
def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline
    
test()
'''

datafile = os.path.join(DATADIR, DATAFILE)
d = parse_file(datafile)
firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
#print d[0]
#print d[9]
for i in d:
    print "\n",i
