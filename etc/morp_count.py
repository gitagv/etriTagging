# # morp count
# # create by Kitak Park.
from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_patent_morp
original = etri.original

AlldocumentN = 0
AllsentenceN = 0
AllmorpN = 0
GroupN = 1
for o in original.find():
    sentenceN = 0
    morpN = 0

    print(o['title']['text'])

    AlldocumentN += 1

    for sentence in o['sentence']:
        AllsentenceN += 1
        sentenceN += 1

        for morp in sentence['morp']:
            AllmorpN += 1
            morpN += 1
    # print(sentenceN)
    # print(morpN)

    if AllmorpN >= 24000:
        print('여기까지 %s조 분량, 수 : %s\n' % (GroupN, AllmorpN))
        AllmorpN = 0
        GroupN += 1

print(AlldocumentN, AllsentenceN, AllmorpN)

