list1 = [1, 2, 3, 4, 5]
print(list1) #[1, 2, 3, 4, 5]
#list1[0], list1[2], … , list1[-1], list1[-2], …

#add
list1.append(6)
list1 = list1 + [7, 8, 9] #can plus between list
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#delete
del list1[1] #delete value of 1th idx
list1.remove(3) #del '3'
list1.pop(4) #return deleted value
print(list1) #[1, 4, 5, 6, 8, 9]

length = len(list1)
print(length) #6

#methods
list1.index(9) #find index of value
list1.extend([10, 11]) #add value on last
list1.insert(5, 100) #insert 100 on 5th idx
print(list1) #[1, 4, 5, 6, 8, 100, 9, 10, 11]

list1.sort() #sorting
list1.reverse() #reverse order
print(list1) #['100', '11', '10', '9', '8', '6', '5', '4', '1']

#list and string
str1 = "".join(list(map(str, list1))) #from list to string. attach list based on " "
print(str1) #1001110986541
list2 = str1.split("\0") #from string to list. slice string based on parameter
print(list2) #['1001110986541']
list3 = list(str1) #slice every spelling 
print(list3) #['1', '0', '0', '1', '1', '1', '0', '9', '8', '6', '5', '4', '1']

#slicing
#list1[x, y] #from xth idx, to y-1th idx
#string1[x, y]
#list1[x, y, z] #z : step.

del list1[:5] #first~4th idx delete
print(list1) #[6, 5, 4, 1]
list1[1:3] = [77, 88]
print(list1) #[6, 77, 88, 1]
list1[1:3] = [77, 88, 99] #diffirent number of value
print(list1) #[6, 77, 88, 99, 1]
list1[1:3] = [77]
print(list1) #[6, 77, 99, 1]