from app import Haine
from app import Accesorii

produse = []
h1 = Haine("Pantaloni", 100, 3)
a1 = Accesorii("Bratara", 100, 4, "argint")
produse.append(h1)
produse.append(a1)


def vizualizare(produse):
    for produs in produse:
        print(produs)


def add_product(produse):
    products = {'1': Haine, '2': Accesorii}
    product_selector = input("What is the category\n 1: Haine\n 2: Accesorii")
    nume = input('nume:')
    pret = int(input('pret:'))
    stoc = int(input('stock:'))
    if product_selector == '2':
        material = input('material:')
    else:
        material = None
    try:
        new_product = Haine(nume, pret, stoc, material=material)
    except:
        print('something is wrong')
    else:
        produse.append(new_product)


def meniu():
    meniu = {"1": add_product, "2": vizualizare, "3": quit}
    while True:
        optiune = input("Optiuni:\n1.Adaugare produs\n2.Vizualizati\n3.Iesire\n").strip()
        try:
            # action = meniu[optiune]
            if optiune == "2":
                meniu[optiune](produse)
            elif optiune == '1':
                meniu[optiune](produse)
        except KeyError:
            print("Incorrect value! try again... ")
        # action()


meniu()
