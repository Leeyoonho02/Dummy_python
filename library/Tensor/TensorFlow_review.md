# 🧠 Day 3 – TensorFlow 기본 복습 정리

## ✅ 1. 텐서 생성

```python
import tensorflow as tf
import numpy as np

# 상수 텐서
a = tf.constant([[1, 2, 3], [4, 5, 6]])

# 변수 텐서 (학습 가능한 값)
b = tf.Variable([[7, 8, 9], [10, 11, 12]])
```

---

## ✅ 2. 기본 연산

```python
x = tf.constant([1.0, 2.0, 3.0])
y = tf.constant([4.0, 5.0, 6.0])

tf.add(x, y)            # [5.0, 7.0, 9.0]
tf.multiply(x, y)       # [4.0, 10.0, 18.0]
tf.reduce_mean(y)       # 평균: 5.0
```

---

## ✅ 3. 자동 미분 (Auto Differentiation)

```python
x = tf.Variable(3.0)

with tf.GradientTape() as tape:
    y = x**2 + 2*x + 1

dy_dx = tape.gradient(y, x)  # 도함수: 2x + 2 → 8.0
```

### 🧪 실습 문제 1

```python
x = tf.Variable(5.0)
with tf.GradientTape() as tape:
    y = x ** 3
dy_dx = tape.gradient(y, x)
print(dy_dx)  # 결과: 75.0 (정답!)
```

---

## ✅ 4. 정적 그래프 (`@tf.function`)

```python
@tf.function
def my_func(x, y):
    return x * y + 3

my_func(tf.constant(3.0), tf.constant(4.0))  # 결과: 15.0
```

### 🧪 실습 문제 2

```python
@tf.function
def cube_plus_one(x):
    return x**3 + 1

cube_plus_one(tf.constant(2.0))  # 결과: 9.0
```

---

## ✅ 5. NumPy <-> Tensor 변환

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

tf_arr = tf.convert_to_tensor(arr)
np_arr = tf_arr.numpy()
```

---

> 다음은: **Day 4 – Keras 모델 설계 복습**