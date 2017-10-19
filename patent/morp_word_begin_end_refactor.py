# # morp _ word _ begin _end
# # create by Kitak Park.
from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_patent_morp
test = etri['Group1']

################ 여기만 수정 , 하고 추가 ########
fixedArr = [
'1020010036478.json_2_29_-1'
]
##################################################

for n, f in enumerate(fixedArr):
    # 문서 이름
    documentName = f.split('_')[0]
    # 문장 번호
    sentenceN = int(f.split('_')[1])
    # word 수정 시작 인덱스
    wordN = int(f.split('_')[2])
    # 비긴 엔드 증감 1 or -1
    begin_end = int(f.split('_')[3])

    print(documentName, sentenceN, wordN, begin_end)

    # 결합이던 분리던 해당 인덱스의 begin은 안 변하고 end만 변하며
    # 다음 인덱스부터 begin, end가 수정됨
    for t in test.find():
        if documentName == t['title']['text']:
            for sentence in t['sentence']:
                if sentence['id'] == sentenceN:
                    for word in sentence['word']:
                        # print(word['begin'],word['end'])
                        if word['id'] == wordN:
                            word.update({'end': word['end'] + begin_end})
                            test.save(t)
                        elif word['id'] > wordN:
                            word.update({'begin':word['begin'] + begin_end})
                            word.update({'end': word['end'] + begin_end})
                            test.save(t)
                        else:
                            pass
                        # print(word['begin'], word['end'])
                        # print('\n')


