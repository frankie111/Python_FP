from enum import Enum

from lab5.models.Identifiable import Identifiable


class Repository:
    def __init__(self, formatter):
        self.__formatter = formatter

    def add(self, obj):
        """
        Adds an object to the database
        :param obj:
        :returns: The result of the operation as Repository.Result
        """
        obj_list = self.__formatter.load()
        obj.id = obj.__hash__()

        if obj_list == -1:
            self.__formatter.save([obj])
            return Repository.Result.SUCCESS

        if obj not in obj_list:
            obj_list.append(obj)
            self.__formatter.save(obj_list)
            return Repository.Result.SUCCESS
        else:
            return Repository.Result.ALREADY_EXISTS

    def add_list(self, objects):
        """
        Adds a list of objects to the database
        :param objects:
        :returns: The result of the operation as Repository.Result
        """
        obj_list = self.__formatter.load()
        result = Repository.Result.SUCCESS

        if obj_list == -1:
            for obj in objects:
                obj.id = obj.__hash__()
            self.__formatter.save(objects)
            return result

        for obj in objects:
            if obj not in obj_list:
                obj.id = obj.__hash__()
                obj_list.append(obj)
            else:
                result = Repository.Result.ALREADY_EXISTS
        self.__formatter.save(obj_list)
        return result

    def remove(self, obj):
        """
        Removes an object from the database
        :param obj:
        :returns: The result of the operation as Repository.Result
        """
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
        """
        Updates an object in the database
        :param obj: The object to be updated
        :param updated_obj: An object with the updated properties
        :returns: The result of the operation as Repository.Result
        """
        assert type(obj) == type(updated_obj)
        obj_list = self.__formatter.load()
        lis = list(filter(lambda o: o == obj, obj_list))
        if len(lis) > 0:
            # Copy attributes of updated_obj if not None:
            attr_list = list(filter(lambda a: '_' not in a and a != 'id', dir(updated_obj)))
            for attr in attr_list:
                attr_val = getattr(updated_obj, attr)
                if attr_val is not None:
                    setattr(lis[0], attr, attr_val)

            self.__formatter.save(obj_list)
            return Repository.Result.SUCCESS

        return Repository.Result.NOT_FOUND

    def search(self, obj:Identifiable):
        """
        Returns a list of matching objects from the database
        filters the database by part of the first not None attribute of obj
        :param obj:
        :returns: A filtered list of objects
        """
        obj_list = self.__formatter.load()

        for attr in dir(obj):
            if getattr(obj, attr) is not None:
                if type(attr) is str:
                    filtered = list(filter(lambda o: getattr(obj, attr).lower() in getattr(o, attr).lower(), obj_list))
                    return filtered
                else:
                    filtered = list(filter(lambda o: getattr(obj, attr) == getattr(o, attr), obj_list))
                    return filtered

        return []

    def get_all(self):
        """
        Returns a list of all objects from the database
        :return:
        """
        obj_list = self.__formatter.load()
        return obj_list if obj_list != -1 else []

    class Result(Enum):
        SUCCESS = 1
        ALREADY_EXISTS = 2
        NOT_FOUND = 3
