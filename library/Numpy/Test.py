import numpy as np

arr = np.array([[3, 6, 9], [2, 4, 8]])
print(arr.shape)
print(arr.mean())
print(arr.sum(axis=0))  # 열별 합계
print(arr.max(axis=1))  # 행별 최댓값

# 리스트 버전
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = []
for i in range(3):
    result.append(list1[i] + list2[i])
print("list ver: ", result)

# numpy 버전
print("numpy ver: ", np.add(list1, list2))