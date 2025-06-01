from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# 시퀀셜 모델 구조
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])

# Model compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy', # 이진 분류
    metrics=['accuracy']        # 평가 지표: 정확도
)

# test
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

model.compile(
    optimizer='adam', 
    loss='binary_crossentropy', 
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=50, batch_size=32)

loss, acc = model.evaluate(x_test, y_test)
print("테스트 정확도:", acc)