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

        return "Printing Invoice"


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







class DigitalOrder(OrderProcessor):
    """
    Docstring for DigitalOrder
    The DigitalOrder class for payment of digital goods
    """

    def shipping_order(self):

        shipping_amount = 0

        self.amount = shipping_amount + self.amount
 

    def apply_discount(self):

        self.amount = self.amount * 0.9



class PhysicalOrder(OrderProcessor):

    def shipping_order(self):

        shipping_cost = 50

        #check the address
        self.address_validation()

        self.amount = shipping_cost + self.amount


    def address_validation(self):

        pass



class InternationalOrder(PhysicalOrder):

    def shipping_order(self):

        custom_duty = 10

        international_tax = 30

        self.amount = custom_duty + international_tax + self.amount





if __name__ == "main":

    #digital_order 
    digital_order = DigitalOrder()

    print(digital_order.shipping_order())
        




