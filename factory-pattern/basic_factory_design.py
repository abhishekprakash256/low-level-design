"""
The basic factory design 

"""

from abc import ABC, abstractmethod


#the abstract method
class Button(ABC):

    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC) :

    @abstractmethod
    def render(self):
        pass


#the concrete class for windows
class WindowsButton(Button):

    def render(self):
        print("This is windows button")


class WindowsCheckbox(Checkbox):

    def render(self):
        print("This is windows checkbox")


#the concrete class for macos 
class MacosButton(Button):

    def render(self):
        print("This is the macos button")

class MacosCheckbox(Checkbox):

    def render(self):
        print("This is macos checkbox")





#make the factory abstract class
class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:

        pass

    @abstractmethod
    def create_checkbox(self) -> Button :

        pass





#make the factory class
class WindowsFactory(GUIFactory) :

    def create_button(self):

        return WindowsButton()
    
    def create_checkbox(self):
        
        return WindowsCheckbox()
    

#make the factory class for Macos
class MacOsFactory(GUIFactory) :

    def create_button(self):
        return MacosButton()
    
    def create_checkbox(self):
        return WindowsButton()



#create the class for Application

class Application:

    def __init__(self , factory : GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render(self):

        self.button.render()
        self.checkbox.render()




def configure_app(os_type: str):

    if os_type == "windows":
        factory = WindowsFactory()
    else:
        factory = MacOsFactory()

    app = Application(factory)
    return app


app = configure_app("windows")
app.render()