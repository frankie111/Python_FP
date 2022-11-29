from lab5.models.Identifiable import Identifiable


class Meal(Identifiable):
    def __init__(self):
        super().__init__()
        self.__portion_size = None
        self.__price = None

    @property
    def portion_size(self):
        return self.__portion_size

    @portion_size.setter
    def portion_size(self, portion_size):
        self.__portion_size = portion_size

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
