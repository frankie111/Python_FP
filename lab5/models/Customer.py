from lab5.models.Identifiable import Identifiable


class Customer(Identifiable):
    def __init__(self, id_=None, name=None, address=None, dict_=None):
        super().__init__(id_)
        self.__name = name
        self.__address = address
        if dict is not None:
            self.__dict__ = dict_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
