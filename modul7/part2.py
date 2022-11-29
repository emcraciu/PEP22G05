class A():
    attr1 = 'my_text'
    attr2 = 10


a = A()
# print(a.__repr__())
print(dir(a))
# check attribute exists
print(hasattr(a, "attr1"))
print(hasattr(a, "attr3"))

# get value from attribute
print(getattr(a, "attr3", "abcd"))
print(getattr(a, "attr2", "abcd"))

# setting and attribute
for i in range(100):
    setattr(a, f"attr{i}", f"{i+1}")

print(dir(a))
print(a.attr1)
print(a.attr2)

print(a.__setattr__("new_attr", "100"))
# print(a.new_attr)
print(a.__getattribute__("new_attr"))

# Create object and set attributes from input


class A:
    attr_A = 'A'
    custom = "my_custom_text"

class B(A):
    attr_B = 'B'
    custom = 1

class C(B):
    attr_C = 'C'
    custom = 10

a = A()
b = B()
print(b.attr_A)
print(b.attr_B)
c = C()
print(c.attr_A)
print(c.attr_B)
print(c.attr_C)
print(c.custom)