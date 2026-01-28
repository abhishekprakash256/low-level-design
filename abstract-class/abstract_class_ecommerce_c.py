"""
Docstring for abstract-class.abstract_class_ecommerce_c
The correct version of the ecommerce class paymnet problem
"""





from abc import ABC, abstractmethod


class OrderProcessor(ABC):
    """
    Abstract base class for ecommerce order processing
    """

    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    # -------- TEMPLATE METHOD --------
    def process_order(self):
        self.validate_order()
        self.calculate_total()
        self.apply_discount()
        self.process_payment()
        self.generate_invoice()

    # -------- ABSTRACT METHODS --------
    @abstractmethod
    def validate_order(self):
        pass

    @abstractmethod
    def calculate_total(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass

    # -------- HOOK METHOD --------
    def apply_discount(self):
        pass

    # -------- SHARED METHOD --------
    def generate_invoice(self):
        print(f"Invoice | Order ID: {self.order_id} | Amount: {self.amount}")







class DigitalOrder(OrderProcessor):
    """
    Payment for digital goods
    """

    def validate_order(self):
        print("Validating digital order (no shipping required)")

    def calculate_total(self):
        self.shipping_order()

    def shipping_order(self):
        shipping_amount = 0
        self.amount += shipping_amount

    def apply_discount(self):
        print("Applying digital discount")
        self.amount *= 0.9

    def process_payment(self):
        print("Processing digital payment")




class PhysicalOrder(OrderProcessor):
    """
    Payment for physical goods
    """

    def validate_order(self):
        self.address_validation()

    def calculate_total(self):
        self.shipping_order()

    def shipping_order(self):
        shipping_cost = 50
        self.amount += shipping_cost

    def address_validation(self):
        print("Validating shipping address")

    def process_payment(self):
        print("Processing physical order payment")




class InternationalOrder(PhysicalOrder):
    """
    Payment for international orders
    """

    def calculate_total(self):
        self.shipping_order()
        self.add_custom_duty()

    def add_custom_duty(self):
        custom_duty = 10
        international_tax = 30
        self.amount += custom_duty + international_tax

    def apply_discount(self):
        print("Applying international tax")
        self.amount *= 1.05





if __name__ == "__main__":

    print("---- DIGITAL ORDER ----")
    digital_order = DigitalOrder("D001", 100)
    digital_order.process_order()

    print("\n---- PHYSICAL ORDER ----")
    physical_order = PhysicalOrder("P001", 200)
    physical_order.process_order()

    print("\n---- INTERNATIONAL ORDER ----")
    international_order = InternationalOrder("I001", 300)
    international_order.process_order()

        




