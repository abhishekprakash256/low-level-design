"""
The file to use the singelton
"""


from basic_singelton_pattern import singelton_class , singelton_class_fixed

from singelton_pattern_designs import SingletonInstance ,SingletonDecorator , SingletonThreading


print(singelton_class.test_func("hello"))

print(singelton_class.test_func("Hey"))

print(singelton_class.test_func("hello") == singelton_class.test_func("Hey"))

print(singelton_class_fixed.test_func())

print(singelton_class_fixed.test_func() == singelton_class_fixed.test_func())


#create the singelton pattern

singelton_instance = SingletonInstance()

singelton_instance2 = SingletonInstance()

print(singelton_instance == singelton_instance2)


#using the decorator
@SingletonDecorator
class Database:
    pass

db1 = Database()
db2 = Database()

print(db1 is db2)


singelton_thread = SingletonThreading()

singelton_thread2 = SingletonThreading()

print(singelton_thread == singelton_thread2)