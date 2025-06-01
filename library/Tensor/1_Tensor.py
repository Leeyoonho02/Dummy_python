import tensorflow as tf
import numpy as np

# constant tensor
a = tf.constant([[1, 2, 3], [4, 5, 6]])
#print(a)

# variable tensor (learnable)
b = tf.Variable([[7, 8, 9], [10, 11, 12]])
#print(b)

x = tf.constant([1.0, 2.0, 3.0])
y = tf.constant([4.0, 5.0, 6.0])

print(tf.add(x, y))
print(tf.multiply(x, y))
print(tf.reduce_mean(y)) # reduce: 어떠한 방법으로 값을 하나로 줄인다는 뜻.

# 자동 미분 auto differentiation
x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = x**2 + 2*x + 1
    
dy_dx = tape.gradient(y, x)
print(dy_dx)

# 정적 그래프
@tf.function
def my_func(x, y):
    return x*y + 3

print(my_func(tf.constant(3.0), tf.constant(4.0)))

# numpy <-> tensor
arr = np.array([[1, 2, 3], [4, 5, 6]])

tf_arr = tf.convert_to_tensor(arr)
print(tf_arr)

np_arr = tf_arr.numpy()
print(np_arr)