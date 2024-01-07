#for
list1 = [876, 45, 986, 567, 56786, 9865, 345]
for x in list1: #value of list1
    print(x)
for i in range(5): #0 1 2 3 4
    print(i)
for i in range(len(list1)): #0 1 2 3 4 5 6
    print(i)
for i, val in enumerate(list1): #index and value of list
    print(i, val)

#while
selected = input('가위, 바위, 보 중에 선택하세요>')
while selected not in ['rock', 'scissors', 'paper']:
    selected = input('가위, 바위, 보 중에 선택하세요>')
