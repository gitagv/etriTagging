from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')

db = client.etri_patent_wsd_ne

col = db['Group1']

totalne = 0

for a in col.find():
    for sent in a['sentence']:
        wsd_idx = 0
        ne_idx = 0
        for i in sent['WSD']:
            if wsd_idx != i['id']:
                print("WSD: ", a['title']['text'], sent['id'], i['id'])
            wsd_idx += 1

        for i in sent['NE']:
            if ne_idx != i['id']:
                print("NE: ", a['title']['text'], sent['id'], i['id'])
            ne_idx += 1