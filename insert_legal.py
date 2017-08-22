# # DB insert
# # create by Kitak Park.
import codecs
import glob
import json
import os
from pymongo import MongoClient

# connection = MongoClient('mongodb://root:nlp44342@203.255.81.46')
# connection = MongoClient('mongodb://myUserAdmin:abc123@203.255.81.70')
connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_legal_morp
original = etri.original
# submit = etri.submit
test = etri.test

collection_1 = etri['Group1']
collection_3 = etri['Group2']
collection_5 = etri['Group3']
collection_7 = etri['Group4']

Group1 = ['국회법(수정).json', '헌법(수정).json']
Group2 = ['국회법(수정).json', '정부조직법(수정).json']
Group3 = ['독일연방공화국 기본법(수정).json', '러시아 연방 헌법(수정).json', '일본국헌법(수정).json', '프랑스 헌법(수정).json']
Group4 = ['국회법(수정).json',  '미국 연방 헌법(수정).json']

FILES = glob.glob(os.path.join('./20170801_legal_2179', '*.json'))

for FILE in FILES:
    f = FILE.split('\\')[1]
    insertT = json.load(codecs.open(FILE, 'r', encoding='utf-8-sig'))
    #
    original.insert(insertT)
    test.insert(insertT)
    # # submit.insert(insertT)
    if f in Group1:
        collection_1.insert(insertT)
    if f in Group2:
        collection_3.insert(insertT)
    if f in Group3:
        collection_5.insert(insertT)
    if f in Group4:
        collection_7.insert(insertT)
