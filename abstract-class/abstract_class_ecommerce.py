"""
Docstring for abstract-class.abstract_class_ecommerce
Scenario: Order Processing System (E-commerce)

You are building an order processing engine for an e-commerce platform.

Different order types exist:

DigitalOrder (ebooks, subscriptions)

PhysicalOrder (clothes, electronics)

InternationalOrder (customs, duties)

Each order follows a common lifecycle, but some steps differ depending on the order type.
"""
from abc import ABC, abstractmethod


class OrderProcessor(ABC):
    """
    Docstring for OrderProcessor
    The OrderProcessor class has the blue print for the order processing
    """

    def __init__(self, order_id, amount):

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




class DigitalOrder(OrderProcessor):

    def __init__(self):

        self.shipping_cost = False
        
    
    def apply_discount(self):
        
        return "Can apply digital discount"
    


class PhysicalOrder(OrderProcessor):

    def __init__(self):

        self.shipping_cost = True
        
    
    def apply_discount(self):
        
        return "Can apply digital discount"
    


class InternationalOrder(OrderProcessor,PhysicalOrder):

    def __init__(self):
        
        self.custom_duty = True


    def generate_invoice(self):

        return "Add custom Duty"

        