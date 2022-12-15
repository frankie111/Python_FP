import pickle

from lab5.models.CookedDish import CookedDish
from lab5.repository.formatters.DataFormatter import DataFormatter


class CookedDishFormatter(DataFormatter):
    def __init__(self, file=None):
        super().__init__(file)

    def convert_to_string(self, cooked_dish_list):
        return pickle.dumps(cooked_dish_list)

    def convert_from_string(self, string):
        return [] if len(string) == 0 else pickle.loads(string)
