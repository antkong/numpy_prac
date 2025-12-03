import pandas as pd

# data = pd.read_csv("titanic.csv")
# print(data.head())
# #n=5가 기본임

#Series 생성
# name1 = ['철수','영이','길동','미영','순이','철이']
# score1 = [84,21,87,100,59,46]
# name2 = ['길동', '철수','영이','철이','순이','미영']
# score2 = [99,87,87,84,77,15]
# s1 = pd.Series(score1, index=name1)
# s2 = pd.Series(score2, index=name2)

# d = pd.DataFrame()
# d['국어'] = s1
# d['영어'] = s2

# print(d)
#index,columns DataFrame
scores = [[84,87,78],[21,15,84],[87,84,76],[100,87,99],[59,99,59],[46,77,56]]
names = ['a','b','c','d','e','f']
lectures = ['korean','math','english']
d2 = pd.DataFrame(scores, index = names, columns = lectures)
print(d2)

# #rename(객체변환)
# print(d2.rename(index={'a':'철수', 'b':'영이'}))
# print(d2.rename(columns = {'korean':'leac1','math':'leac2'}))

# #rename(원본 객체 변경)
# d2.rename(index={'c':'철수', 'd':'영이'}, inplace=True)
# d2.rename(columns = {'korean':'leac1','math':'leac2'}, inplace=True)
# print(d2)

# #drop(axis=0 : 행 / 1 : 열)
# d2.drop('a', axis=0, inplace=True)
# print(d2)

# #행, 열 추가
# d2.loc['total1'] = d2.sum(axis=0)
# d2['total2'] = d2.sum(axis=1)
# print(d2)

#행값 수정
d2.loc['a'] = [80,90,80]
d2.iloc[0] = [84,87,78]
#열값 수정
d2['korean'] = [80,30,90,100,60,50]
print(d2)