# find GCD by Euclidean Algorithm
# GCD(a, b) == GCD(b, a%b) (a > b)
def GCD(a, b):
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)

# find LCM by GCD
# LCM(a, b) == (a*b) / GCD(a, b)
def LCM(a, b):
    return (a*b)/GCD(a, b)

a, b = map(int, input().split())
print(GCD(a, b), LCM(a, b))