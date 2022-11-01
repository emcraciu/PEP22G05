def calc():
    data = {}
    for i in range(1, 4):
        user = input(f"introduceti utilizatorul pc:{i}")
        parola = input(f"introduceti parola pc:{i}")
        data[user] = parola
        # data.update({user: parola})
    for key, value in data.items():
        print(f"{key} -> {value}")


calc()
