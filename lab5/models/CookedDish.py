from lab5.models.Dish import Dish


class CookedDish(Dish):
    def __init__(self, id_=None, name=None, portion_size=None, price=None, prep_time=None, dict_=None):
        super().__init__(id_, name, portion_size, price)
        self.__prep_time = prep_time
        if dict_ is not None:
            self.__dict__ = dict_

    def __eq__(self, other):
        return super().__eq__(other) and self.__prep_time == other.__prep_time

    def __str__(self):
        return super().__str__() + f", Zubereitungszeit = '{self.__prep_time}'"

    @property
    def prep_time(self):
        return self.__prep_time

    @prep_time.setter
    def prep_time(self, prep_time):
        self.__prep_time = prep_time
