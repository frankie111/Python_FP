from lab5.models.Identifiable import Identifiable


class Client(Identifiable):
    def __init__(self, id_, name, address):
        super().__init__()
        self.__id = id_
        self.__name = name
        self.__address = address

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
