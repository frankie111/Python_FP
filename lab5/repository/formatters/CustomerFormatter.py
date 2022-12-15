import pickle

from lab5.repository.formatters.DataFormatter import DataFormatter


class CustomerFormatter(DataFormatter):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, customer_list):
        return pickle.dumps(customer_list)

    def convert_from_string(self, string):
        return [] if len(string) == 0 else pickle.loads(string)