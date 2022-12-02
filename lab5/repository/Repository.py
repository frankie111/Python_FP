from enum import Enum


class Repository:
    """
    An abstract class to be inherited by all repository implementations
    """

    def __init__(self, db_root="repository/database"):
        self.__db_root = db_root
        # self.__menu = db_root + "/menu"
        # self.__cooked_dishes = self.__menu + "/cooked_dishes.txt"
        # self.__drinks = self.__menu + "/drinks.txt"
        # self.__orders = db_root + "/orders/orders.txt"

    @property
    def db_root(self):
        return self.__db_root

    @db_root.setter
    def db_root(self, db_root):
        self.__db_root = db_root

    def add(self, obj):
        pass

    def remove(self, obj):
        pass

    def update(self, obj, updated_obj):
        pass

    def find(self):
        pass

    def get_all(self):
        pass

    class Result(Enum):
        SUCCESS = 1
        ALREADY_EXISTS = 2
        NOT_FOUND = 3
