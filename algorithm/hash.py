if __name__ == '__main__':
    N, M = map(int, input().split())
    
    hashKeyList = []
    for _ in range(N):
        hashKeyList.append(hash(input()))
    
    temp = ''
    answerList = []
    for _ in range(M):
        temp = input()
        if hash(temp) in hashKeyList:
            answerList.append(temp)
    
    answerList.sort()
    print(len(answerList))
    for name in answerList:
        print(name)