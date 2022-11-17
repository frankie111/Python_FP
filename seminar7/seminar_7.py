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


def main():
    dacia = Auto("marke", "modell", "baujahr", "farbe")
    stats = Statistics()
    stats.add_auto(dacia)
