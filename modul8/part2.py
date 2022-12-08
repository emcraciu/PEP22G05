# # File operations
#
# my_stream = open("my_text.txt", mode="w")
# print(type(my_stream))
# my_stream.write("Hello Python")
# my_stream.close()  # also does my_stream.flush()
#
# # with statement
#
# with open("my_text.txt", mode="w") as file:
#     file.write("Hello Python with")
#     # raise BaseException  # close is still called even in case of exception
# with open("my_text.txt", mode="rb") as file:
#     result = file.read()
#
# print(type(result))
# print(result)  # this is a bytes object displaied as text
#

# datetime
import datetime

my_date1 = datetime.datetime(year=2021, month=3, day=11)
my_date2 = datetime.datetime(year=2020, month=5, day=10, minute=32)
print(my_date1)
print(my_date2)
result = my_date1 - my_date2
print(result)
print(type(result))
print(result.days)
print(type(result.days))
print(my_date2.minute)
# get current date
print(datetime.datetime.now())

# compare dates
print(my_date1 > my_date2)


## lambda functions

def a(x, y):
    return x + y


print(a(1, 2))

b = lambda x, y: x + y  # do not do this
print(b(1, 2))


def calcualte(functie, number):
    return functie(number, number)


print(calcualte(a, 9))

print(calcualte(lambda x, y: x + y, 8))
print("#" * 80)
for i in range(100):
    print(calcualte(lambda x, y: x + y + i, 8))

# examples:
print(map(lambda x: x + 1, [2, 3, 4]).__next__())
print(filter(lambda x: x + 1, [2, 3, 4]).__next__())
print("#" * 80)

for i in filter(lambda x: x + 1, [2, -1, 3, -2, 4]):
    print(i)
