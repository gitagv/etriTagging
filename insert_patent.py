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

# etri = connection.etri_patent_morp
etri = connection.etri_patent_wsd_ne
original = etri.original
submit = etri.submit
test = etri.test

collection_1 = etri['Group1']
collection_3 = etri['Group2']
collection_5 = etri['Group3']
collection_7 = etri['Group4']

Group1 = ['1020000022266.json','1020000083784.json','1020010036478.json','1020010054421.json','1020010080185.json',
          '1020010087411.json','1020020018004.json','1020020084454.json','1020030028272.json','1020030056364.json']
Group2 = ['1020040056582.json','1020040056584.json','1020040056638.json','1020040078406.json','2020070018478.json',
          '1020050019814.json','1020050064310.json','1020090051233.json','1020080019940.json','1020080020188.json']
Group3 = ['1020120144532.json','1020130021737.json','1020130053682.json','1020140137731.json','1020150042306.json',
          '1020050015959.json','2020130001049.json','1020120115740.json','1020110138719.json']
Group4 = ['1020020053700.json','1020100120827.json','1020110025339.json','1020110050673.json','1020110104047.json',
          '1020120127894.json','1020120030889.json','1020120087002.json','1020080010234.json']

FILES = glob.glob(os.path.join('./4-특허-MLT+autoWSD,NE', '*.json'))

arr = []
for FILE in FILES:
    f = FILE.split('\\')[1]
    print(f)
    insertT = json.load(codecs.open(FILE, 'r', encoding='utf-8-sig'))

    original.insert(insertT)
    test.insert(insertT)
    submit.insert(insertT)

    if f in Group1:
        collection_1.insert(insertT)
    if f in Group2:
        collection_3.insert(insertT)
    if f in Group3:
        collection_5.insert(insertT)
    if f in Group4:
        collection_7.insert(insertT)
