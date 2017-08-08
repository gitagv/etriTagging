import glob
import os

FILEpath = glob.glob(os.path.join('./ucorpus_news', '*.ucorpus'))
# 케냐.txt
FILES = [f + '.txt' for f in FILEpath]
FILENAME = [file.split('.txt.ucorpus')[0] for file in FILEpath]
# FILENAME = ['케냐', '칭기즈 칸', '소수 (수론)', '마르틴 루터', '힘 (물리)', '라인 강',
#             '아폴로 계획', '하버드 대학교', '원나라', '시카고 대학교', '엽록체', '제국주의', '니콜라 테슬라',
#             '계산 복잡도 이론', '산소', '위그노', '흑사병',
#             '잭슨빌 (플로리다 주)', 'ABC (미국의 방송사)', '노르만인', '닥터 후', '건설', '증기 기관',
#             '프레즈노', '기후 변화에 관한 정부간 패널', '아마존 우림', '빅토리아 앨버트 박물관',
#             '프렌치 인디언 전쟁', '면역계', '시민 불복종', '스카이 (영국 & 아일랜드)', '남부 캘리포니아', '경제적 불평등', '스코틀랜드 의회', '슈퍼볼 50']
print(FILENAME)
for filename in FILENAME:
    with open(filename + '.txt.ucorpus', "r", encoding="utf-8") as f:
        data = f.read()
        count = 0
        # 문장\n형태소 단위 리스트
        data = data.split('\n\n')
        data_1 = []
        data_2 = []
        for n, d in enumerate(data):
            if d != '':
                # print(d)
                data_1 = d.split('\n')[0]
                data_2 = d.split('\n')[1].strip(' ')
                eojeol_1 = data_1.replace('  ', ' ').replace('   ', ' ').split(' ')
                eojeol_2 = data_2.split(' ')
                len_1 = len(eojeol_1)
                len_2 = len(eojeol_2)

                # print(eojeol_1, len_1)
                # print(eojeol_2, len_2)

                if len_1 == len_2:
                    pass
                else:
                    with open('./test/' + filename.split('\\')[1] + '.txt', "a", encoding="utf-8") as result_file:
                        result_file.write("{}번째 문장\n".format(n))
                        result_file.write("\n")
                        result_file.write("{}".format(d))
                        result_file.write("\n\n")