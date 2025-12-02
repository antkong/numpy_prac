import numpy as np
#make array
a = np.arange(100,110).reshape(5,2)
#np.arange(범위 시작, 끝).reshape(1차배열개수, 2차배열개수)
print(a)

#Transpose(행과 열 교체)
b = np.arange(10).reshape(2,5).T
print(b)

#indexing

#slicing


#min, max(최소, 최댓값 return) 
#argmin, argmax(최소와 최대의 위치 return)
#sum, mean, median(행렬전체합, 평균, 중간값)
#sort(정렬: shuffle 배열, shuffling 명령)
#axis
#var, std(분산, 표준편차)
#exp, log, sin, cos
#dot