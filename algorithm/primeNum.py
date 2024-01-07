import sys

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    m, n = map(int, sys.stdin.readline().split())

    for i in range(m, n+1):
        if is_prime(i):
            print(i)