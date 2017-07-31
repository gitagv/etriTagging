from pymongo import MongoClient

client = MongoClient('mongodb://203.255.81.71:27017')

db = client.etri
original_collection = db['original']
submit_collection = db['submit']
collection = db['7-실험용']
collection_1 = db['1-민숙']
collection_2 = db['1-희연']
collection_3 = db['2-덕진']
collection_4 = db['2-영훈']
collection_5 = db['3-중식']
collection_6 = db['3-지원']
collection_7 = db['4-시은']
collection_8 = db['4-현진']

Group1 = ['케냐', '칭기즈 칸', '소수 (수론)', '마르틴 루터', '힘 (물리)', '라인 강', '아폴로 계획', '위그노']
Group2 = ['하버드 대학교', '원나라', '시카고 대학교', '엽록체', '제국주의']
Group3 = ['니콜라 테슬라', '계산 복잡도 이론', '산소', '흑사병', '잭슨빌 (플로리다 주)', 'ABC (미국의 방송사)', '노르만인', '기후 변화에 관한 정부간 패널']
Group4 = ['닥터 후', '건설', '증기 기관', '프레즈노', '아마존 우림', '빅토리아 앨버트 박물관', '프렌치 인디언 전쟁', '면역계', '시민 불복종', '스카이 (영국 & 아일랜드)', '남부 캘리포니아', '경제적 불평등', '스코틀랜드 의회', '슈퍼볼 50']

Group = Group4
data1 = collection_7
data2 = collection_8

updateDat = []
FILE = open('crosschecking_update.txt' , 'r', encoding='utf-8').read().split('\n')
# for f in FILE:
#     title = f.split('  ')[0]
#     senNum = f.split('  ')[1]
#     morpNum = f.split('  ')[2]
#     morpType = f.split('  ')[3]
#     updateDat.append()

# print(updateDat)

for l in Group:
    for s in submit_collection.find():
        if l == s['title']['text']:
            for f in FILE:
                title = f.split('  ')[0]
                senNum = int(f.split('  ')[1])
                morpNum = int(f.split('  ')[2])
                morpType = f.split('  ')[3]

                if title ==  s['title']['text']:
                    s['sentence'][senNum]['morp'][morpNum].update({'type':morpType})
                    submit_collection.save(s)

#
# with open("updateMorph.txt", "r", encoding='utf-8') as f:
#     text = f.readlines()
# for lines in text:
#     lines = lines.strip('[')
#     lines = lines.strip(']')
#     lines = lines.strip('\'')
#     print(lines)
#     # print(lines[0], lines[1], lines[2], lines[3])
# #
# # for l in Group:
# #     for obj_1, obj_2, obj_3 in zip(data1.find(), data2.find(), original_collection.find()):   # 컬렉션 1,2  3,4  5,6 이런식으로 바꿀 것
# #         if l == obj_1['title']['text']:
# #             for val_1, val_2, val_3 in zip(obj_1['sentence'], obj_2['sentence'], obj_3['sentence']):
# #                 for tag_1, tag_2, tag_3 in zip(val_1['morp'], val_2['morp'], val_3['morp']):
#
#                     # for lines in text:
#                     #     if(lines[0]==obj_1['title']['text'] and lines[1]==val_1['id'] and lines[2] == tag_1['id']):
#                     #         print(lines)
#
#
