"""
The singelton pattern designs
"""

class SingletonInstance:
    """
    This is detectction of instance using the var and __new__ keyword
    """

    #store the class instance 
    _instance = None

    def __new__(cls):
        """
        The __new__ patten is used to get the instance
        Not using the __init__ to initilaize the object
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
    


def SingletonDecorator(cls):
    """
    The design pattern using the decorator
    """

    #uisng a dict to store the instance
    instances = {}

    #the method to store the instance 
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return get_instance



import threading

class SingletonThreading:
    """
    The singleton pattern using the thread safe
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):

        with cls._lock:

            if cls._instance is None:
                cls._instance = super().__new__(cls)

        return cls._instance