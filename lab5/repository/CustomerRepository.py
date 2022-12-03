from lab5.repository.Repository import Repository
from lab5.repository.formatters.CustomerFormatter import CustomerFormatter


class CustomerRepository(Repository):

    def __init__(self, path):
        super().__init__(CustomerFormatter(path))
