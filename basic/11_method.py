#example code
class Human():
    '''human being'''
    def __init__(self, name, weight): #initializing
        print("execute __init__")

        self.name = name
        self.weight = weight

        print("create... name : {}, weight : {}".format(self.name, self.weight))
    '''
    def create(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person
	'''		
    def __str__(self): #instance print form
        return "{}({}kg)".format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print("{} eat, weight become {}.".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{} walk, weight become {}.".format(self.name, self.weight))

    def speak(self, message):
        print('{} says "{}"'.format(self.name, message))

#person = Human.create('yoonho', 67)
person = Human("yoonho", 67)

person.walk()
person.eat()
person.eat()
person.speak("hello!")
print(person)