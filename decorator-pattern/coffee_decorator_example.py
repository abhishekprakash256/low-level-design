"""
Making a coffee decorator ecample using a coffee as base class and more variants 
The idea is to have open for addition but not changes to the class
"""

from abc import ABC , abstractmethod


#make the asbtract coffee class

class Coffee(ABC):
	"""
	The coffee base class
	"""

	@abstractmethod
	def get_description(self) :

		pass


	@abstractmethod
	def get_cost(self):

		pass




#make the concrete class
class SimpleCoffee(Coffee):
	"""
	The simple coffee concrete class
	"""

	def get_description(self) :

		return "This is simple coffee"


	def get_cost(self):

		return 2



#make the decorator class
class CoffeeDecorator(Coffee):

	def __init__(self, decorated_coffee):

		self.decorated_coffee = decorated_coffee


	def get_description(self):

		return self.decorated_coffee.get_description()



	def get_cost(self):

		return self.decorated_coffee.get_cost()



#make the latte class
class CoffeeExpresso(CoffeeDecorator):

	def get_description(self):

		return self.decorated_coffee.get_description() + " with Milk"

	def get_cost(self):

		return self.decorated_coffee.get_cost() + 2


#the hot choctlate coffee
class HotChoclateCoffee(CoffeeExpresso) :

	def get_description(self):

		return self.decorated_coffee.get_description() + " and Choclate"

	def get_cost(self):

		return self.decorated_coffee.get_cost() + 2




if __name__== "__main__":

	simple_coffee = SimpleCoffee()

	print(simple_coffee.get_cost())


	coffee_expresso = CoffeeExpresso(simple_coffee)

	print(coffee_expresso.get_description())

	print(coffee_expresso.get_cost())



	hot_choclate = HotChoclateCoffee(coffee_expresso)

	print(hot_choclate.get_description())

	print(hot_choclate.get_cost())