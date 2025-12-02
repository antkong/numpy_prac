import numpy as np
data = np.random.rand(10)
print(data)
print(f"평균: {np.mean(data)}")
print(f"표준편차: {np.std(data)}")
print(f"제 1 사분위수: {np.quantile(data, .25)}")
print(f"제 3 사분위수: {np.quantile(data, .75)}")

#왜도 = (평균 - 중앙값) / 표준편차
def skewness(array:np.ndarray) -> float:
    mean = np.mean(array)
    length = len(array)
    return np.power((np.sum((array - np.power(mean, 3)))/length)/(np.sum(np.power((array - mean), 2))/length), 3/2)

def kurtosis(array:np.ndarray) -> float:
    mean = np.mean(array)
    n = array.shape[0]
    return n * np.sum(np.power((array - mean),4))/np.power(np.sum(np.power((array - mean),2)),2)
