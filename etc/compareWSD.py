import pymongo
connection = pymongo.MongoClient("203.255.81.137", 27017)
etri = connection.etri
test1 = etri.test3
test2 = etri.test44

dic1 = {}
for t1 in test1.find():
    for senNum, sentence in enumerate(t1['sentence']):
        if senNum <= 3:
            for wsdNum, WSD in enumerate(sentence['WSD']):
                dic1[str(senNum) + '_' + str(wsdNum)] = WSD['text'] + '_' + WSD['scode']

dic2 = {}
for t2 in test2.find():
    for senNum, sentence in enumerate(t2['sentence']):
        if senNum <= 3:
            for wsdNum, WSD in enumerate(sentence['WSD']):
                dic2[str(senNum) + '_' + str(wsdNum)] = WSD['text'] + '_' + WSD['scode']

allcnt = 0
samecnt = 0
for d in dic1:
    allcnt +=1
    if dic1[d] == dic2[d]:
        samecnt += 1
    else:
        print(d)
        print("3: %s, 4: %s" %(dic1[d], dic2[d]))

print(allcnt)
samecnt -= 1
print(samecnt/allcnt)

