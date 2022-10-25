parola = 7788
b = range(3)
for i in b:
    a = int(input('Introduceti o parola: '))
    if (a == parola):
        print('Acces permis')
        break
    else:
        print('Parola gresita. mai incercati.')
else:
    print('Acccount locked')
 ### version 2
i = 0
while i < 3:
    passw = input("Introduceti parola:")
    if passw == "7788":
        print("Access permis!")
        break
    else:
        print("Parola gresita. Mai incercati.")
        i += 1
else:
    print("PC-ul este blocat pentru urmatoarele 30 minute!!!")
