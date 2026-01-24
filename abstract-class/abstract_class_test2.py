"""
Making an abstract for the shapes 
"""


from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Docstring for Shape
    making shapes for the abstract class
    """
    @abstractmethod
    def area(self):

        pass
    
    @abstractmethod
    def perimeter(self):

        pass




#make the shapes 

class Square(Shape):
    """
    Docstring for Square
    The square shape
    """

    def __init__(self, side):
        
        self.side = side

    
    def area(self):

        return self.side * self.side
    
    def perimeter(self):
        
        return 4 * self.side
    


class Rectangle(Shape) :
    """
    Docstring for Rectangle
    The Rectangle Shape
    """

    def __init__(self, length , width):
        
        self.length = length
        self.width = width

    
    def area(self):

        return self.length * self.width
    
    def perimeter(self):
        
        return 2 * (self.length + self.width)




if __name__ == "__main__":

    test_square = Square(4)

    test_rectangle = Rectangle(2,4)

    print(test_square.area())
    print(test_square.perimeter())


    print(test_rectangle.area())
    print(test_rectangle.perimeter())



        

    


