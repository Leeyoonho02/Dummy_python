from sys import stdin
import itertools

count = 0
n, r = map(int, stdin.readline().split())
nPr = itertools.permutations(range(n), r)
nCr = itertools.combinations(range(n), r)

print(list(nPr))
print(list(nCr))