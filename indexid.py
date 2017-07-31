from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.46')

etri = connection.etri_wiki
submit = etri.submit

for s in submit.find():
    print(s['title']['text'])
    for sentence in s['sentence']:
        for id, morp in enumerate(sentence['morp']):
            morp.update({'id':id})
            submit.save(s)