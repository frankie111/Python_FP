from lab5.repository.Repository import Repository
from lab5.repository.formatters.CookedDishFormatter import CookedDishFormatter


class CookedDishRepository(Repository):

    def __init__(self, menu="/menu"):
        super().__init__(CookedDishFormatter(self.db_root + menu + "/cooked_dishes.txt"))

    def remove(self, obj):
        super().remove(obj)

    def update(self, obj, updated_obj):
        super().update(obj, updated_obj)

    def find(self):
        super().find()

    def get_all(self):
        super().get_all()
