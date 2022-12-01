from lab5.models.Dish import Dish


class Drink(Dish):
    def __init__(self, id_=None, portion_size=None, price=None, alcohol_content=None, dict_=None):
        super().__init__(id_, portion_size, price)
        self.__alcohol_content = alcohol_content
        if dict_ is not None:
            self.__dict__ = dict_

    @property
    def alcohol_content(self):
        return self.__alcohol_content

    @alcohol_content.setter
    def alcohol_content(self, alcohol_content):
        self.__alcohol_content = alcohol_content
