# Output functions
print('Hello World')

# Input functions
# input('Say Hello: ')

# Variables
my_name = 'Emanuel'
print(my_name)
my_number = 1_000_000
print(my_number)

# type function
result = type(10)
print(result)

# return of print
result = print('example')
print(result)

# return of input
result = input('Say Hello: ')
print(result)

# print multiple args
print('Emanuel', 'Ion', 'Illia')

# casting
# result = 'abcd'
# result = int(result)
# print(result)

result = 10  # comment
result = str(result)
print(type(result))

# Operatii

# comparison
a = 100
b = 100
print(a == b)
print('ID of a is:', id(a))
print('ID of b is:', id(b))
print(a is b)

a = "/////////////////abcd"*4100 + "/////////////////abcd$%^*" + "/////////////////abcd$%^*"
print(a)
b = "/////////////////abcd"*4100 + "/////////////////abcd$%^*" + "/////////////////abcd$%^*"
print(a == b)
print('ID of a is:', id(a))
print('ID of b is:', id(b))
print(a is b)

# slice
    #0123456
a = 'my_text'
print(a[1])
print(a[1:3])
print(a[1:6])
print(a[1:])
print(a[:6])
print(a[:6:3])

    #-7-6-5-4-3-2-1
#a  ' m y _ t e x t'
a = 'my_text'
print(a[-1])
print(a[-6:-1])
print(a[-1:-6:-3])

b = 'This is may reversed text'

