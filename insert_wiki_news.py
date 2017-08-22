# # DB insert
# # create by Kitak Park.
import codecs
import glob
import json
import os
from pymongo import MongoClient

# connection = MongoClient('mongodb://root:nlp44342@203.255.81.46')
# connection = MongoClient('mongodb://myUserAdmin:abc123@203.255.81.70')
connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_news
# original = etri.original
# submit = etri.submit
# test = etri.test

# collection_1 = etri['1-희연']
# collection_2 = etri['1-현진']
# collection_3 = etri['2-영훈']
# collection_4 = etri['2-중식']
# collection_5 = etri['3-민숙']
# collection_6 = etri['3-지원']
# collection_7 = etri['4-덕진']
# collection_8 = etri['4-시은']

# Group1 = ['케냐', '칭기즈 칸', '소수 (수론)', '마르틴 루터', '힘 (물리)', '라인 강', '아폴로 계획', '위그노']
# Group2 = ['하버드 대학교', '원나라', '시카고 대학교', '엽록체', '제국주의']
# Group3 = ['니콜라 테슬라', '계산 복잡도 이론', '산소', '흑사병', '잭슨빌 (플로리다 주)', 'ABC (미국의 방송사)', '노르만인', '기후 변화에 관한 정부간 패널']
# Group4 = ['닥터 후', '건설', '증기 기관', '프레즈노', '아마존 우림', '빅토리아 앨버트 박물관', '프렌치 인디언 전쟁', '면역계', '시민 불복종', '스카이 (영국 & 아일랜드)', '남부 캘리포니아', '경제적 불평등', '스코틀랜드 의회', '슈퍼볼 50']

# Group1 = ['20170112-0010008954105.txt', '20170319-0010009118371.txt', '20170521-4210002742987.txt']
# Group2 = ['20170527-0230003283619.txt', '20170609-0230003287020.txt', '20170613-0010009332942.txt']
# Group3 = ['20170502-0050000988519.txt', '20170526-0230003283202.txt', '20170622-0030008026025.txt']
# Group4 = ['20170120-0250002678055.txt', '20170522-4210002744977.txt', '20170608-0010009321581.txt']

# FILES = glob.glob(os.path.join('./test_json', '*.json'))
# FILES = glob.glob(os.path.join('./170609_1차태깅문서_위키(35문서_756문장)', '*.json'))
# FILES = glob.glob(os.path.join('./20170714_news_300_title', '*.txt'))
FILES = glob.glob(os.path.join('./20170801_legal_2179', '*.json'))

for FILE in FILES:
    f = FILE.split('\\')[1]
    # print(f.split('-')[0])
    # print(f.split('_')[1].split('(본문)')[0])
    # f = f.split('_')[1].split('(본문)')[0]
    insertT = json.load(codecs.open(FILE, 'r', encoding='utf-8-sig'))

    # original.insert(insertT)
    test.insert(insertT)
    # submit.insert(insertT)
    # if f in Group1:
    #     collection_1.insert(insertT)
    #     collection_2.insert(insertT)
    # elif f in Group2:
    #     collection_3.insert(insertT)
    #     collection_4.insert(insertT)
    # elif f in Group3:
    #     collection_5.insert(insertT)
    #     collection_6.insert(insertT)
    # elif f in Group4:
    #     collection_7.insert(insertT)
    #     collection_8.insert(insertT)