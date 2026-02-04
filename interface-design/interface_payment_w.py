"""
The progrom to make the basic of the interface design


We’ll build a Payment System using:

Interface (contract)

Abstract class (shared behavior)

Concrete implementations

Client code that depends only on the interface



--------------------------------------------

make a paymnet class with base payment method

PaymentMethod()
method pay


abstract class -- 

BasePaymnet()
def validate()

def log()


CreditCardPayment(BasePayment)


has both method


"""




from abc import ABC, abstractmethod



class PaymentMethod(ABC):
	"""
	The interface class
	"""

	def pay(self, amount : float):

		pass



class BasePayment(PaymentMethod):
	"""
	The abstract method class
	"""

	def validate_pay(self, amount):
		"""
		The validate pay class
		"""

		if amount < 0 :

			return False

		else :

			return True


	def log(self, amount):
		"""
		The log method for the payment
		"""

		return f"The payment of {amount} been logged"




class CreditCardPayment(BasePayment):
	"""
	The concrete class
	"""


	def pay(self, amount: float):

		return amount



	def succesfull_payment(self , amount : float ):

		self.validate_pay(amount)

		self.log(amount)

		self.pay(amount)

		return True





if __name__ == "__main__":

	cardpayment = CreditCardPayment()

	print(cardpayment.succesfull_payment(10))






