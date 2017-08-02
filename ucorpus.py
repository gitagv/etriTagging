from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.46')
db = client.etri_wiki
submit_collection = db.submit

for obj in submit_collection.find():

    # if obj['title']['text'] == '케냐':
        print("------title : %s------\n" % obj['title']['text'])
        for sen in obj['sentence']:

            # if sen['id'] == 5:
                eojeol_arr = [e for e in sen['text'].split(' ') if e.strip() != '']
                print("sentence id : %s, sentence : %s" % (sen['id'], sen['text']))
                print("eojeol_arr : %s" % eojeol_arr)
                morp_arr = {}
                eojeol_index = []
                result = []
                endNum = len(sen['morp'])

                for morp in sen['morp']:
                    morp_arr[morp['id']] = morp['lemma']
                # print(morp_arr)

                passN = 0
                startNum = 0
                for eojeol in eojeol_arr:
                    # print(eojeol)
                    for n in range(startNum, endNum):
                        if morp_arr[n] != '-':
                            # print(morp_arr)
                            if len(eojeol) == 1:
                                if morp_arr[n] != '-' and len(morp_arr[n]) == 1:
                                    eojeol_index.append(n)
                                    morp_arr[n] = '-'
                                    startNum = n+1
                                    for a in range(0, n - 1):
                                        morp_arr[a] = '-'
                                    break

                            if len(eojeol) == len(morp_arr[n]):
                                if eojeol == morp_arr[n]:
                                    eojeol_index.append(n)
                                    morp_arr[n] = '-'
                                    startNum = n + 1
                                    for a in range(0, n - 1):
                                        morp_arr[a] = '-'
                                    break
                                elif eojeol[0] == morp_arr[n][0]:
                                    eojeol_index.append(n)
                                    morp_arr[n] = '-'
                                    startNum = n + 1
                                    for a in range(0, n - 1):
                                        morp_arr[a] = '-'
                                    break
                            else:
                                if eojeol[0] == morp_arr[n][0]:
                                    eojeol_index.append(n)
                                    morp_arr[n] = '-'
                                    startNum = n + 1
                                    for a in range(0, n - 1):
                                        morp_arr[a] = '-'
                                    break

                eojeol_index.append(endNum)

                print(eojeol_index)
                print("\n")
