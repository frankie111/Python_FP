class Identifiable:

    def __init__(self, id_=None):
        self.__id = id_

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_
