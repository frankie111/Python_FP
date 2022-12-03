from lab5.repository.Repository import Repository
from lab5.repository.formatters.DrinkFormatter import DrinkFormatter


class DrinkRepository(Repository):

    def __init__(self, path):
        super().__init__(DrinkFormatter(path))
