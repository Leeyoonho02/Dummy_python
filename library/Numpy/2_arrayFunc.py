import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("1. 배열 기능")
print(a.sum())
print(a.mean())
print(a.std())     # 표준편차
print(a.var())     # 분산
print(a.max())     # 최대값
print(a.min())     # 최소값

print(a.sum(axis=0))        # 열 방향 합계
print(a.sum(axis=1))        # 행 방향 합계
print(a.mean(axis=0))       # 열 방향 평균
print(a.mean(axis=1))       # 행 방향 평균

print("2. indexing / slicing")
print(a[0, 1])
print(a[:, 1])      # 2번째 열 추출
print(a[1, :])      # 2번째 행 추출

print("3. broadcasting")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 0, 1])

print(a + b)
print(a - b)

print("4. 배열 변환")
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a.reshape(10))
print(a.reshape(2, 5))

