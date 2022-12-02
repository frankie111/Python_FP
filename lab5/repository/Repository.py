from enum import Enum


class Repository:
    """
    An abstract class to be inherited by all repository implementations
    """

    def __init__(self, formatter, db_root="repository/database"):
        self.__db_root = db_root
        self.__formatter = formatter
        # self.__menu = db_root + "/menu"
        # self.__drinks = self.__menu + "/drinks.txt"
        # self.__orders = db_root + "/orders/orders.txt"

    @property
    def db_root(self):
        return self.__db_root

    @db_root.setter
    def db_root(self, db_root):
        self.__db_root = db_root

    def add(self, obj):
        obj_list = self.__formatter.load()

        if obj_list == -1:
            self.__formatter.save([obj])
            return Repository.Result.SUCCESS

        if obj not in obj_list:
            next_id = obj_list[-1].id + 1
            obj.id = next_id
            obj_list.append(obj)
            self.__formatter.save(obj_list)
            return Repository.Result.SUCCESS
        else:
            return Repository.Result.ALREADY_EXISTS

    def remove(self, obj):
        obj_list = self.__formatter.load()

        if obj_list == -1:
            return Repository.Result.NOT_FOUND

        new_list = list(filter(lambda o: o != obj, obj_list))

        if len(new_list) != len(obj_list):
            self.__formatter.save(new_list)
            return Repository.Result.SUCCESS
        else:
            return Repository.Result.NOT_FOUND

    def update(self, obj, updated_obj):
        obj_list = self.__formatter.load()
        lis = list(filter(lambda o: o == obj, obj_list))

        if len(lis) > 0:
            o = lis[0]

            for attr in dir(updated_obj):
                if getattr(updated_obj, attr) is not None:
                    obj.attr = updated_obj.attr

                

    def find(self):
        pass

    def get_all(self):
        pass

    class Result(Enum):
        SUCCESS = 1
        ALREADY_EXISTS = 2
        NOT_FOUND = 3
