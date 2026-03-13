"""
makding the basic singleton pattern
"""


class SingeltonClass():
	"""
	This is a wrong example as creation of the class has to ignore the second object
	"""

	def test_func(self, word) :

		return f"This is the {word}"


class SingeltonClassFixed():

	def test_func(self) :

		return "This is the test"

singelton_class = SingeltonClass()

singelton_class_fixed = SingeltonClassFixed()