from lab5.models.Dish import Dish


class Drink(Dish):
    def __init__(self, id_=None, name=None, portion_size=None, price=None, alcohol_content=None, dict_=None):
        super().__init__(id_, name, portion_size, price)
        self.__alcohol_content = alcohol_content
        if dict_ is not None:
            self.__dict__ = dict_

    def __eq__(self, other):
        return super().__eq__(other) and self.__alcohol_content == other.__alcohol_content

    def __str__(self):
        return super().__str__() + f", Alkoholgehalt = '{self.__alcohol_content}'"

    @property
    def alcohol_content(self):
        return self.__alcohol_content

    @alcohol_content.setter
    def alcohol_content(self, alcohol_content):
        self.__alcohol_content = alcohol_content
