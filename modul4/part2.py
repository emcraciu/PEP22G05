# # variables in functions
#
# # global variables in functions
#
# my_var = "Emanuel"
#
# def print_data():
#     global my_var
#     my_var = 'NewName'
#     my_local = 'Local'
#     print(f'Global {my_var}')
#     def new_print_data():
#         nonlocal my_local
#         my_local = 'Modified Local'
#         print(f'In second function local {my_local}')
#         print(f'In second function {my_var}')
#     new_print_data()
#     print(f'Local var in first function {my_local}')
#
# print(f'outside Global {my_var}')
# print_data()
# print(f'outside Global {my_var}')
#
# """
# Crate app that is able to respond with the provided name
#
# Hi Bob,
# >>> My name is Jhon
# Hi Jhon
#
# How is the weather
# >>> The weather is cold
#
# For Jhon weather is cold
#
#
#
# All of this will be in a function .
# """

# my_tuple = (1, 2, 3)
# print(my_tuple)
#
# my_tuple = 1, 2, 3
# print(type(my_tuple))
#
# my_tuple = 1,
# print(type(my_tuple))
#
# a = 5
# b = 3
# a, b = b, a
# print(a, b)
#
# # unpack variables in tuple
#
# a = 5
# b = 3
# c = 7
# d = 11
# # f = 13
# a, *var, d = d, c, b, a
# print(a, d)
# print(var)
#
#
# def test_function(*args, **kwargs):
#     print('Args:', args)
#     print('Kwargs:', kwargs)
#
#
# test_function(1, 2, 3, 4, 5, {'1': 2}, end='\n', next=(123,))
# #test_function(1, 2, 3, 4, 5, *(6, 7), **{'a': 2}, end='\n', next=(123,))

# exception

# print(1 / 0)


def div(number1, number2):
    result = 'infinit'
    try:
        result = number1 / number2
    except TypeError:
        print('not possible for string')
        # return None
        result = None
    except ZeroDivisionError:
        print('not possible do divide by 0')
    except:
        raise
    return result


print(div(1, 0))
print(div('1', 10))
