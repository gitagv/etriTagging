from pymongo import MongoClient

client = MongoClient('mongodb://203.255.81.71:27017')

db = client.etri
original_collection = db['original']
collection = db['7-실험용']

collection_3 = db['2-덕진']
collection_4 = db['2-영훈']

Group2 = ['하버드 대학교', '원나라', '시카고 대학교', '엽록체', '제국주의']

# 그룹명 , 이름, 컬렉션, 타이틀, 문장 번호 수정

Group = Group2
data1 = collection_3
data2 = collection_4
# title = '닥터 후'
# senid = 15

count = 0
eojulCount = 0
sameTagTotal = 0   #둘이 같게 태깅한 형태소 개수
sameDiffTotal = 0   # 같게 태깅했는데 원본과 태그가 다른 형태소 개수
sameTotal = 0

diffList = []               #서로 다르게 태깅한 [문서, 문장번호, 형태소번호] 집합
sameDiffList = []           #서로 같게 태깅했지만 원본과 다른 형태소의 [문서, 문장번호, 형태소번호] 집합
remove_division_list = []       #결합, 분리 된 형태소 리스트([문서, 문장번호, 형태소 번호] 로 구성)

flag = True
for l in Group:
    for obj_1, obj_2, obj_3 in zip(data1.find(), data2.find(), original_collection.find()):   # 컬렉션 1,2  3,4  5,6 이런식으로 바꿀 것
        if l == obj_1['title']['text']:
            for val_1, val_2, val_3 in zip(obj_1['sentence'], obj_2['sentence'], obj_3['sentence']):

                for tag_1, tag_2, tag_3 in zip(val_1['morp'], val_2['morp'], val_3['morp']):
                    if 'remove' in tag_1:
                        if not (tag_1['remove'] == None and tag_1['division'] == None):
                            remove_division_list.append(obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']))
                        if 'remove' in tag_2:
                            if not (tag_2['remove'] == None and tag_2['division'] == None):
                                if [obj_2['title']['text'], val_2['id'], tag_2['id']] not in remove_division_list:
                                    remove_division_list.append(obj_2['title']['text'] + '  ' + str(val_2['id']) + '  ' + str(tag_2['id']))
                    eojulCount += 1
                    if(tag_1['type'] != tag_2['type']):
                        count += 1
                        diffList.append(obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']) + '  ' + tag_1['type'] + '  ' + tag_2['type'])

                    else:
                        sameTagTotal += 1
                        if tag_1['type'] != tag_3['type']:
                            sameDiffTotal += 1
                            sameDiffList.append(obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']) + '  ' + tag_1['type'] + '  ' + tag_3['type'])

        if flag == False:
            break

print("진행 형태소 개수: {}, 서로 다르게 태깅한 형태소 개수: {}, 오류율: {}".format(eojulCount, count, (count*100)/eojulCount))
print("\n\n")

with open("./result/diffList_each.txt", "w", encoding='utf-8') as f:
    for diff in diffList:
        f.write("%s\n" % str(diff))

with open("./result/diffList_original.txt", "w", encoding='utf-8') as f:
    for diff_ in sameDiffList:
        f.write(str(diff_))
        f.write("\n")

with open("./result/remove_division_list.txt", "w", encoding='utf-8') as f:
    for sub_lst in remove_division_list:
        f.write(str(sub_lst))
        f.write("\n")