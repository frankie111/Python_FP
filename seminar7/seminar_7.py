from cmath import pi


class Fractie:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def __str__(self):
        return f"{self.n}/{self.m}"

    def extindere(self, k):
        self.n *= k
        self.m *= k

    def simplificare(self, k):
        self.n /= k
        self.m /= k


class Auto:
    def __init__(self, marke, modell, baujahr, farbe):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.farbe = farbe


class Statistics:
    def __init__(self):
        self.autos = []

    def add_auto(self, auto):
        self.autos.append(auto)

    def anzahl_auto_farbe(self, farbe):
        anzahl = 0
        for auto in self.autos:
            if auto.farbe == farbe:
                anzahl += 1

        return anzahl


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, r, c):
        self.r = r  # number
        self.c = c  # list, tuple

    def print(self):
        print(f'radius: {self.r}, center: {self.c}')

    def move(self, dx, dy):
        self.c = (self.c.x + dx, self.c.y + dy)

    def resize(self, k):
        self.r *= k

    def area(self):
        return pi * self.r ** 2


def main():
    c = Circle(10, (1, 2))
    c.print()


main()
