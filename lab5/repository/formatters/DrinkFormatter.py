import json

from lab5.models.Drink import Drink
from lab5.repository.formatters.DataFormatter import DataFormatter


class DrinkFormatter(DataFormatter):
    def __init__(self, file=None):
        super().__init__(file)

    def convert_to_string(self, drink_list):
        return json.dumps(list(map(lambda drink: drink.__dict__, drink_list)), indent=4)

    def convert_from_string(self, string):
        drink_dicts = json.loads(string)
        return list(map(lambda drink_dict: Drink(dict_=drink_dict), drink_dicts))
