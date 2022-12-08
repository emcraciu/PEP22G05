# File operations

my_stream = open("my_text.txt", mode="w")
print(type(my_stream))
my_stream.write("Hello Python")
my_stream.close()  # also does my_stream.flush()

# with statement

with open("my_text.txt", mode="w") as file:
    file.write("Hello Python with")
    # raise BaseException  # close is still called even in case of exception
with open("my_text.txt", mode="rb") as file:
    result = file.read()

print(type(result))
print(result)  # this is a bytes object displaied as text
