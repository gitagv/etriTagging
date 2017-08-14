# # DB wiki WSD insert
# # create by Kitak Park.
import codecs
import glob
import json
import os
from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_wiki_wsd
original = etri.original
test = etri.test

collection_1 = etri['1-희연']
collection_2 = etri['1-현진']
collection_3 = etri['2-영훈']
collection_4 = etri['2-중식']
collection_5 = etri['3-민숙']
collection_6 = etri['3-지원']
collection_7 = etri['4-덕진']
collection_8 = etri['4-시은']

# 형태소 - 정탁, 개체명 - 기탁
# Group1 = ['0002431_케냐(본문).json', '0002604_칭기즈 칸(본문).json', '0003832_소수 (수론)(본문).json', '0005267_마르틴 루터(본문).json', '0007435_힘 (물리)(본문).json', '0011971_라인 강(본문).json', '0021888_아폴로 계획(본문).json', '0073536_위그노(본문).json']
# 형태소 - 기탁, 개체명 - 태빈
# Group2 = ['0022891_하버드 대학교(본문).json', '0031869_원나라(본문).json', '0034386_시카고 대학교(본문).json', '0038017_엽록체(본문).json', '0038432_제국주의(본문).json']
# 형태소 - 희성, 개체명 - 희성
# Group3 = ['0064865_니콜라 테슬라(본문).json', '0065541_계산 복잡도 이론(본문).json', '0066823_산소(본문).json', '0081200_흑사병(본문).json', '0099396_잭슨빌 (플로리다 주)(본문).json', '0101743_ABC (미국의 방송사)(본문).json', '0116876_노르만인(본문).json', '0137278_기후 변화에 관한 정부간 패널(본문).json']
# 형태소 - 태빈, 개체명 - 정탁
# Group4 = ['0128316_닥터 후(본문).json', '0129301_건설(본문).json', '0129438_증기 기관(본문).json', '0132051_프레즈노(본문).json', '0156720_아마존 우림(본문).json', '0321711_빅토리아 앨버트 박물관(본문).json', '0477729_프렌치 인디언 전쟁(본문).json', '0478195_면역계(본문).json', '0569642_시민 불복종(본문).json', '0787774_스카이 (영국 & 아일랜드)(본문).json', '0791575_남부 캘리포니아(본문).json', '0858744_경제적 불평등(본문).json', '1036011_스코틀랜드 의회(본문).json', '1440966_슈퍼볼 50(본문).json']

Group1 = ['0002431.json', '0002604.json', '0003832.json', '0005267.json', '0007435.json', '0011971.json', '0021888.json', '0073536.json']
Group2 = ['0022891.json', '0031869.json', '0034386.json', '0038017.json', '0038432.json']
Group3 = ['0064865.json', '0065541.json', '0066823.json', '0081200.json', '0099396.json', '0101743.json', '0116876.json', '0137278.json']
Group4 = ['0128316.json', '0129301.json', '0129438.json', '0132051.json', '0156720.json', '0321711.json', '0477729.json', '0478195.json', '0569642.json', '0787774.json', '0791575.json', '0858744.json', '1036011.json', '1440966.json']

# Group1 = ['케냐', '칭기즈 칸', '소수 (수론)', '마르틴 루터', '힘 (물리)', '라인 강', '아폴로 계획', '위그노']
# Group2 = ['하버드 대학교', '원나라', '시카고 대학교', '엽록체', '제국주의']
# Group3 = ['니콜라 테슬라', '계산 복잡도 이론', '산소', '흑사병', '잭슨빌 (플로리다 주)', 'ABC (미국의 방송사)', '노르만인', '기후 변화에 관한 정부간 패널']
# Group4 = ['닥터 후', '건설', '증기 기관', '프레즈노', '아마존 우림', '빅토리아 앨버트 박물관', '프렌치 인디언 전쟁', '면역계', '시민 불복종', '스카이 (영국 & 아일랜드)', '남부 캘리포니아', '경제적 불평등', '스코틀랜드 의회', '슈퍼볼 50']

FILES = glob.glob(os.path.join('./20170609_wiki_756_ne_wsd', '*.json'))

for FILE in FILES:
    f = FILE.split('\\')[1]
    print(f)
    insertT = json.load(codecs.open(FILE, 'r', encoding='utf-8-sig'))

    original.insert(insertT)
    test.insert(insertT)

    if f in Group1:
        collection_1.insert(insertT)
        collection_2.insert(insertT)
    elif f in Group2:
        collection_3.insert(insertT)
        collection_4.insert(insertT)
    elif f in Group3:
        collection_5.insert(insertT)
        collection_6.insert(insertT)
    elif f in Group4:
        collection_7.insert(insertT)
        collection_8.insert(insertT)