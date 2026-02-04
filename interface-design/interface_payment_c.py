"""
The progrom to make the basic of the interface design


We’ll build a Payment System using:

Interface (contract)

Abstract class (shared behavior)

Concrete implementations

Client code that depends only on the interface
"""

"""
abstract class 

for interface class 

class PaymentMethod(ABC)

for abstract class 

class BasePayment(PaymentMethod):

mehod validate_pay()

method log()

method succesfull_payment()






"""



from abc import ABC, abstractmethod




#make the interface class
class PaymentMethod(ABC):
	"""
	The interface class for payment
	"""

	@abstractmethod
	def pay(self, amount: float) :
		"""
		The pay method
		"""

		pass




#make the abstract class
class BasePayment(PaymentMethod):
	"""
	The base payment class for payment
	"""

	def validate_pay(self, amount : float) :
		"""
		The method to validate pay
		"""

		if amount < 0 :

			raise ValueError("Payment failed: invalid amount")


	def log_payment(self,amount : float):
		"""
		The log of the payment done
		"""

		print(f"Payment of {amount} succesfull")


	def succesfull_payment(self , amount):
		"""
		The succesfull payment method 
		Template-style method
		"""

		self.validate_pay(amount) 

		self.log_payment(amount)

		self.pay(amount)




#make the concrete class
class CreditCardPayment(BasePayment):
	"""
	The credit card payment class 
	"""

	def pay(self, amount):
		"""
		The payment method for card
		"""

		print(f"The paymnet has been done by card for {amount}")





if __name__ == "__main__":

	cardpayment = CreditCardPayment()

	pay_card = cardpayment.succesfull_payment(10)










	
