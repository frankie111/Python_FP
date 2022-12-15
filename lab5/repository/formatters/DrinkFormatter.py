import pickle

from lab5.repository.formatters.DataFormatter import DataFormatter


class DrinkFormatter(DataFormatter):
    def __init__(self, file=None):
        super().__init__(file)

    def convert_to_string(self, drink_list):
        return pickle.dumps(drink_list)

    def convert_from_string(self, string):
        return [] if len(string) == 0 else pickle.loads(string)
