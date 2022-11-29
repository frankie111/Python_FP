from functools import reduce

from lab5.models.Identifiable import Identifiable


class Order(Identifiable):
    def __init__(self, client_id=None, meals=None):
        super().__init__()
        self.__client_id = client_id
        self.__meals = meals
        self.__total_price = None

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, client_id):
        self.__client_id = client_id

    @property
    def meals(self):
        return self.__meals

    @meals.setter
    def meals(self, meals):
        self.__meals = meals

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price):
        self.__total_price = total_price

    def compute_total_price(self):
        price = reduce(lambda a, b: a + b, self.__meals)
