# # DB output json
# # create by Kitak Park.

import pymongo
connection = pymongo.MongoClient("203.255.81.46", 27017)
etri = connection.etri_wiki
submit = etri.submit

from bson.json_util import dumps
import json
import glob
import os

FILES = glob.glob(os.path.join('./170609_1차태깅문서_위키(35문서_756문장)', '*.json'))
FILENAME = [f.split('\\')[1] for f in FILES]
NAME = [f.split('_')[1].split('(본문)')[0] for f in FILENAME]

for s in submit.find():
    s['_id'] = ""
    for n in NAME:
        nindex = NAME.index(n)
        if s['title']['text'] == n:

            with open('./submit_json/' + FILENAME[nindex], 'w', encoding='utf-8') as f:
                f.write(s)
