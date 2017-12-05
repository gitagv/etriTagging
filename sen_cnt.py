# # DB insert
# # create by Kitak Park.
import codecs
import glob
import json
import os
from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.46')
# connection = MongoClient('mongodb://myUserAdmin:abc123@203.255.81.70')
# connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

# etri = connection.etri_wiki
# etri = connection.etri_news
etri = connection.etri_legal
# etri = connection.etri_patent

# original = etri.original
submit = etri.submit
# test = etri.test

for s in submit.find():
    sen_cnt = 0
    print(s['title']['text'])
    for sen in s['sentence']:
        sen_cnt += 1

    print(sen_cnt)
