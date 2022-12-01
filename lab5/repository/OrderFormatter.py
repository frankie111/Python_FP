import json

from lab5.models.Order import Order
from lab5.repository.DataFormatter import DataFormatter


class OrderFormatter(DataFormatter):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, order_list):
        return json.dumps(list(map(lambda order: order.__dict__, order_list)), indent=4)

    def convert_from_string(self, string):
        order_dicts = json.loads(string)
        return list(map(lambda order_dict: Order(dict_=order_dict), order_dicts))
