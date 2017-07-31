from pymongo import MongoClient

client = MongoClient('mongodb://203.255.81.71:27017')

db = client.etri
original_collection = db['original']
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

# 그룹명 , 이름, 컬렉션, 타이틀, 문장 번호 수정

Group = Group4
data1 = collection_7
data2 = collection_8
title = '닥터 후'
senid = 15

count = 0
eojulCount = 0
sameTagTotal = 0   #둘이 같게 태깅한 형태소 개수
sameDiffTotal = 0   # 같게 태깅했는데 원본과 태그가 다른 형태소 개수
sameTotal = 0

diffList = []               #서로 다르게 태깅한 [문서, 문장번호, 형태소번호] 집합
sameDiffList = []           #서로 같게 태깅했지만 원본과 다른 형태소의 [문서, 문장번호, 형태소번호] 집합
remove_division_list = []       #결합, 분리 된 형태소 리스트([문서, 문장번호, 형태소 번호] 로 구성)
# diff_list1 = []
# diff_list2 = []
flag = True
for l in Group:
    for obj_1, obj_2, obj_3 in zip(data1.find(), data2.find(), original_collection.find()):   # 컬렉션 1,2  3,4  5,6 이런식으로 바꿀 것
        if l == obj_1['title']['text']:
            for val_1, val_2, val_3 in zip(obj_1['sentence'], obj_2['sentence'], obj_3['sentence']):
                # if title == obj_1['title']['text'] and val_1['id'] == senid:
                #     flag = False
                #     break

                for tag_1, tag_2, tag_3 in zip(val_1['morp'], val_2['morp'], val_3['morp']):
                    if 'remove' in tag_1:
                        if not (tag_1['remove'] == None and tag_1['division'] == None):
                            remove_division_list.append(obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']))
                        if 'remove' in tag_2:
                            if not (tag_2['remove'] == None and tag_2['division'] == None):
                                if [obj_2['title']['text'], val_2['id'], tag_2['id']] not in remove_division_list:
                                    remove_division_list.append(obj_2['title']['text'] + '  ' + str(val_2['id'])+ '  ' + str(tag_2['id']))

                    eojulCount += 1
                    if(tag_1['type'] != tag_2['type']):
                        count += 1
                        diffList.append(obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']) + '  ' + tag_1[
                                'type'] + '  ' + tag_2['type'])
                        # diff_list1.append(
                        #     obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']) + '  ' + tag_1[
                        #         'type'])
                        # diff_list2.append(
                        #     obj_2['title']['text'] + '  ' + str(val_2['id']) + '  ' + str(tag_2['id']) + '  ' + tag_2[
                        #         'type'])
                        # print("문서: {}".format(obj_1['title']['text']))
                        # print("문장번호: {}".format(val_1['id']))
                        # print("문장: {}".format(val_1['text']))
                        # print("단어번호: {}".format(tag_1['id']))
                        # print("단어: {}".format(tag_1['lemma']))
                        # print("{} - {}: {}, {}: {}".format(GroupName, name1, tag_1['type'], name2, tag_2['type']))    # 컬렉션 바뀌면 이름 변경할 것
                        # print("\n")
                    else:
                        sameTagTotal += 1
                        if tag_1['type'] != tag_3['type']:
                            sameDiffTotal += 1
                            sameDiffList.append(obj_1['title']['text'] + '  ' + str(val_1['id']) + '  ' + str(tag_1['id']) + '  ' + tag_1['type'] + '  ' + tag_3['type'])
                        # else:
                        #     sameTotal += 1
                        #     print("========== 원본과 같게 태깅된 것들==============")
                        #     print("문서: {}".format(obj_1['sentence'][0]['text']))
                        #     print("문장번호: {}".format(val_1['id']))
                        #     print("단어번호: {}".format(tag_1['id']))
                        #     print("=======================================\n\n")


        if flag == False:
            break

print("진행 형태소 개수: {}, 서로 다르게 태깅한 형태소 개수: {}, 오류율: {}".format(eojulCount, count, (count*100)/eojulCount))
print("\n\n")
with open("samediffList.txt", "w", encoding='utf-8') as f:
    for difff in sameDiffList:
        f.write("%s\n" % difff)
with open("crosschecking_update.txt", "w", encoding='utf-8') as f:
    for difff in sameDiffList:
        f.write("%s\n" % difff)
    for diff in diffList:
        f.write("%s\n" % diff)
with open("diffList.txt", "w", encoding='utf-8') as f:
    # f.write("----------서로 다르게 태깅된 형태소 리스트----------------\n")
    # f.write("[문서, 문장번호, 형태소번호, 학생1태그, 학생2태그] 의 형식\n\n\n")
    for diff in diffList:
        f.write("%s\n" % diff)
    # f.write("----------서로 다르게 태깅된 형태소 리스트----------------\n")
    # f.write("[문서, 문장번호, 형태소번호, 학생1태그, 학생2태그] 의 형식\n\n\n")

    # f.write("\n")
    # f.write("----------같게 태깅했지만 원문과 다르게 태깅된 형태소 리스트----------------\n")
    # f.write("[문서, 문장번호, 형태소번호, 수동태그, 원본태그] 의 형식\n\n\n")
    # for diff_ in sameDiffList:
    #     f.write(str(diff_))
    #     f.write("\n")
    # 결합, 분리 태깅된 형태소 결과 출력
    # f.write("\n")
    # f.write("----------remove, division 태깅된 형태소 리스트-----------\n\n")
    # for sub_lst in remove_division_list:
    #     f.write(str(sub_lst))
    #     f.write("\n")
    # f.write("\n")
    # f.write("결합,분리 총 개수: {}".format(len(remove_division_list)))
    # f.write("\n")

    # f.write("같게 태깅된 개수: {}".format(sameTagTotal))
    # f.write("\n")
    # f.write("같게 태깅 됐는데 원본과 다르게 태깅된 개수: {}".format(sameDiffTotal))
    # f.write("\n")
    # f.write("원본이랑 다른 비율: {}".format((sameDiffTotal*100)/sameTagTotal))
    # f.write("\n")
with open('remove_division.txt', 'w', encoding='utf-8') as f:
    for sub_lst in remove_division_list:
        f.write("%s\n" % sub_lst)
# with open("./result/result1.txt", "w", encoding='utf-8') as f:
#     for r1 in diff_list1:
#         f.write("%s\n" % r1)
# with open("./result/result2.txt", "w", encoding='utf-8') as f:
#     for r2 in diff_list2:
#         f.write("%s\n" % r2)
# with open("./result/crossChecking.txt", "w", encoding='utf-8') as f:
#     for r2 in diff_list2:
#         f.write("%s\n" % r2)
# 총 형태소 개수 출력
# total = 0
# for i in collection.find():
#     eojCnt = 0
#     senCnt = 0
#     for val in i['sentence']:
#         senCnt += 1
#         for eojul_val in val['morp']:
#
#             eojCnt += 1
#             total += 1
#     # print("단어 : %s, 문장 수: %s, 어절 수: %s  총 어절 수: %s" % (i['title']['text'], senCnt, eojCnt ,coutn))
# print("total: {}".format(total))
