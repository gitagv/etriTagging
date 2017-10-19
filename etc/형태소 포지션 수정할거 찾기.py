
def main():
    file1 = open("H:\ETRI 태깅 용역\백업\legal_morp\Legal_morp_헌법_현진.txt", 'r', encoding='utf-8')
    # file2 = open("K:\ETRI 태깅 용역\백업파일\법률문서\일본국헌법.txt", 'r', encoding='euc-kr')
    # file3 = open("K:\ETRI 태깅 용역\백업파일\법률문서\러시아 연방 헌법.txt", 'r', encoding='euc-kr')

    line1 = file1.readlines()
    # line2 = file2.readlines()
    # line3 = file3.readlines()

    for a in line1:
        if a.split(' ')[3] == "INSERT":
            print(a, end='')
    for a in line1:
        if a.split(' ')[3] == "REMOVE":
            print(a, end='')
    #
    # for a in line2:
    #     if a.split('\t')[3] == "INSERT":
    #         print(a, end='')
    #     if a.split('\t')[3] == "REMOVE":
    #         print(a, end='')
    #
    # for a in line3:
    #     if a.split('\t')[5] == "INSERT":
    #         print(a, end='')
    #     if a.split('\t')[5] == "REMOVE":
    #         print(a, end='')
main()