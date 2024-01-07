#key : string, number, tuple
#value : any data

dict = {'a':1, 'b':2, 'c':3}
print(dict['b']) #2

print('a' in dict) #True
print('d' in dict) #False

#add, modify
dict['d'] = 4
dict['a'] = 111
print(dict) #{'a':111, 'b':2, 'c':3, 'd':4}

#delete
del(dict['c'])
dict.pop('d')
print(dict) #{'a':111, 'b':2}

dict.clear()
print(dict) #{}

#merge
dict1 = {1:111, 2:222}
dict2 = {1:11, 3:33}
dict1.update(dict1) #update dict1 to dict2
print(dict1) #{1:11, 2:223, 3:33}

#with 'for'
for key in dict1.keys(): #can omit 'keys()'
    print(key) #1 2
for value in dict1.values():
    print(value) #111 222
for key, value in dict1.items():
    print(key, value) #1 111, 2 222
#in dictionary, dont care about order