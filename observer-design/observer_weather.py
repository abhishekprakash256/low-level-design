"""
Docstring for observer-design.observer_weather

makiing the observer pattern with the weather 

reqs : --

the observer abstract class 

the observer concrete class 
the phone 
the app


the subject abstract clas

the subject concreate class 
weather station

"""


from abc import ABC, abstractmethod
from typing import List



class Observer(ABC):
    """
    Docstring for Observer
    The observer abstract class
    """
    
    @abstractmethod
    def update(self,weather : str):

        pass


class Subject(ABC):
    """
    Docstring for Subject
    The subject abstract class 
    """

    @abstractmethod
    def add_observer(self, observer : Observer):

        pass
  

    @abstractmethod 
    def remove_observer(self, observer : Observer):

        pass


    @abstractmethod
    def notify_observer(self, weather : str):

        pass



#make the concrete class for weather
class Weather(Subject):
    """
    The weather concrete class
    """

    def __init__(self):
        self.observers = []
        self.weather = ""

    def add_observer(self, observer : Observer):
        """
        The function to add the observer
        """

        self.observers.append(observer)


    def remove_observer(self, observer : Observer):
        """
        The function to remove the obsever
        """

        self.observers.remove(observer)

        
        
 





