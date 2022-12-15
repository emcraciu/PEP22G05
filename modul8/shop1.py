"""
A shop needs an iterable object to keep track of product expiration dates.
Each product in the shop will have a string name, datetime expiration date and quantity
Iterating the object will return all products in the shop ordered by expiration date
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add product to the shop
    d) 10p: Method to decrease quantity and remove product
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Add products:
        - Banana, 1 Aug 2022, 100
        - Orange, 2 Aug 2022, 200
        - Orange, 3 Aug 2022, 50
    c) 10p: Remove products
        - Orange, 10
        - Banana, 50
    d) 10p: Iterate the created object.
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""
import datetime


class ShopIterator:
    """iterator for shop product"""

    def __init__(self, produse: dict):
        self.expiration_dates = []
        for item in produse.items():
            self.expiration_dates.append(item)
        self.expiration_dates.sort(key=lambda x: x[1])

    def __iter__(self):
        return self

    def __next__(self):
        if self.expiration_dates:
            return self.expiration_dates.pop(0)
        else:
            raise StopIteration


class Shop:
    """class for tracking products"""
    inventory = {}

    def __init__(self):
        pass

    def add_product(self, nume, data, cantitate):
        """adding a product"""
        self.inventory.update({nume: [data, cantitate]})

    def remove_product(self, nume, cantitate):
        """removing a product"""
        print(self.inventory[nume][1])
        if self.inventory[nume][1] > cantitate:
            self.inventory[nume][1] -= cantitate
        else:
            del self.inventory[nume]

    def __iter__(self):
        produse = {}
        for key, value in self.inventory.items():
            produse[key] = value[0]

        return ShopIterator(produse)


shop = Shop()
shop.add_product('banane', datetime.datetime(2022, 7, 10), 50)
print(shop.inventory)
shop.remove_product('banane', 10)
print(shop.inventory)
# shop.remove_product('banane', 40)
# print(shop.inventory)
shop.add_product('portocale', datetime.datetime(2022, 2, 5), 70)

with open("examen.txt", "w") as file:
    for item in shop:
        file.write(str(item) + "\n")
