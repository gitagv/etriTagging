from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')

db = client.etri_wiki_wsd

original_collection = db['original1']

namelist = [0, '현진', '희연', '영훈', '중식', '민숙', '지원',  '덕진', '시은']
GROUP = 1
name1 = str(GROUP) + '-' + namelist[GROUP * 2 - 1]
name2 = str(GROUP) + '-' + namelist[GROUP * 2]

collection1 = db[name1]
collection2 = db[name2]
# original_collection = db['original4']

count = 0
eojulCount = 0
sameTagTotal = 0   #둘이 같게 태깅한 형태소 개수
sameDiffTotal = 0   # 같게 태깅했는데 원본과 태그가 다른 형태소 개수
sameTotal = 0

diffList = []               #서로 다르게 태깅한 [문서, 문장번호, 형태소번호] 집합
sameDiffList = []           #서로 같게 태깅했지만 원본과 다른 형태소의 [문서, 문장번호, 형태소번호] 집합
remove_division_list = []       #결합, 분리 된 형태소 리스트([문서, 문장번호, 형태소 번호] 로 구성)

flag = True
for obj_1, obj_2, obj_3 in zip(collection1.find(), collection2.find(), original_collection.find()):   # 컬렉션 1,2  3,4  5,6 이런식으로 바꿀 것
    for val_1, val_2, val_3 in zip(obj_1['sentence'], obj_2['sentence'], obj_3['sentence']):

        for tag_1, tag_2, tag_3 in zip(val_1['WSD'], val_2['WSD'], val_3['WSD']):

            eojulCount += 1
            if(tag_1['scode'] != tag_2['scode']):
                count += 1
                diffList.append(obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']) + '  ' + tag_1['scode'] + '  ' + tag_2['scode'])

            else:
                sameTagTotal += 1
                if tag_1['scode'] != tag_3['scode']:
                    sameDiffTotal += 1
                    sameDiffList.append(obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']) + '  ' + tag_1['scode'])


print("진행 형태소 개수: {}, 서로 다르게 태깅한 형태소 개수: {}, 오류율: {}".format(eojulCount, count, (count*100)/eojulCount))
print("\n\n")

with open("./wiki_wsd_result/diffList_each.txt", "w", encoding='utf-8') as f:
    for diff in diffList:
        f.write("%s\n" % str(diff))

with open("./wiki_wsd_result/diffList_original.txt", "w", encoding='utf-8') as f:
    for diff_ in sameDiffList:
        f.write(str(diff_))
        f.write("\n")