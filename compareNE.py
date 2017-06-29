import pymongo
connection = pymongo.MongoClient("203.255.81.137", 27017)
etri = connection.etri
test1 = etri.test5
test2 = etri.test6

ne_cnt = 0
dic1 = {}
for t1 in test1.find():
    for senNum, sentence in enumerate(t1['sentence']):
        if senNum <= 46:
            for neNum, ne in enumerate(sentence['NE']):
                ne_cnt +=1
                dic1[str(senNum) + '_' + str(neNum)] = ne['text'] + '_' + ne['type']

dic2 = {}
for t2 in test2.find():
    for senNum, sentence in enumerate(t2['sentence']):
        if senNum <= 46:
            for neNum, ne in enumerate(sentence['NE']):
                dic2[str(senNum) + '_' + str(neNum)] = ne['text'] + '_' + ne['type']
allcnt = 0
samecnt = 0
for d in dic1:
    allcnt +=1
    if dic1[d] == dic2[d]:
        samecnt += 1
    else:
        print(d)
        print("5: %s, 6: %s" %(dic1[d], dic2[d]))

print(ne_cnt)
print(allcnt)
print(samecnt/allcnt)

