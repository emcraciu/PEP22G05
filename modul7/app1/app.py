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


class Incaltaminte(Haine):

    def __init__(self, nume, pret, stoc, **kwargs):
        super(Incaltaminte, self).__init__(nume, pret, stoc)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        f = super().__str__()
        for attribute_ in dir(self):
            if "__" in attribute_ or attribute_ in ["name", "pret", "stoc"]:
                continue
            f += f"\n {attribute_} = {getattr(self, attribute_)}"
        return f


class Genti(Incaltaminte):
    pass


if __name__ == '__main__':
    pantofi = Incaltaminte("pantof1", 50, 100, marime=40, material='piele', culoare="black")
    # bratara = Accesorii('Test', 'aur', 100, 50)
    # bluze = Haine("bluze", 10, 5)
    # print(bluze.pret)
    # print(bratara.material)
    # print(bluze)
    # print(bratara)

    print(pantofi)

    genti = Genti("poseta", 50, 100,  material='piele', culoare="black", acesori="nasturi")
    print(genti)
