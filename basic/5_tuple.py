#can't modify or delete value

tuple1 = (1, 2, 3)
print(tuple1)
tuple2 = 1, 2, 3
print(tuple2)

list1 = [1, 2, 3]
tuple3 = tuple(list1)
print(tuple3)

#packing, unpacking
a, b = 1, 2
print(a, b) #1 2

#unpacking
c = (3, 4)
d, e = c
print(d, e) #3 4

#packing
f = d, e 
print(f) #(3, 4)

#example : value change
x = 10
y = 20
x, y = y, x
print(x, y) #20 10

#example : return of function
def func():
	return 100, 200
x, y = func()
print(x, y) #100 200

#example : for
for a in enumerate(list1):
	print('idx : {}, val : {}'.format(*a)) #'*' : unpack tuple
dict = {'a':1, 'b':2, 'c':3}
for a in dict.items():
	print('key : {}, val : {}'.format(*a))