class Animal(): 
		def greet(self):
				print("greeting...")
	

class Human(Animal):
		def shake(self):
				print("shaking hand...")
		
		def greet(self):
				self.shake()

class Dog(Animal):
		def wag(self):
				print("wagging tail...")

		def greet(self):
				self.wag()

class Cow(Animal):
		'''cow'''

man = Human()
dog = Dog()
cow = Cow()

cow.greet() #greeting...

#override
man.greet() #shaking hand...
dog.greet() #wagging tail...