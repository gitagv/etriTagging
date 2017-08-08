# # DB news WSD insert
# # create by Kitak Park.
import codecs
import glob
import json
import os
from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_wsd
original = etri.original
test = etri.test

collection_1 = etri['1-희연']
collection_2 = etri['1-현진']
collection_3 = etri['2-영훈']
collection_4 = etri['2-중식']
collection_5 = etri['3-민숙']
collection_6 = etri['3-지원']
collection_7 = etri['4-덕진']
collection_8 = etri['4-시은']

Group1 = ['20170112-0010008954105.txt.json', '20170319-0010009118371.txt.json', '20170521-4210002742987.txt.json']
Group2 = ['20170527-0230003283619.txt.json', '20170609-0230003287020.txt.json', '20170613-0010009332942.txt.json']
Group3 = ['20170502-0050000988519.txt.json', '20170526-0230003283202.txt.json', '20170622-0030008026025.txt.json']
Group4 = ['20170120-0250002678055.txt.json', '20170522-4210002744977.txt.json', '20170608-0010009321581.txt.json']

FILES = glob.glob(os.path.join('./20170714_news_300_ne_wsd', '*.json'))

for FILE in FILES:
    f = FILE.split('\\')[1]

    insertT = json.load(codecs.open(FILE, 'r', encoding='utf-8-sig'))

    original.insert(insertT)
    test.insert(insertT)

    if f in Group1:
        collection_1.insert(insertT)
        collection_2.insert(insertT)
    elif f in Group2:
        collection_3.insert(insertT)
        collection_4.insert(insertT)
    elif f in Group3:
        collection_5.insert(insertT)
        collection_6.insert(insertT)
    elif f in Group4:
        collection_7.insert(insertT)
        collection_8.insert(insertT)