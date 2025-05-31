import random
import numpy as np

n, m = map(int, input().split())
l = np.random.choice(np.arange(1, n+1), m, 0)
l.sort()
print(l)