#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Successful Request

from bs4 import BeautifulSoup
import requests
import json


s= requests.Session()

r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")

soup = BeautifulSoup(r.text)

eventvalidation_element = soup.find(id = "__EVENTVALIDATION")
eventvalidation= eventvalidation_element["value"]

viewstate_element = soup.find(id = "__VIEWSTATE")
viewstate= viewstate_element["value"]
 
r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                  data={'AirportList': "BOS",
                        'CarrierList': "VX",
                        'Submit': 'Submit',
                        "__EVENTTARGET": "",
                        "__EVENTARGUMENT": "",
                        "__EVENTVALIDATION": eventvalidation,
                        "__VIEWSTATE": viewstate})

f = open("virgin_and_logan_airport_successful.html","w")
f.write(r.text)

