from lab5.models.Meal import Meal


class CookedMeal(Meal):
    def __init__(self, id_, portion_size, price, prep_time):
        super().__init__()
        self.__id = id_
        self.__portion_size = portion_size
        self.__price = price
        self.__prep_time = prep_time

    @property
    def prep_time(self):
        return self.__prep_time

    @prep_time.setter
    def prep_time(self, prep_time):
        self.__prep_time = prep_time
