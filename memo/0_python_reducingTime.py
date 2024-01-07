'''input'''

#fast than input()
import sys
n = int(sys.stdin.readline())
sys.stdout.write(str(n))

#fast than append
list1 = [0]*n
print(list1)
for i in range(n):
    list1[i] = int(sys.stdin.readline())
    
print(list1[0])

'''print'''

#fast than print()print()...
s = ""
for i in list1:
    s += (str(i) + '\n')
print(s)