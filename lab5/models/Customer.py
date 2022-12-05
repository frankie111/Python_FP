from lab5.models.Identifiable import Identifiable


class Customer(Identifiable):
    def __init__(self, id_=0, name=None, address=None, dict_=None):
        super().__init__(id_)
        self.__name = name
        self.__address = address
        if dict_ is not None:
            self.__dict__ = dict_

    def __eq__(self, other):
        return self.__name == other.__name and self.__address == other.__address

    def __str__(self):
        return f"Name = '{self.__name}', Adresse = '{self.__address}'"

    def __hash__(self):
        return hash(self.__str__())

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
