# 🤖 Keras 기본 복습 정리 made by GPT

## ✅ 1. 모델 구성 – Sequential API

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])
```

- `Dense`: 완전 연결 층 (fully connected layer)
- `activation`: 활성화 함수 (`relu`, `sigmoid`, `softmax`, 등)
- `input_shape`: 입력 특성의 개수

---

## ✅ 2. 모델 컴파일

```python
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

- `optimizer`: 가중치 업데이트 방식 (`adam`, `sgd`, 등)
- `loss`: 손실 함수
  - 이진 분류: `binary_crossentropy`
  - 다중 분류: `categorical_crossentropy`
- `metrics`: 성능 지표

---

## ✅ 3. 모델 학습

```python
model.fit(x_train, y_train, epochs=10, batch_size=32)
```

- `epochs`: 전체 데이터를 몇 번 반복 학습할지
- `batch_size`: 한 번에 학습할 데이터 개수

---

## ✅ 4. 모델 평가 & 예측

```python
loss, acc = model.evaluate(x_test, y_test)
print("테스트 정확도:", acc)

predictions = model.predict(x_test)
```

---

## ✅ 5. 실습 예제 – 랜덤 데이터

```python
import numpy as np

x_train = np.random.random((1000, 10))
y_train = np.random.randint(2, size=(1000, 1))
x_test = np.random.random((200, 10))
y_test = np.random.randint(2, size=(200, 1))

model = Sequential([
    Dense(128, activation='relu', input_shape=(10,)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=50, batch_size=32)
loss, acc = model.evaluate(x_test, y_test)
print("테스트 정확도:", acc)
```

---

## 🧠 실습 리뷰

- 입력/출력 모두 랜덤 → 학습할 수 있는 **패턴이 없음**
- 정확도는 보통 **50% 근처**
- 실제 의미 있는 학습을 위해선 **규칙 있는 데이터**가 필요

### ✔ 패턴이 있는 예시:
```python
x_train = np.random.random((1000, 10))
y_train = (x_train[:, 0] > 0.5).astype(int).reshape(-1, 1)
```

> x의 첫 번째 값이 0.5보다 크면 1, 아니면 0 → 학습 가능해짐!