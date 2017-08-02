import glob
import os

from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.71')
db = client.etri_news
submit_collection = db.submit

FILEpath = glob.glob(os.path.join('../20170714_news_300.ucorpus', '*.ucorpus'))
# print(FILEpath)
FILES = [f.rsplit('\\')[1] for f in FILEpath]
# print(FILES)

for obj in submit_collection.find():
    path = '../20170714_news_300.ucorpus_result/' + obj['title']['text']
    with open(path, "w", encoding="utf-8") as f:
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
