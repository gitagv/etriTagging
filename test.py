# # DB test
# # create by Kitak Park.

import json
import pymongo
connection = pymongo.MongoClient("203.255.81.137", 27017)
etri = connection.etri
origin = etri.test1

FILE = './170609_1차태깅문서_위키(35문서_756문장)/0007435_힘 (물리)(본문).json'
text = open(FILE, 'r', encoding='utf-8').read()
insertT = json.loads(text)
origin.insert(insertT)