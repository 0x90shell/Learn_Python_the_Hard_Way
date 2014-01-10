"""
What happened is Python's original rendition of class was broken in many serious ways. By the time they admitted the fault it was too late, and they had to support it. In order to fix the problem, they needed some "new class" style so that the "old classes" would keep working but you could use the new more correct version. This is where "class is-a object" comes in. They decided that they would use the word "object", lowercased, to be the "class" that you inherit from to make a class. Confusing right? A class inherits from the class named object to make a class but it's not an object really it's a class, but do not forget to inherit from object.

Python 3.x:
class MyClass(object): = new-style class
class MyClass: = new-style class (implicitly inherits from object)

Python 2.x:
class MyClass(object): = new-style class
class MyClass: = OLD-STYLE CLASS
"""

class pet(object): #class
	number_of_legs = 0
	
	#second argument is turned into a local variable within the class instance called "name".
	def __init__(self,name):
		self.name = name
		
	def sleep(self): 
		#method, this is essentially a function that always has a variable called self
		#self refers to the word preceeding the method in dot notation
		#for example instance.sleep() would populate self variable with "instance"
		print "%s is sleeping. ZZzzz..." % self.name
		
	def count_legs(self):
		print "%s has %s legs." % (self.name, self.number_of_legs)

#dog is-a pet		
class dog(pet): 

	#dog class inherits from pet class, meaning it has pet and dog methods available to use
	def bark(self):
		print "%s is a dog. Woof woof!" % self.name
		
Doug = dog("Doug") 
#instance, class is useless if not intitialized in an instance
Doug.sleep()
Doug.bark()
Doug.number_of_legs = 4 #doug is a dog, lol
Doug.count_legs()

Nemo = pet("Nemo")
Nemo.count_legs()
