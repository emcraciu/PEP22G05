### import Module

# import my_functions
# import time
# import math
# import random
# import sys
#
# print(sys.path)
# #sys.path.append('C:\\Users\\ozy24\\PycharmProjects')
# # import modul4.part1  # relative to project root
#
# print(my_functions)
# print(my_functions.factorial(6))
#
# print(type(random))
# result = random.random()
# print(result)
# result = random.randint(1, 5)
# print(result)
#
#
# result = time.time()
# print(result)
#
# time.sleep(1)
#
# from time import sleep
# print('before sleep')
# sleep(5)
# print('after sleep')

from my_functions import factorial

# my_imported_var = 'Local'
# from my_functions import *
# print(my_imported_var)

### import Package

#import my_package
import my_package as new_name

print(type(new_name))
print(new_name.my_var)
print(new_name.factorial(10))