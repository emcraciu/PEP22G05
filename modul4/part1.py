# functions

# # 3! = 1*2*3
# def factorial(number):
#     print(number)
#     result = 1
#     for i in range(1, number + 1):
#         result *= i
#     return result
#
#
# factorial(10)
# # print(result)  # does not exist outside function
#
# result = factorial(10)
# print('Result is :', result)

# 3! = 1*2*3
# def factorial(number, limit):
#     print(number)
#     result = 1
#     for i in range(1, number + 1):
#         if result > limit:
#             return result  # this stops function execution
#         result *= i
#     return result
#
# result = factorial(100, 1000)
# print('Result is :', result)
#

# variable number of arguments
def factorial(*args): # variable number of arguments
    print(args)

factorial(1234,1234)
print(__name__)