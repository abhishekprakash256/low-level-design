"""
Docstring for abstract-class.abstract_notification
designing a notification system with abstract class
the state is not in the correct place in Notification
"""


from abc import ABC, abstractmethod

class Notification(ABC):
    """
    The recipients state should not be there 
    """

    def __init__(self):

        self.recipients = []
        self.messages = []

    def log_notification(self , recipient ):
        """
        Docstring for log_notification
        concreate method for the logging
        """

        return "Notification send to" , recipient

    
    @abstractmethod
    def send(self):

        pass





class SMSNotification(Notification):
    """
    Docstring for SMSNotification
    The SMS sub class
    """

    def send(self,recipient , message):

        #add the recipient
        if recipient not in self.recipients:

            self.recipients.append(recipient)
        
        if message not in self.messages:

            self.messages.append(message)


        return "Sending SMS to ",recipient , ":"  , message
    



class EmailNotification(Notification):
    """
    Docstring for EmailNotification
    The Email sub class
    """

    def send(self,recipient , message):

        #add the recipient
        if recipient not in self.recipients:

            self.recipients.append(recipient)
        
        if message not in self.messages:

            self.messages.append(message)


        return "Sending EMAIL to ",recipient , ":"  , message



class PushNotification(Notification):
    """
    Docstring for PushlNotification
    The Push sub class
    """

    def send(self,recipient , message):

        #add the recipient
        if recipient not in self.recipients:

            self.recipients.append(recipient)
        
        if message not in self.messages:

            self.messages.append(message)


        return "Sending Push notifications to ",recipient , ":"  , message





if __name__ == "__main__":

    sms = SMSNotification()
    print(sms.send("+123456789", "Hello"))
    print(sms.log_notification("+123456789"))


    email = EmailNotification()
    print(email.send("abc@example.com" , "Hello"))
    print(sms.log_notification("+123456789"))

    push = PushNotification()
    print(push.send("user123","Hello"))
    print(push.log_notification("+123456789"))
          

