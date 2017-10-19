# # DB insert
# # create by Kitak Park.
import codecs
import glob
import json
import os
from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_legal_WSD_NE
original = etri.original

collection_1 = etri['Group1']

Group1 = ['국회법', '헌법']

for c in collection_1.find():
    if c['title']['text'] in Group1:
        print(c['title']['text'])
        for sentence in c['sentence']:
            print(sentence['id'],sentence['text'])
            # if c['title']['text'] == '국회법' and sentence['id'] == 335:
            #     break
        print('\n')
