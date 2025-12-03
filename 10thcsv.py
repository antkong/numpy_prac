# crime_in_seoul.csv‛ 파일을 사용하여 다음과 같은 작업을 수행하시오
# 출처: 구글 코랩에서 작성 (https://colab.research.google.com/)
# csv 파일을 읽어서 데이터프레임 객체로 만들기 (인코딩은 ‘euc-kr’로 읽어오기)
# 살인이 10건 이상 발생한 곳 데이터 추출하기
# 살인의 발생에 대한 합계 구하기
# 살인의 검거에 대한 합계 구하기

crime_seoul = pd.read_csv("crime_in_seoul.csv", encoding='euc-kr')
d=crime_seoul[crime_seoul.죄종 == '살인']
d1=d[d.발생검거 == '발생']
d1[d1.건수>=10]
d=crime_seoul[crime_seoul.죄종 == '살인']
d1=d[d.발생검거 == '발생']
sum(d1.건수)
d=crime_seoul[crime_seoul.죄종 == '살인']
d2=d[d.발생검거 == '검거']
sum(d2.건수)





import pandas as pd

# 1. CSV 파일 읽기 (euc-kr 인코딩)
crime_seoul = pd.read_csv("crime_in_seoul.csv", encoding='euc-kr')

# 2. 죄종이 '살인'인 데이터만 추출
murder = crime_seoul[crime_seoul['죄종'] == '살인']

# 3. '발생' 중에서 10건 이상 발생한 곳
murder_over_10 = murder[(murder['발생검거'] == '발생') & (murder['건수'] >= 10)]
print("▶ 살인이 10건 이상 발생한 곳")
print(murder_over_10)

# 4. 살인의 발생 합계
murder_occ_sum = murder[murder['발생검거'] == '발생']['건수'].sum()
print("\n▶ 살인의 발생 합계:", murder_occ_sum)

# 5. 살인의 검거 합계
murder_arrest_sum = murder[murder['발생검거'] == '검거']['건수'].sum()
print("\n▶ 살인의 검거 합계:", murder_arrest_sum)
