from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')

db = client.etri_patent_wsd_ne

col = db['Group1']

totalne = 0

for index,a in enumerate(col.find()):
    for sent in a['sentence']:
        mor = []
        for mora in sent['morp']:
            mor.append(mora['lemma'])
        flag = -1
        for aaa in sent['word']:
            if aaa['text'][0] != mor[aaa['begin']][0] and aaa['text'][-1] != mor[aaa['end']][-1]:
                print(index,'\t',a['title']['text'],'\t',aaa['text'], '\t', mor[aaa['begin']], '\t', mor[aaa['end']],'\t',sent['id'],'\t',aaa['id'])
            if (flag + 1) != aaa['begin']:
                print("flag", '\t', aaa['text'], '\t', flag, '\t', aaa['begin'], '\t', aaa['end'], '\t',index,'\t',a['title']['text'], '\t',sent['id'], '\t',aaa['id'])
            flag = aaa['end']