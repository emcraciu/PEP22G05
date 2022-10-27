# # continue keyword
#
# my_str = 'abcdefg'
#
# # for letter in my_str:
# #     print("before continue")
# #     if letter == 'd':
# #         continue  # this will stop current iteration
# #     if letter == 'f':
# #         break  # this will stop for loop
# #     print(letter)
#
# # else keyword
#
# for letter in my_str:
#     print("before continue")
#     if letter == 'd':
#         continue  # this will stop current iteration
#     # if letter == 'f':
#     #     break  # this will stop for loop
#     print(letter)
# else:
#     print('all is done') # this will never get executed if break is encountered
#
# my_number = 0
#
# while my_number < 5:
#     print(my_number)
#     if my_number == 3:
#         break
#     my_number += 1
# else:
#     print('all done while')


# # Lists
# my_var = 3.3
# my_list = ['a', 1, True, my_var]
#
# my_list.__iter__()
#
# for obj in my_list:
#     print(obj)
#
# print('adding to list')
# my_list.append([])
#
# for obj in my_list:
#     print(obj)
#
# print(f'first object is: {my_list[0]}')
# print(f'second object is: {my_list[1]}')
# print(f'third object is: {my_list[2]}')
# print(f'forth object is: {my_list[3]}')
# print(f'fifth object is: {my_list[-1]}')
#
# print('Response is :', my_list.extend([1, 2, 3]))  # but initial object is modified
#
# for obj in my_list:
#     print(obj)
#
# print(my_list)

# modifying object

# a = "name: {}"
# print(f"Initial ID: {id(a)}")
# result = a.format('abcd')
# print("Identity of objects: ", id(a), id(result))
# print(a)
#
# b = ["name: {}"]
# print(f"Initial ID: {id(b)}")
# result = b.append('abcd')
# print("Identity of objects: ", id(b), id(result))
# print(b)  # lists are mutable

# mutable objects in modifying for loops

my_new_list = list('random')

# for letter in my_new_list:
#     my_new_list.append('a')
#     print(letter)

# for letter in my_new_list:
#     my_new_list.pop()
#     print(letter)

# for letter in my_new_list.copy(): # copy of the list
#     my_new_list.pop()
#     print(letter)
#
# print(my_new_list)

# Dictionary

empty_dict = {}
my_dict = {'key1': 'value1', 1: True, 3.14: ['Py']}
print(my_dict)
my_dict['1'] = False
print(my_dict)
my_dict[1] = "False"
print(my_dict)

# Dictionary methods
result = my_dict.pop(1)
print(result)
print(my_dict)

my_dict.update({'key1': 'value3', 'key2': 'value2'})
print(my_dict)

my_dict.__iter__()

for item in my_dict:  # keys are iterated
    print(item)

print("listing values")

for item in my_dict.values():  # values are iterated
    print(item)

print("listing keys")
for item in my_dict.keys():  # keys are iterated
    print(item)

print("listing items")
for item in my_dict.items():  # items are iterated
    print(item)

print("listing items")
for item in my_dict.items():  # items are iterated
    print(item)

print("listing items in separate variables")
for key, value in my_dict.items():  # items are iterated
    print(f"key {key}, value {value}")

