#list comprehension
areas1 = [i*i for i in range(1, 11)]
print(areas1) 
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

areas2 = [i*i for i in range(1, 11) if i%2 == 0]
print(areas2) 
#[4, 16, 36, 64, 100]

areas3 = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(areas3) 
#[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

#dictionary comprehension
students = ["tae", "jin", "jung", "ha", "sung"]
for num, name in enumerate(students):
	print("{}:{}".format(num+1, name))
#same result
studDict = {"{}".format(num+1):name for num, name in enumerate(students)}
print(studDict)

scores = [85, 92, 78, 90, 100]
for x, y in zip(students, scores):
	print(x, y)
#same result
scoreDict = {name:score for name, score in zip(students, scores)}
print(scoreDict)