"""
making a test for the abstract class 
"""


from abc import ABC, abstractmethod


#make the animal class 
class Animal(ABC):

    @abstractmethod
    def sound(self):
        """
        Docstring for sound
        
        The abstract makes the method essential to define in sub class
        """
        pass

    def movement(self):
        pass



class Dog(Animal):

    def sound(self):

        return "Bark"
    


dog = Dog()

print(dog.sound())