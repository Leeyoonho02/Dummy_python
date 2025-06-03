import time
import matplotlib.pyplot as plt
import numpy as np

def CUT_ROD(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i-1] + CUT_ROD(p, n-i))
    return q

def DP_CUT_ROD(p, n):
    r = [0 for i in range(n+1)]
    r[0] = 0
    
    for i in range(n+1):
        q = float('-inf')
        for j in range(i+1):
            q = max(q, p[j-1] + r[i-j])
        r[i] = q
    return r[n]

if __name__ == "__main__":
    N = [10, 13, 15, 18, 20]
    p = np.random.randint(1, 50, size=N[-1])
    p.sort()
    print(f"p: {p}\n")
    
    time_list_CR = []
    time_list_DPCR = []
    
    for n in N:
        print(f"[n = {n}]")
        
        start_time = time.time()
        print("Result of CUT_ROD: ", CUT_ROD(p, n))
        end_time = time.time()
        print(f"Time taken (CUT_ROD): {end_time - start_time} seconds")
        time_list_CR.append(end_time - start_time)
        
        start_time = time.time()
        print("Result of DP_CUT_ROD: ", DP_CUT_ROD(p, n))
        end_time = time.time()
        print(f"Time taken (DP_CUT_ROD): {end_time - start_time} seconds")
        time_list_DPCR.append(end_time - start_time)
        
        print()

    plt.plot(N, time_list_CR, label="CUT_ROD")
    plt.plot(N, time_list_DPCR, label="DP_CUT_ROD")
    plt.legend()
    plt.show()