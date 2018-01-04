#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:50:09 2017

@author:  aishwaryamajumder
"""

import time
import json
import csv
import requests
import sys  
import codecs
import os

with open('reviewAZTempe.json', 'a') as g:
    for line in codecs.open('review.json', 'r', 'UTF-8'):
        data = json.loads(line)
        for line1 in open('businessAZTempe.json'):
            data1 = json.loads(line1)
            if(data["business_id"]==data1["business_id"]):
                print("----------------------\n",data1["name"],"\n",data["text"],"\n----------------------\n" )
                json.dump(data, g)
                g.write('\n')
g.close()
#==============================================================================
#     data = json.loads(line1.decode('unicode-escape'))
#     print(data)
# #==============================================================================

 

#==============================================================================
# 
#     colsToRemove = ('neighborhood','longitude','latitude','is_open','hours')
#     for cols in colsToRemove:
#         data.pop(cols, None)
#     with open('businessAZTempe.json', 'a') as f:    
#         if(data["state"]=='AZ' and data["city"]=='Tempe'):
#             json.dump(data, f)
#             f.write('\n')
# f.close()
#==============================================================================
