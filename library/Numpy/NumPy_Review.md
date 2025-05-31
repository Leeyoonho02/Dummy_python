# 📘 Day 1 – NumPy 핵심 복습 정리

## ✅ 1. 배열 생성 및 구조

```python
import numpy as np

a = np.array([1, 2, 3])           # 1차원 배열
b = np.array([[1, 2], [3, 4]])    # 2차원 배열
```

- `a.shape`: 배열 형태
- `a.ndim`: 차원 수
- `a.size`: 전체 원소 수

---

## ✅ 2. 배열 생성 함수

```python
np.zeros((2, 3))       # 2x3 영행렬
np.ones((3, 3))        # 3x3 1행렬
np.eye(3)              # 단위 행렬
np.arange(0, 10, 2)    # [0 2 4 6 8]
np.linspace(0, 1, 5)   # [0. 0.25 0.5 0.75 1.]
```

---

## ✅ 3. 인덱싱 & 슬라이싱

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

a[0, 1]     # 2
a[:, 1]     # [2 5]
a[1, :]     # [4 5 6]
```

---

## ✅ 4. 브로드캐스팅

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 0, 1])

a + b
# [[2 2 4]
#  [5 5 7]]
```

---

## ✅ 5. 벡터화 연산 & 내적

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

x + y         # [5 7 9]
x * y         # [4 10 18]
np.dot(x, y)  # 32
```

---

## ✅ 6. 통계 함수

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

np.mean(a)            # 전체 평균
np.sum(a, axis=0)     # 열별 합계
np.max(a, axis=1)     # 행별 최대값
np.min(a)
np.std(a)
np.median(a)
```

---

## 🧪 실습 예제 요약

### ✔ 2x3 배열 실습

```python
arr = np.array([[3, 6, 9], [2, 4, 8]])

print(arr.shape)              # (2, 3)
print(np.mean(arr))           # 전체 평균
print(arr.sum(axis=0))        # 열별 합계
print(arr.max(axis=1))        # 행별 최대값
```

### ✔ 리스트 연산 vs. NumPy 연산

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 리스트 버전
result = []
for i in range(3):
    result.append(list1[i] + list2[i])
print("list ver: ", result)

# numpy 버전
print("numpy ver: ", np.add(list1, list2))
```

---

## 🎯 추가 실습 아이디어

### ✔ 브로드캐스팅 확인

```python
arr = np.array([[10, 20, 30], [40, 50, 60]])
add_vec = np.array([1, 2, 3])
print(arr + add_vec)
```

### ✔ 통계 함수 정리 실습

```python
a = np.array([[3, 1], [5, 7]])

print(np.min(a))
print(np.std(a))
print(np.median(a))
print(np.mean(a, axis=0))
```
