class Identifiable:

    def __init__(self):
        self.__id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_
