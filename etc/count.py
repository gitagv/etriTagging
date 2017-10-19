import os

filelist = os.listdir("../20170801_legal_2179_morp/")
total = 0
ttt = 0
for i in filelist:
    with open("../20170801_legal_2179_morp/" + i, "r",
              encoding='utf-8') as f:
        count = 0
        idcount = 0
        filecount = 0
        texts = f.read()
        flag = True
        cccc = 0
        for line in texts.split('\n'):
            if line[:7] == '	"id" :':
                if line[8:-1] == '139':
                    break
                idcount += 1
                count = 0
            if line == '	"WSD" : [':
                flag = False
            elif flag == False and line == '	],':
                flag = True
                filecount += count
                # print(count)
            elif flag == False:
                # for li in line.split(','):
                #     if li[:10] == '		{"id" : ':
                #         print(li[10:],end=' ')
                #     if li[:11] == ' "lemma" : ':
                #         print(li[12:-1],end=' ')
                #     if li[:10] == ' "type" : ':
                #         print(li[11:-1])
                count += 1
    print("%s\t%d\t%d" % (i, idcount,filecount))
    total += filecount
    ttt += idcount
    # break
# print(cccc)
print(total)
print(ttt)
print(total / 4)
