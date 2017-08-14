import os

# Group3 = ['20170502-0050000988519.txt.json', '20170526-0230003283202.txt.json', '20170622-0030008026025.txt.json']

list = os.listdir('../20170714_news_300.ucorpus_result/')
for lis in list:
    print('------------------------------------------------------------')
    with open('../20170714_news_300.ucorpus_result/' + lis, "r", encoding='utf-8') as f:
        print(lis)
        # if lis.split('_')[1].split('(본문)')[0] == '20170112-0010008954105.txt.ucorpus':
        if lis == '20170526-0230003283202.txt.ucorpus':
            texts = f.read()
            temp1 = []
            temp2 = []
            cur = 1
            for n, text in enumerate(texts.split('\n')):
                for eojeol in text.split(' '):
                    if cur % 3 == 1:
                        print(int(n/3))
                        temp1.append(eojeol)
                    if cur % 3 == 2:
                        temp2.append(eojeol)
                if cur % 3 == 0:

                    for i in range(0, temp1.__len__()):
                        print("%s\t\t%s" % (temp1[i], temp2[i]))
                    print('\n\n')
                    temp1 = []
                    temp2 = []
                cur += 1

            break
