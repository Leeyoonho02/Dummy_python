#class : A set of functions or variables
#instance : object created by class, each have own value

list1 = [1, 2, 3]
list2 = [1, 2, 3]

#list1, 2 is instance of same class (list class)
print(isinstance(list1, list)) #True
print(isinstance(list2, list)) #True

#list1, 2 has same value
print(list1 == list2) #True

#list1, 2 is diffirent instance
print(list1 is list2) #False

#class making
class Human():
    '''human being'''
    language = ""
    name = ""

person1 = Human() #make instance
person2 = Human()

person1.language = 'korean'
person2.language = 'english'
person1.name = 'yoonho'
person2.name = 'peter'

def speak(person):
		print("{} says {}.".format(person.name, person.language))

#Human.speak = speak #give function to class
#person1.speak() #same result with speak(person1)
#person2.speak() #same  