import glob
import os

from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.46')
db = client.etri_wiki
submit_collection = db.submit

FILEpath = glob.glob(os.path.join('../20170609_wiki_756.ucorpus', '*.ucorpus'))
# print(FILEpath)
FILES = [f.rsplit('\\')[1] for f in FILEpath]
# print(FILES)
FILENAME = ['케냐', '칭기즈 칸', '소수 (수론)', '마르틴 루터', '힘 (물리)', '라인 강',
            '아폴로 계획', '하버드 대학교', '원나라', '시카고 대학교', '엽록체', '제국주의', '니콜라 테슬라',
            '계산 복잡도 이론', '산소', '위그노', '흑사병',
            '잭슨빌 (플로리다 주)', 'ABC (미국의 방송사)', '노르만인', '닥터 후', '건설', '증기 기관',
            '프레즈노', '기후 변화에 관한 정부간 패널', '아마존 우림', '빅토리아 앨버트 박물관',
            '프렌치 인디언 전쟁', '면역계', '시민 불복종', '스카이 (영국 & 아일랜드)', '남부 캘리포니아', '경제적 불평등', '스코틀랜드 의회', '슈퍼볼 50']

# FILES = [glob.glob(os.path.join('./20170714_news_300', '*.txt'))]

for obj in submit_collection.find():
    with open('./20170609_wiki_756.ucorpus_result/'+FILES[FILENAME.index(obj['title']['text'])], "w", encoding="utf-8") as f:
        for sen in obj['sentence']:
            eojeol_arr = [e for e in sen['text'].split(' ') if e.strip() != '']
            morp_arr = {}
            eojeol_index = []
            eojeol_cnt = eojeol_arr.__len__()
            endNum = len(sen['morp'])
            cur = 0
            for morp in sen['morp']:
                morp_arr[morp['id']] = morp['lemma']
            sentempid = 0
            sentemp = ''
            for i in range(0, endNum):
                if sentemp != eojeol_arr[cur]:
                    if sentemp == '':
                        sentempid = i
                    if cur + 1 < eojeol_cnt and eojeol_arr[cur + 1][0] == morp_arr[i][0] and sentemp != '':
                        eojeol_index.append(sentempid)
                        cur += 1
                        sentemp = ''
                        sentempid = i
                    sentemp += morp_arr[i]
                if sentemp == eojeol_arr[cur]:
                    eojeol_index.append(sentempid)
                    cur += 1
                    sentemp = ''
                if cur == eojeol_cnt:
                    break
                elif endNum == i + 1 and sentemp != '':
                    eojeol_index.append(sentempid)

            eojeol_index.append(endNum)
            print(eojeol_index)
            print("\n")

            f.write(sen['text'])
            f.write("\n")
            result_string = ''
            for idx in range(0, endNum):
                if idx == 0:
                    result_string += sen['morp'][idx]['lemma'] + '/' + sen['morp'][idx]['type']
                    continue
                if idx == endNum-1:
                    result_string = result_string + '+' + sen['morp'][idx]['lemma'] + '/' + sen['morp'][idx]['type']
                    continue

                if idx != 0 and idx in eojeol_index:
                    result_string += ' ' + sen['morp'][idx]['lemma'] + '/' + sen['morp'][idx]['type']
                else:
                    result_string += '+' + sen['morp'][idx]['lemma'] + '/' + sen['morp'][idx]['type']

            f.write(result_string)
            f.write("\n\n")
