class Auto:
    def __init__(self, marke, modell, preis):
        self.marke = marke
        self.modell = modell
        self.preis = preis
        self.sold = False

    def start(self):
        print("VROOM VROOM")


class Client:
    def __init__(self, name, sum):
        self.name = name
        self.sum = sum

    def buy(self, auto):
        if self.sum >= auto.preis and not auto.sold:
            self.sum -= auto.preis
            auto.sold = True

        raise AttributeError("cannot buy")


class Autohaus:
    def __init__(self):
        self.autos = []

    def add(self, auto):
        self.autos.append(auto)

    def sell(self, person, idx):
        person.buy(self.autos[idx])


bob = Client("Bob", 200)
auto1 = Auto("ma-ta", "bun-ta", 11)
