from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')

db = client.etri_patent_wsd_ne

col = db['Group1']

totalne = 0

for a in col.find():
    for sent in a['sentence']:
        morp = []
        for i in sent['morp']:
            morp.append(i['lemma'])
        for i in sent['NE']:
            if i['text'][0] == morp[i['begin']][0] and i['text'][-1] == morp[i['end']][-1]:
                pass
            else:
                print(a['title']['text'], '\t ', sent['id'], '\t', i['id'], '\t', i['text'], '\t', morp[i['begin']],
                      '\t', morp[i['end']], '\t', i['begin'], '\t', i['end'])
                # print(i['text'][0],'\t',morp[i['begin']][0],'\t',i['text'][-1],'\t',morp[i['end']][-1])