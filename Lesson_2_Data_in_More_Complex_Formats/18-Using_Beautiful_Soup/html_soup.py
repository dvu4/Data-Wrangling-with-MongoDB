#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI
# All your changes should be in the 'extract_data' function

from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html)
        data["eventvalidation"] = soup.find(id= "__EVENTVALIDATION")["value"]
        data["viewstate"] = soup.find(id= "__VIEWSTATE")["value"]

        '''
        # SOLUTION
        soup = BeautifulSoup(html)
        ev = soup.find(id = "__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]

        vs = soup.find(id = "__VIEWSTATE")
        data["viewstate"] = vs["value"]
        '''

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text

    
def test():
    data = extract_data(html_page)
    print 'EVENTVALIDATION is : \n',data["eventvalidation"][:100]
    print 'VIEWSTATE is : \n',data["viewstate"][:100]
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")

    
test()

'''
def options(soup, id):
    option_values = []
    carrier_list = soup.find(id=id)
    for option in carrier_list.find_all('option'):
        option_values.append(option['value'])
    return option_values

der main():
    soup = BeautifulSoup(open("virgin_and_logan_airport.html"))

    codes = options(soup, 'CarrierList')

    codes = options(soup, 'AirportList')
'''
