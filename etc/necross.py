from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')

db = client.etri_ne

namelist = [0, '현진', '희연', '영훈', '중식', '민숙', '지원',  '덕진', '시은']
GROUP = 1
name1 = str(GROUP) + '-' + namelist[GROUP * 2 - 1]
name2 = str(GROUP) + '-' + namelist[GROUP * 2]

collection1 = db[name1]
collection2 = db[name2]
# original_collection = db['original4']

for obj_1,obj_2 in zip(collection1.find(),collection2.find()):
    print(obj_1['title']['text'],'\n')
    sen = 0
    for val_1,val_2 in zip(obj_1['sentence'],obj_2['sentence']):
        print(namelist[GROUP * 2 - 1],end='\t')
        for tag_1 in val_1['NE']:
            print(tag_1['text'],' ',tag_1['type'],end='      ')
        print()
        print(namelist[GROUP * 2], end='\t')
        for tag_2 in val_2['NE']:
            print(tag_2['text'],' ',tag_2['type'],end='      ')
        print()
        print()
    # break