# # DB insert
# # create by Kitak Park.

import glob
import json
import os
import pymongo
connection = pymongo.MongoClient("203.255.81.71", 27017)
etri = connection.etri_news
original = etri.original
submit = etri.submit
test = etri.test

collection_1 = etri['1-희연']
collection_2 = etri['1-현진']
collection_3 = etri['2-영훈']
collection_4 = etri['2-중식']
collection_5 = etri['3-민숙']
collection_6 = etri['3-지원']
collection_7 = etri['4-덕진']
collection_8 = etri['4-시은']

Group1 = ['20170112-0010008954105.txt', '20170319-0010009118371.txt', '20170521-4210002742987.txt']
Group2 = ['20170527-0230003283619.txt', '20170609-0230003287020.txt', '20170613-0010009332942.txt']
Group3 = ['20170502-0050000988519.txt', '20170526-0230003283202.txt', '20170622-0030008026025.txt']
Group4 = ['20170120-0250002678055.txt', '20170522-4210002744977.txt', '20170608-0010009321581.txt']

# FILES = glob.glob(os.path.join('./170609_1차태깅문서_위키(35문서_756문장)', '*.json'))
FILES = glob.glob(os.path.join('./20170714_news_300', '*.txt'))


for FILE in FILES:
    f = FILE.split('\\')[1]
    print(f.split('-')[0])

    text = open(FILE, 'r', encoding='utf-8').read()
    insertT = json.loads(text)
    # original.insert(insertT)
    # test.insert(insertT)
    # submit.insert(insertT)
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