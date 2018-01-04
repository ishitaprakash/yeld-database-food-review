#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:10:54 2017

@author: ishitaprakash
"""

import io
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
import json
import csv
import requests
import sys  
import codecs
import os
import time
mins=0
frequency_good = { }
frequency_bad = { }
astars5_good=""
astars5_bad=""
count=0
final={}
final_list={}
counter=0

review_string=""
bus_id_temp=""
final_good=[]
final_bad=[]
new_list_good=[]
new_list_bad=[]
current_sec=time.time()
def remove_if_exists(i,value):
    try:
       i.remove(value)
    except ValueError:
              pass
for line in open('input.json'):
        
        count=0
        review_string = ""
        data = json.loads(line)
        bus_id=data["business_id"]
        if(bus_id_temp!=bus_id) :
          bus_id_temp=""
          final_good=[]
          final_bad=[]
          resultwords=[]
          frequency_good.clear()
          frequency_bad.clear()
          final_str_good="" 
          final_str_bad=""
          new_list_good.clear();
          new_list_bad.clear();
          astars5_good=""
          astars5_bad=""

          



          
        bus_id_temp=bus_id
        stars=data["stars"]
        if(stars==5 or stars==4 or stars==3):
              review_string="good"
              astars5_good=astars5_good+(data["text"].lower())
              splitted_data_good=""
              stopwordsgood=list(stopwords.words('english'))
              stopwords_good=stopwordsgood+["food",'not','credit','order','from','This','is','by','far','the','I','have','ever','been','too','time', 'of', 'year', 'am', 'all', 'about','make', 'for', 'a','to', 'give', 'or', 'to', 'receive!', 'If', 'you', 'are', 'anything', 'like', 'me......and', 'earned', 'title','as', 'a', 'kid......because', 'ate', 'all','out', 'of','out', 'of','out', 'of','and', 'put','part', 'back', 'in', 'package...thinking', 'no', 'one', 'would', 'notice......then', 'get','instead.', 'Not', 'that', 'you', 'wont', 'make', 'up', 'difference', 'eating', '20', 'of', 'them', 'you', 'will', 'just', 'think', 'your', 'eating', 'less','them,','less.','too.','us','Eric','place!','treats,','my','was','off','way','but','with','this','it,','food,', 'on,', 'which,', 'there,', 'because,', 'now,', 'store,', 'on,', 'there,', 'food,', 'which,','food,', 'on,', 'which,', 'there,','food,', 'on,', 'which,', 'there,','food,', 'on,', 'which,', 'there,','it,', 'there,', 'food,', 'on,','found','best','spring','enjoy','app','ordered','good','came','come','felt','today','another','place','rapid','told','Im','eat','ate','eaten','eating','place','place.','restaurant','food.','-',"don't",'got','&',',','great','here.','return.','im',"it's",'little','micheal','said','water','late.','even','saw',"wong's",'love','liked','looking','special',"i'm", "i'll","didn't", 'much','pretty','much','usually','bad','years.']
              
              splitted_data_good=astars5_good.split();
              resultwords_good  = [word for word in splitted_data_good if word not in stopwords_good]
              
              for word in resultwords_good:
               count = frequency_good.get(word,0)
               frequency_good[word] = count + 1

              new_list_good = sorted(frequency_good.items(),key=lambda item: item[1],reverse=True)
              
              
        elif (stars==2 or stars==1):
              review_string="bad"
              astars5_bad=astars5_bad+(data["text"].lower())
              splitted_data_bad=""

              stopwordsbad=list(stopwords.words('english'))
              stopwords_bad=stopwordsbad+["food",'not','credit','order','from','This','is','by','far','the','I','have','ever','been','too','time', 'of', 'year', 'am', 'all', 'about','make', 'for', 'a','to', 'give', 'or', 'to', 'receive!', 'If', 'you', 'are', 'anything', 'like', 'me......and', 'earned', 'title','as', 'a', 'kid......because', 'ate', 'all','out', 'of','out', 'of','out', 'of','and', 'put','part', 'back', 'in', 'package...thinking', 'no', 'one', 'would', 'notice......then', 'get','instead.', 'Not', 'that', 'you', 'wont', 'make', 'up', 'difference', 'eating', '20', 'of', 'them', 'you', 'will', 'just', 'think', 'your', 'eating', 'less','them,','less.','too.','us','Eric','place!','treats,','my','was','off','way','but','with','this','it,','food,', 'on,', 'which,', 'there,', 'because,', 'now,', 'store,', 'on,', 'there,', 'food,', 'which,','food,', 'on,', 'which,', 'there,','food,', 'on,', 'which,', 'there,','food,', 'on,', 'which,', 'there,','it,', 'there,', 'food,', 'on,','found','best','spring','enjoy','app','ordered','good','came','come','felt','today','another','place','rapid','told','Im','eat','ate','eaten','eating','place','place.','restaurant','food.','-',"don't",'got','&',',','great','here.','return.','im',"it's",'little','micheal','said','water','late.','even','saw',"wong's",'love','liked','looking','special',"i'm", "i'll","didn't", 'much','pretty','much','usually','bad','years.']
              
              splitted_data_bad=astars5_bad.split();
              resultwords_bad  = [word for word in splitted_data_bad if word not in stopwords_bad]
          
              for word in resultwords_bad:
               count = frequency_bad.get(word,0)
               frequency_bad[word] = count + 1

              new_list_bad = sorted(frequency_bad.items(),key=lambda item: item[1],reverse=True) 
        
        
       
       
        
        for x in range(0,2): 

            
            if(review_string=="good"):
                 final_str_good=(new_list_good[x][0])
                 remove_if_exists(final_good,final_str_good)
                 final_good.append(final_str_good)
                 final[bus_id]={'good':final_good,'bad':final_bad} 
            if(review_string=="bad"):
                 final_str_bad=(new_list_bad[x][0])
                 remove_if_exists(final_bad,final_str_bad)
                 final_bad.append(final_str_bad)
                 final[bus_id]={'good':final_good,'bad':final_bad} 
with open('output.json', 'a') as f:    
 for bus_id in final:
    counter=counter+1
    print("business_id"+":"+bus_id,final[bus_id])
    print("\n")
    json.dump(bus_id,f)
    json.dump(final[bus_id], f)
    f.write('\n')
f.close()
print(time.time()-current_sec)
    