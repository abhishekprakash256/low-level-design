"""
This file is for using command pattern and coding using a remote and device example
"""

from abc import ABC, abstractmethod


#making the abstract class method
class Command(ABC):
    """
    This is the command abstract class
    """

    @abstractmethod
    def execute(self):
        pass



#making the Concrete command

class TurnOnCommand(Command) :

    def __init__(self , device):

        self.device = device

    def execute(self):
        
        self.device.turn_on()


class TurnOffCommand(Command) :

    def __init__(self , device):

        self.device = device

    def execute(self):
        
        self.device.turn_off()



class AdjustVolumeCommand(Command) :

    def __init__(self , stereo):

        self.stereo = stereo

    def execute(self):
        
        self.stereo.adjust_volume()

    
class ChangeChannel(Command):

    def __init__(self, tv):

        self.tv = tv
    
    def execute(self):
        return self.tv.change_channel()





#abstract class for the device 
class Device(ABC):

    @abstractmethod
    def turn_on(self):

        pass

    
    @abstractmethod
    def turn_off(self):

        pass



#concrete device 
class TV(Device):

    def turn_on(self):
        
        print("TV is turned on")

    def turn_off(self):
        
        print("TV is turned off")

    def change_channel(self):

        print("Channel is changed")


class Stereo(Device):

    def turn_on(self):

        print("Stereo is tuened ON")


    def turn_off(self):

        print("Stereo is tuened OFF")

    def adjust_volume(self):

        print("Stereo volume is adjusted")



#remote control class for the invoker
class RemoteControl():

    def __init__(self):

        self.command = None

    def set_command(self, command):

        self.command = command

    def press_button(self):

        if self.command is not None :

            self.command.execute()

        else:
            print("No command has been assinged")



if __name__ == "__main__" :

    #make the device
    tv = TV()

    stereo = Stereo()

    #create command
    turn_on_tv = TurnOnCommand(tv)
    turn_off_tv = TurnOffCommand(tv)
    adjust_volume = AdjustVolumeCommand(stereo)
    change_channel = ChangeChannel(tv)


    #make the invoker 
    remote = RemoteControl()


    # Execute commands
    remote.set_command(turn_on_tv)
    remote.press_button()

    remote.set_command(adjust_volume)
    remote.press_button()

    remote.set_command(change_channel)
    remote.press_button()

    remote.set_command(turn_off_tv)
    remote.press_button()



    