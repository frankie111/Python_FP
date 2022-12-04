from lab5.models.Identifiable import Identifiable


class Dish(Identifiable):
    def __init__(self, id_=None, name=None, portion_size=None, price=None):
        super().__init__(id_)
        self.__portion_size = portion_size
        self.__price = price
        self.__name = name

    def __eq__(self, other):
        return self.__name == other.__name and self.__portion_size == other.__portion_size and self.__price == other.__price

    def __str__(self):
        return f"Name = '{self.__name}', Portionsgröße = '{self.__portion_size}', Preis = '{self.__price}'"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

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
