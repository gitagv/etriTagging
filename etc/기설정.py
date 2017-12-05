from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')

db = client.etri_patent_wsd_ne

col = db['Group4']


for obj in col.find():
    for val in obj['sentence']:
        if '기설정' in val['text']:
            print(obj['title']['text'], val['id'])