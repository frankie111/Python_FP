from lab5.models.Dish import Dish


class CookedDish(Dish):
    def __init__(self, id_=None, portion_size=None, price=None, prep_time=None, dict_=None):
        super().__init__(id_, portion_size, price)
        self.__prep_time = prep_time
        if dict_ is not None:
            self.__dict__ = dict_

    @property
    def prep_time(self):
        return self.__prep_time

    @prep_time.setter
    def prep_time(self, prep_time):
        self.__prep_time = prep_time
