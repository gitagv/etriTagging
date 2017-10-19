# # morp _ word _ begin _end _ confirm
# # create by Kitak Park.
from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_patent_morp
test = etri['Group4']

for t in test.find():
    for sentence in t['sentence']:
        # if sentence['word'][0]['begin'] == 0:
        #     pass
        # else:
        #     print(t['title']['text'], sentence['id'])
        #     pass

        wordLen = len(sentence['word']) - 1
        morpLen = len(sentence['morp']) - 1
        if sentence['word'][wordLen]['end'] == sentence['morp'][morpLen]['id']:
            pass
        else:
            print("문서 : %s , 문장 번호 : %s, word 끝 index의 end 값 : %s, 형태소 끝 index : %s" % (t['title']['text'], sentence['id'], sentence['word'][wordLen]['end'], sentence['morp'][morpLen]['id']))
            pass


