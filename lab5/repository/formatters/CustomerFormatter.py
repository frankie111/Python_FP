import json

from lab5.models.Customer import Customer
from lab5.repository.formatters.DataFormatter import DataFormatter


class CustomerFormatter(DataFormatter):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, customer_list):
        return json.dumps(list(map(lambda customer: customer.__dict__, customer_list)), indent=4)

    def convert_from_string(self, string):
        customer_dicts = json.loads(string)
        return list(map(lambda customer_dict: Customer(dict_=customer_dict), customer_dicts))
