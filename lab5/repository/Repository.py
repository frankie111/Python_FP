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

    def add(self, obj):
        pass

    def remove(self, obj):
        pass

    def find(self):
        pass

    def update(self, obj, updated_obj):
        pass
