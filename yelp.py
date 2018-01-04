#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:50:09 2017

@author:  ishitaprakash
"""

import time
import json
import csv
import requests

for line in open('business.json'):
    data = json.loads(line)

    colsToRemove = ('neighborhood','longitude','latitude','is_open','hours')
    for cols in colsToRemove:
        data.pop(cols, None)
    with open('businessAZTempe.json', 'a') as f:    
        for category in data["categories"]:
            if(category != 'Restaurants'):
                data.pop(category, None)
            elif(data["state"]=='AZ' and data["city"]=='Tempe'):
                print(data["categories"])
                json.dump(data, f)
                f.write('\n')
f.close()
#==============================================================================
#         js=json.dumps(data)
#         data2 = json.loads(js)
# #==============================================================================
#==============================================================================
#     json=json.dumps(data)
#==============================================================================
#==============================================================================
#         print(data)
#==============================================================================
#    print(data["name"])
#==============================================================================
#     
#     if(data["state"]=='AZ'):
#         print(data['name'],data['postal_code'],data['city'],data['state'])
# 
#==============================================================================
