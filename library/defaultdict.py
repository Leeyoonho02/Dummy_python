#defaultdict
from collections import defaultdict

input()
dic = defaultdict(int)
for i in list(map(int, input().split())):
    dic[i] += 1

input()
for i in list(map(int, input().split())):
    print(dic[i], end=" ")

