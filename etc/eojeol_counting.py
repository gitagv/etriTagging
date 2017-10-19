# # morp count
# # create by Kitak Park.
from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_legal_WSD_NE
original = etri.original
etri = connection.etri
documents = etri.documents

Group1 = ['케냐', '칭기즈 칸', '소수 (수론)', '마르틴 루터', '힘 (물리)', '라인 강', '아폴로 계획', '위그노']
Group2 = ['하버드 대학교', '원나라', '시카고 대학교', '엽록체', '제국주의']
Group3 = ['니콜라 테슬라', '계산 복잡도 이론', '산소', '흑사병', '잭슨빌 (플로리다 주)', 'ABC (미국의 방송사)', '노르만인', '기후변화에 관한 정부간 패널']
Group4 = ['닥터 후', '건설', '증기 기관', '프레즈노', '아마존 우림', '빅토리아 앨버트 박물관', '프렌치 인디언 전쟁', '면역계', '시민 불복종', '스카이 (영국 & 아일랜드)', '남부 캘리포니아', '경제적 불평등', '스코틀랜드 의회', '슈퍼볼 50']

documentN = 0
sentenceN = 0
morphN = 0
wsdN =0
neN = 0
for d in documents.find():
    if d['title']['text'] in Group2:
        tag = True
        print(d['title']['text'])
        documentN += 1
        for sentence in d['sentence']:
            # if d['title']['text'] == '힘 (물리)' and sentence['id'] == 1:
            if d['title']['text'] == '시카고 대학교' and sentence['id'] == 21:
                tag = False
                break
            else:
                tag = True
                sentenceN += 1
                for morp in sentence['morp']:
                    morphN += 1
                # for WSD in sentence['WSD']:
                #     wsdN += 1
                # for NE in sentence['NE']:
                #     neN += 1
        if tag == False:
            break

print(documentN,sentenceN,morphN, wsdN, neN, morphN + wsdN + neN)