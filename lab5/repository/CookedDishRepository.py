from lab5.repository.Repository import Repository
from lab5.repository.formatters.CookedDishFormatter import CookedDishFormatter


class CookedDishRepository(Repository):

    def __init__(self, path):
        super().__init__(CookedDishFormatter(path))