from pymongo import MongoClient

# connection = MongoClient('mongodb://root:nlp44342@203.255.81.46')
# etri = connection.etri_wiki
# submit = etri.submit

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')
etri = client.etri_news
submit = etri.submit

for s in submit.find():
    # print(s['title']['text'])
    print(s['_id'])
    for sentence in s['sentence']:
        for id, morp in enumerate(sentence['morp']):
            morp.update({'id':id})
            submit.save(s)