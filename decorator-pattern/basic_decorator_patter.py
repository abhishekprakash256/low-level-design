"""
Using the decorator pattern for the beverage class 
"""



class Beverage():

	def cost(self):

		return 2


class Coffee() :

	def __init__(self, beverage) :

		self.beverage = beverage

	def cost(self) :

		return self.beverage.cost() + 1


class Expresso(Coffee) : 

	def cost(self):

		return self.coffee.cost() + 2


class HotChoclate(Coffee):

	def cost(self):

		return self.expresso.cost() + 1




if __name__ =="__main__":

	beverage = Beverage()


	coffee = Coffee(beverage)

	expresso = Expresso()

	hotchoclate = HotChoclate()


	res_hotchoclate = HotChoclate.cost()

	print(res_hotchoclate) 