from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.46')

db = client.etri_wiki

col = db['submit']

# findWord = ['게이지']

# for f in findWord:
#     print(f)
#     for c in col.find():
#         for sent in c['sentence']:
#
#             for morp in sent['morp']:
#                 if morp['lemma'] == f and morp['type'] != 'NNG':
#                     print("형태소")
#                     # morp.update({'type':'NNG'})
#                     print(c['title']['text'], sent['id'], morp['id'], morp['type'])
#
#             # for WSD in sent['WSD']:
#             #     if WSD['text'] == f and WSD['type'] == 'NNG':
#             #         if WSD['scode'] != '04':
#             #             print("WSD")
#             #             WSD.update({'type': 'NNG'})
#                         # WSD.update({'scode': '04'})
#                         # print(c['title']['text'], sent['id'], WSD['id'], WSD['type'], WSD['scode'])
#
#         # print('\n')
#         # col.save(c)

findWord = ['쪽']
for f in findWord:
    print(f)
    for c in col.find():
        for sent in c['sentence']:

            for morp in sent['morp']:
                if morp['lemma'] == f and morp['type'] == 'NNG':
                    print("형태소")
                    print(c['title']['text'],sent['id'],morp['id'], morp['type'])
    print('\n')
#             for WSD in sent['WSD']:
#                 if WSD['text'] == f and WSD['type'] != 'MM':
#                     print("WSD")
#                     print(c['title']['text'],sent['id'],WSD['id'], WSD['type'], WSD['scode'])
#         print('\n')