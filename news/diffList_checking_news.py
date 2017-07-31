from pymongo import MongoClient

# client = MongoClient('mongodb://203.255.81.46:27017')
client = MongoClient('mongodb://root:nlp44342@203.255.81.71')

db = client.etri_news
submit_collection = db['submit']

Group1 = ['file01', 'file03', 'file05']
Group1_id = ['59789454e908906ac86ba79f', '59789456e908906ac86ba7a1', '59789457e908906ac86ba7a3']
# Group1_Ob_id = ['ObjectId("59789454e908906ac86ba79f")', 'ObjectId("59789456e908906ac86ba7a1")', 'ObjectId("59789457e908906ac86ba7a3")']
# Group2 = ['file08', 'file10', 'file11']
# Group3 = ['file04', 'file07', 'file12']
# Group4 = ['file02', 'file06', 'file09']

Group = Group1_id

updateDat = []

FILE = open('./crosschecking_update1.txt' , 'r', encoding='utf-8').read().split('\n')

for Gid in Group1_id:
    for s in submit_collection.find():
        if Gid == str(s['_id']):
            for f in FILE:
                Gindex = Group1_id.index(str(s['_id']))
                title = f.split('  ')[0]
                id = f.split('  ')[1]
                senNum = int(f.split('  ')[2])
                morpNum = int(f.split('  ')[3])
                morpType = f.split('  ')[4]

                if title == Group1[Gindex]:
                    print(s['sentence'][senNum]['morp'][morpNum])
                    s['sentence'][senNum]['morp'][morpNum].update({'type':morpType})
                    submit_collection.save(s)