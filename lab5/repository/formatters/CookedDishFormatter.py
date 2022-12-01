import json

from lab5.models.CookedDish import CookedDish
from lab5.repository.formatters.DataFormatter import DataFormatter


class CookedDishFormatter(DataFormatter):
    def __init__(self, file=None):
        super().__init__(file)

    def convert_to_string(self, cooked_dish_list):
        return json.dumps(list(map(lambda dish: dish.__dict__, cooked_dish_list)), indent=4)

    def convert_from_string(self, string):
        dish_dicts = json.loads(string)
        return list(map(lambda dish_dict: CookedDish(dict_=dish_dict), dish_dicts))
