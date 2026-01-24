"""
The correct implenetation of the abstract class
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Abstract base class for all notifications
    """

    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def log_notification(self):
        """
        Concrete method shared by all notifications
        """
        print(f"Notification sent to {self.recipient}")

    @abstractmethod
    def send(self):
        """
        Abstract method that must be implemented by subclasses
        """
        pass


class SMSNotification(Notification):
    def send(self):
        print(f"Sending SMS to {self.recipient}: {self.message}")


class EmailNotification(Notification):
    def send(self):
        print(f"Sending EMAIL to {self.recipient}: {self.message}")


class PushNotification(Notification):
    def send(self):
        print(f"Sending PUSH to {self.recipient}: {self.message}")


if __name__ == "__main__":
    sms = SMSNotification("+123456789", "Hello")
    sms.send()
    sms.log_notification()

    email = EmailNotification("abc@example.com", "Hello")
    email.send()
    email.log_notification()

    push = PushNotification("user123", "Hello")
    push.send()
    push.log_notification()
