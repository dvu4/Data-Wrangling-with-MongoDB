#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Broken Request

from bs4 import BeautifulSoup
import requests
import json

r = requests.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(r.text)

eventvalidation_element = soup.find(id = "__EVENTVALIDATION")
eventvalidation= eventvalidation_element["value"]

viewstate_element = soup.find(id = "__VIEWSTATE")
viewstate= viewstate_element["value"]
 
r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                  data={'AirportList': "BOS",
                        'CarrierList': "VX",
                        'Submit': 'Submit',
                        "__EVENTTARGET": "",
                        "__EVENTARGUMENT": "",
                        "__EVENTVALIDATION": eventvalidation,
                        "__VIEWSTATE": viewstate})

f = open("virgin_and_logan_airport_broken.html","w")
f.write(r.text)
