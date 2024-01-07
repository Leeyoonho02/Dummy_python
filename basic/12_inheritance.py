#parent class
class Animal(): 
    def walk(self):
        print("walking...")

    def eat(self):
        print("eating...")
        
#child class : can use method of parent class
#use something of parent in child : super().methodOfParent()
class Human(Animal):
    def shake(self):
        print("shaking hand...")

class Dog(Animal):
    def wag(self):
        print("wagging tail...")
        
cow = Animal()

cow.walk()
cow.eat()

#child class : can use method of parent class
man = Human()
dog = Dog()

man.walk()
man.shake()
dog.eat()
dog.wag()

