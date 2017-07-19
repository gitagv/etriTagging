# # DB insert
# # create by Kitak Park.

import glob
import json
import os
import pymongo
connection = pymongo.MongoClient("203.255.81.71", 27017)
etri = connection.etri
original = etri.original
submit = etri.submit

FILES = glob.glob(os.path.join('./170609_1차태깅문서_위키(35문서_756문장)', '*.json'))

for FILE in FILES:
    text = open(FILE, 'r', encoding='utf-8').read()
    insertT = json.loads(text)
    original.insert(insertT)
    submit.insert(insertT)
