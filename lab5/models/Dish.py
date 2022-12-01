from lab5.models.Identifiable import Identifiable


class Dish(Identifiable):
    def __init__(self, id_=None, portion_size=None, price=None):
        super().__init__(id_)
        self.__portion_size = portion_size
        self.__price = price

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
