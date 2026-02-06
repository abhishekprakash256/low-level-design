"""
The observer of the notifcation system

use a newpublisher as concrete subject 
obersever are email , sms , push notification


"""


from abc import ABC, abstractmethod



class Observer(ABC):
	"""
	The observer absttarct class
	"""

	@abstractmethod
	def update(self, message : str) :

		pass



#the concrete class for the subscriber that are observer
class EmailSubscriber(Observer):
	"""
	The email notification observer class
	"""

	def update(self, message : str):

		print(f"EMAIL received news: {message}")



class SMSSubscriber(Observer):
	"""
	The SMS notification observer class
	"""

	def update(self, message : str):

		print(f"SMS received news: {message}")



class PUSHSubscriber(Observer):
	"""
	The email notification observer class
	"""

	def update(self, message : str):

		print(f"PUSH received news: {message}")





#the abstract class for the subject
class Subject(ABC):
	"""
	The subject abstract class
	"""

	@abstractmethod
	def attach(self, observer :Observer ):

		pass


	@abstractmethod
	def detach(self, observer : observer):

		pass


	@abstractmethod
	def notify(self):

		pass


#the concrete subject class
class NewsPublisher(Subject):
	"""
	The NewsPublisher class to push the notification
	"""

	def __init__(self):
		self.observers = []
		self.latest_news = None

	def attach(self, observer) :

		self.observers.append(observer)


	def detach(self, observer) :

		self.observers.remove(observer)


	def publish_news(self, news : str):

		self.latest_news = news
		self.notify()


	def notify(self):
		
		for observer in self.observers:

			observer.update(self.latest_news)





