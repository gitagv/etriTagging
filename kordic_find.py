import pymongo
connection = pymongo.MongoClient("203.255.81.137", 27017)
kordicDB = connection.kordicDB
data = kordicDB.data_2014
word = '가속도'
list = data.find({"word": word})
for l in list:
    print("word : %s, pos : %s, WSD : %s, 의미: %s" %(l['word'],l['pos'],l['meannum1'],l['mean']))
