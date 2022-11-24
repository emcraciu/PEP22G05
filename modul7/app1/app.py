class Haine:
    nume = ""
    pret = 0
    stoc = 0

    def __init__(self, nume, pret, stoc, **kwargs):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc

    def __str__(self):
        f = f"\n {20 * '='}" \
            f"\n{self.__class__.__name__} " \
            f"\n {20 * '='}" \
            f"\n Nume = {self.nume} " \
            f"\n Pret = {self.pret} " \
            f"\n Stoc = {self.stoc}" \
            f"\n {20 * '-'}"
        return f


class Accesorii:

    def __init__(self, nume, pret, stoc, material='aur', **kwargs):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc
        self.material = material

    def __str__(self):
        f = f"\n {20 * '='}" \
            f"\n{self.__class__.__name__} " \
            f"\n {20 * '='}" \
            f"\n Nume = {self.nume} " \
            f"\n Pret = {self.pret} " \
            f"\n Stoc = {self.stoc}" \
            f"\n Material = {self.material}" \
            f"\n {20 * '-'}"
        return f


if __name__ == '__main__':
    bratara = Accesorii('Test', 'aur', 100, 50)
    bluze = Haine("bluze", 10, 5)
    print(bluze.pret)
    print(bratara.material)
    print(bluze)
    print(bratara)
