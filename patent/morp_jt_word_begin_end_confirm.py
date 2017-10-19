from pymongo import MongoClient

connection = MongoClient('mongodb://root:nlp44342@203.255.81.71')

etri = connection.etri_patent_morp
test = etri['Group1']
# doc = ['1020020053700.json', '1020100120827.json', '1020110025339.json', '1020110050673.json', '1020110104047.json',
#        '1020120127894.json', '1020120030889.json', '1020120087002.json', '1020080010234.json']#4
# doc = ['1020120144532.json', '1020130021737.json', '1020130053682.json', '1020140137731.json', '1020150042306.json',
#        '1020050015959.json', '2020130001049.json', '1020120115740.json', '1020110138719.json']#3
# doc = ['1020040056582.json', '1020040056584.json', '1020040056638.json', '1020040078406.json', '2020070018478.json',
#        '1020050019814.json', '1020050064310.json', '1020090051233.json', '1020080019940.json', '1020080020188.json']#2
doc = {'1020000022266.json', '1020000083784.json', '1020010036478.json', '1020010054421.json', '1020010080185.json',
       '1020010087411.json', '1020020018004.json', '1020020084454.json', '1020030028272.json', '1020030056364.json'}  #1
# doc = {'1020000022266.json'}
for t in test.find():
    for ttt in doc:
        if ttt == t['title']['text']:
            for sentence in t['sentence']:
                mor = []
                for morp in sentence['morp']:
                    mor.append(morp['lemma'])
                for word in sentence['word']:
                    if word['text'][0] != mor[int(word['begin'])][0]:
                        print('=============================================================================')
                        print(ttt, '\t', sentence['id'], '\t', word['id'])
                        print(word['begin'], '\t', word['text'], '\t', mor[int(word['begin'])],
                              mor[int(word['begin']) + 1])