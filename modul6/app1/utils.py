# def adaugare_produs(stoc_existent: dict):
#     prod = input("introduceti produs")
#     caract_produs = prod.split(";")
#     if stoc_existent.get(caract_produs[0], False):
#         stoc_existent.update(
#             {
#                 caract_produs[0]: [
#                     float(caract_produs[1]),
#                     stoc_existent[caract_produs[0]][1] + int(caract_produs[2])
#                 ]
#             }
#         )
#
#     else:
#         stoc_existent.update({caract_produs[0]: [float(caract_produs[1]), int(caract_produs[2])]})

def adaugare_produs(stoc_existent: dict):
    name, price, stock = input("introduceti produs").split(";")
    stock = int(stock)
    price = float(price)
    if stoc_existent.get(name, False):
        stoc_nou = stoc_existent[name][1] + stock
        stoc_existent.update({name: [price, stoc_nou]})
    else:
        stoc_existent.update({name: [price, stock]})



def sterge_produs(stoc_existent: dict):
    produs = input("ce produs doresti sa stergi?")
    del stoc_existent[produs]


def vizualizare_stoc(stoc_existent: dict):
    for produs, info in stoc_existent.items():
        print(produs, ":", info[1])


if __name__ == '__main__':
    # vizualizare_stoc({'prod1': [3.5, 10]})
    # sterge_produs({'prod1': [3.5, 10]})
    adaugare_produs({'prd1': [3.5, 10]})
