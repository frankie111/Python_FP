from lab5.repository.Repository import Repository
from lab5.repository.formatters.OrderFormatter import OrderFormatter


class OrderRepository(Repository):

    def __init__(self, path):
        super().__init__(OrderFormatter(path))
