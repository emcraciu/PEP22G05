def factorial(limit):
    result = 1
    for i in range(1, limit + 1):
        result *= i
    return result


print('Print from module', factorial(5))
