import pandas as pd
# # DataFrame을 엑셀로 저장
# scores = [[84,87,78],[21,15,84],[87,84,76],[100,87,99],[59,99,59],[46,77,56]]
# names = ['a','b','c','d','e','f']
# lectures = ['korean','math','english']
# d2 = pd.DataFrame(scores, index = names, columns = lectures)

# d2.to_excel("scores.xlsx")

# #엑셀 파일 열기

# # index 열 지정하지 않은 경우
# d2 = pd.read_excel("scores.xlsx")
# print(d2)
# #index 열 지정한 경우
# d2 = pd.read_excel("scores.xlsx", index_col=0)
# print(d2)
# #usecols로 가져올 컬럼을 지정한 경우
# d2 = pd.read_excel("scores.xlsx", index_col=0, usecols=['korean','math'])
# print(d2)
# # header를 설정한 경우
# d2 = pd.read_excel("scores2.xlsx", header=0)
# print(d2)

scores = [[84,87,78],[21,15,84],[87,84,76],[100,87,99],[59,99,59],[46,77,56]]
names = ['a','b','c','d','e','f']
lectures = ['korean','math','english']
d2 = pd.DataFrame(scores, index = names, columns = lectures)

# DataFrame을 csv로 저장
d2.to_csv("scores.csv")
# csv 파일 열기
d2.pd.read_csv("scores.csv", index_col=0)#열 지정 시 col=0
print(d2)