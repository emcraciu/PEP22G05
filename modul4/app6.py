def function():
    my_numbers = []
    print('Introduceti numere. Cand sunteti gata, introduceti x.')
    while True:
        try:
            data = int(input('Numar:'))
            my_numbers.append(data)
        except ValueError:
            break
    option = input("""Meniu:
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire
Introduceti optiunea dvs: """)

    def suma(lista: list):
        pass


    def medie(lista: list):
        pass


    def putere(lista: list):
        pass

    meniu = {
        "1": medie,
        "2": suma,
        "3": putere
    }
    result = meniu[option](my_numbers)
    print(f'Rezultatul: {result}')
function()