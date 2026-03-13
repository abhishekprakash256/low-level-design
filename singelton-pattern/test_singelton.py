"""
The file to use the singelton
"""


from basic_singelton_pattern import singelton_class , singelton_class_fixed


print(singelton_class.test_func("hello"))

print(singelton_class.test_func("Hey"))

print(singelton_class.test_func("hello") == singelton_class.test_func("Hey"))

print(singelton_class_fixed.test_func())

print(singelton_class_fixed.test_func() == singelton_class_fixed.test_func())