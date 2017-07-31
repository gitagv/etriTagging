import glob
import os

FILES = glob.glob(os.path.join('./20170609_wiki_756.ucorpus', '*.json.ucorpus'))

for FILE in FILES:
    word = {}
    f = open(FILE, 'r' ,encoding='utf-8').read()
    word['sentence'] = [(s.split('\n')[0], s.split('\n')[1]) for s in f.split('\n\n') if s.strip() != '']

    print(word)
    # for n in word['sentence']:
    #     print(n)

    # for c in word['sentence']:
    #     print(c)
    #     break
    # [s.split(' ') for s in word['sentence'].split('\n')[1]]
    # print(word)
    break