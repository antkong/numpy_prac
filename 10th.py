# 엑셀 파일에서 3번째 행을 header로 하여 2, 4, 7, 10, 14번째 열을 가져와서 데이터프레임 객체로 만들기
# 데이터프레임의 column명을 [‘구별’, ‘인구수’, 한국인’, ‘외국인’, ‘고령자’]로 변경하기
# ‘구별’을 인덱스로 설정하기
# 1번째 행(합계 데이터) 삭제하기
# 각 구별 한국인의 비율 구하기
# 각 구별 외국인의 비율 구하기
# 각 구별 고령자의 비율 구하기
# 인구수가 가장 많은 구부터 보이도록 정렬하기
# 인구수가 적은 순서대로 5개 구 출력하기
# 외국인 수 내림차순 정렬하기
# 고령자 비율 오름차순 정렬하기
import pandas as pd

pop_seoul = pd.read_excel("pop_in_seoul.xlsx", usecols=[1,3,6,9,13], header=2)

pop_seoul.columns = ['구별', '인구수', '한국인', '외국인', '고령자']
pop_seoul.set_index('구별', inplace=True)
pop_seoul.drop('합계', inplace=True)

# 비율 계산
pop_seoul['한국인비율(%)'] = pop_seoul['한국인'] / pop_seoul['인구수'] * 100
pop_seoul['외국인비율(%)'] = pop_seoul['외국인'] / pop_seoul['인구수'] * 100
pop_seoul['고령자비율(%)'] = pop_seoul['고령자'] / pop_seoul['인구수'] * 100

# 정렬
pop_desc = pop_seoul.sort_values(by='인구수', ascending=False, inplace=True)   # 인구수 많은 순
pop_asc_5 = pop_seoul.sort_values(by='인구수', ascending=True, inplace=True).head(5)  # 인구수 적은 5개 구
pop_foreign_desc = pop_seoul.sort_values(by='외국인', ascending=False, inplace=True)   # 외국인 많은 순
pop_old_asc = pop_seoul.sort_values(by='고령자비율(%)', ascending=True, inplace=True)  # 고령자 비율 적은 순

print(pop_seoul.head())
