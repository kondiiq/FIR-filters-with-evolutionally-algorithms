import random

random.seed()


class Osobnik(object):

    def __init__(self):
        for i in range(0, 32):
            self.chromo = [random.randint(0, 1) for i in range(0, 32)]

    def __add__(self, b):
        wynik = Osobnik()
        podz = random.randint(0, 31)
        for key, val in enumerate(b.chromo):
            if key > podz:
                wynik.chromo[key] = self.chromo[key]
            else:
                wynik.chromo[key] = b.chromo[key]
        return wynik

    @property
    def ocena(self):
        return sum(self.chromo)

    def mutuj(self):
        x = Osobnik()
        x.chromo = list(self.chromo)
        index = random.randint(0, 31)
        x.chromo[index] = (x.chromo[index] + 1) % 2
        return x


class Populacja(object):

    def __init__(self):
        self.osobniki = [Osobnik() for i in range(0, 5)]

    def selekcja(self):
        self.osobniki.sort(key=lambda Osobnik: Osobnik.ocena, reverse=True)
        self.osobniki[3] = self.osobniki[0].mutuj()
        self.osobniki[4] = self.osobniki[0] + self.osobniki[1]


x = Populacja()

for i in range(0, 2137):
    print('iteracja nr: {}'.format(i + 1))
    for j in x.osobniki:
        print(j.chromo, j.ocena)
    x.selekcja()