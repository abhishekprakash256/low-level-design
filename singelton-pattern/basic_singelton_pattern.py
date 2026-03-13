"""
makding the basic singleton pattern
"""


class SingeltonClass():

	def test_func(self, word) :

		return f"This is the {word}"


class SingeltonClassFixed():

	def test_func(self) :

		return "This is the test"

singelton_class = SingeltonClass()

singelton_class_fixed = SingeltonClassFixed()