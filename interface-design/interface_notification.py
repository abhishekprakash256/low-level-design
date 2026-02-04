"""
Notification System

Requirements:

System must support:

Email

SMS

Push Notification

Every notification must:

send(recipient, message)

Logging is required for all notifications

Validation (empty message / recipient) is required
"""



from abc import ABC, abstractmethod


#interface class
class BaseNotification(ABC):
	"""
	The base notification interface class
	"""

	@abstractmethod
	def send(self, recipient , message) :
		"""	
		The send notification method
		"""

		pass



#the abstract class
class NotificationSystem():

	def validate(self, recipient , message) :
		"""
		Validate the payment
		"""

		if not message :

			print("The message is empty")

			#return False

		if not recipient :

			print("The recipient is not present")

			#return False


	def logging(self, recipient , message) :
		"""
		The method to log the message
		"""

		print(f"The {message} is send to {recipient}")


	def send_notification(self, recipient, message):
		"""
		Template-style method
		"""

		self.validate(recipient, message)
		self.send(recipient, message)
		self.logging(recipient)




#concrete class 
class EmailNotification(NotificationSystem):
	"""
	The email notification class
	"""

	def send(self, recipient , message ) :

		print(f"The {message} is send through email to {recipient}")



class PushNotification(NotificationSystem):
	"""
	The email notification class
	"""

	def send(self, recipient , message ) :

		print(f"The {message} is send through PUSH to {recipient}")


class SMSlNotification(NotificationSystem):
	"""
	The email notification class
	"""

	def send(self, recipient , message ) :

		print(f"The {message} is send through SMS to {recipient}")




def notify(notification: BaseNotification, recipient, message):
    notification.send_notification(recipient, message)



if __name__ == "__main__" :

	emailnotification = EmailNotification()

	print(emailnotification.send("Anny","Hello"))


	smsnotification = SMSlNotification()

	print(smsnotification.send("Anny","Hello"))

	
	pushnotification = PushNotification()

	print(smsnotification.send("Anny","Hello"))

	
