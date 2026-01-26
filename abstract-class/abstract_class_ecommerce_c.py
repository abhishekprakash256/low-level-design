"""
Docstring for abstract-class.abstract_class_ecommerce_c
The correct version of the ecommerce class paymnet problem
"""


from abc import ABC, abstractmethod


class OrderProcessor(ABC):
    """
    Docstring for OrderProcessor
    The order processor class for payment for ecommerce
    """

    def __init__(self,order_id, amount):

        self.order_id = order_id
        self.amount = amount

    @abstractmethod
    def validate_order(self):

        pass


    @abstractmethod
    def calculate_total(self):

        pass

    @abstractmethod
    def process_payment(self):

        pass

    def apply_discount(self):
        
        pass

    def generate_invoice(self):

        pass


    def process_order(self):
        """
        Docstring for process_order
        The Template method for the steps
    
        :param self: Description
        """

        self.validate_order()

        self.calculate_total()

        self.apply_discount()

        self.process_payment()

        self.generate_invoice()








