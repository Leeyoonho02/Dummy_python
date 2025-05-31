import numpy as np

print("1. 배열 생성")
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(a.shape, b.shape)
print(a.ndim, b.ndim)
print(a.size, b.size)
print(a.dtype, b.dtype)

print("2. 영행렬 생성")
c = np.zeros((2, 3))        # 영행렬 생성
print(c)

print("3. 1행렬 생성")
d = np.ones((2, 3))         # 1행렬 생성
print(d)

print("4. 단위행렬 생성")
e = np.eye(5)             # 단위행렬 생성
print(e)

print("5. 1부터 10까지의 배열 생성, 2씩 증가")
g = np.arange(1, 11, 2)   # 1부터 10까지의 배열 생성, 2씩 증가
print(g)

print("6. 0부터 1까지의 배열 생성, 5개의 요소로 나눔")
h = np.linspace(0, 1, 5)  # 0부터 1까지의 배열 생성, 5개의 요소로 나눔
print(h)

print("7. 1부터 10까지의 배열 생성, 5개의 요소로 나눔")
i = np.linspace(1, 10, 5)  # 1부터 10까지의 배열 생성, 5개의 요소로 나눔
print(i)