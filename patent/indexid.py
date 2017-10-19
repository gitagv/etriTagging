from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')
# etri = client.etri_patent_morp
etri = client.etri_patent_wsd_ne
submit = etri['Group1']

for s in submit.find():
    for sentence in s['sentence']:
        # for id, morp in enumerate(sentence['morp']):
        #     if morp['id'] != id:
        #         print(s['title']['text'], sentence['id'], morp['id'])
        # for id, word in enumerate(sentence['word']):
        #     if word['id'] != id:
        #         print(s['title']['text'], sentence['id'], word['id'])
        for id, wsd in enumerate(sentence['wsd']):
            if wsd['id'] != id:
                print(s['title']['text'], sentence['id'], wsd['id'])
        for id, ne in enumerate(sentence['ne']):
            if ne['id'] != id:
                print(s['title']['text'], sentence['id'], ne['id'])
