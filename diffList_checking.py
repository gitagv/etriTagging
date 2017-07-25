from pymongo import MongoClient

client = MongoClient('mongodb://203.255.81.71:27017')

db = client.etri
submit_collection = db['submit']

Group1 = ['케냐', '칭기즈 칸', '소수 (수론)', '마르틴 루터', '힘 (물리)', '라인 강', '아폴로 계획', '위그노']
Group2 = ['하버드 대학교', '원나라', '시카고 대학교', '엽록체', '제국주의']
Group3 = ['니콜라 테슬라', '계산 복잡도 이론', '산소', '흑사병', '잭슨빌 (플로리다 주)', 'ABC (미국의 방송사)', '노르만인', '기후 변화에 관한 정부간 패널']
Group4 = ['닥터 후', '건설', '증기 기관', '프레즈노', '아마존 우림', '빅토리아 앨버트 박물관', '프렌치 인디언 전쟁', '면역계', '시민 불복종', '스카이 (영국 & 아일랜드)', '남부 캘리포니아', '경제적 불평등', '스코틀랜드 의회', '슈퍼볼 50']

Group = Group2

updateDat = []
FILE = open('./result/crosschecking_update.txt' , 'r', encoding='utf-8').read().split('\n')

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