import pymongo
connection = pymongo.MongoClient("203.255.81.137", 27017)
etri = connection.etri
test1 = etri.test1
test2 = etri.test2

dic1 = {}
for t1 in test1.find():
    for senNum, sentence in enumerate(t1['sentence']):
        if senNum <= 7:
            for morpNum, morp in enumerate(sentence['morp']):
                dic1[str(senNum) + '_' + str(morpNum)] = morp['lemma'] + '_' + morp['type']

dic2 = {}
for t2 in test2.find():
    for senNum, sentence in enumerate(t2['sentence']):
        if senNum <= 7:
            for morpNum, morp in enumerate(sentence['morp']):
                dic2[str(senNum) + '_' + str(morpNum)] = morp['lemma'] + '_' + morp['type']
cnt = 0

for d in dic1:
    if dic1[d] == dic2[d]:
        cnt += 1
    else:
        print(dic1[d], dic2[d])
