from lab5.models.CookedDish import CookedDish
from lab5.repository.CookedDishRepository import CookedDishRepository


def add_dish_test():
    initial_dish = CookedDish(0, "Papara", 450, 12, 15)
    repo = CookedDishRepository("cooked_dishes.txt")
    repo.clear()
    repo.add(initial_dish)

    read_dish = repo.get_all()[0]
    assert initial_dish == read_dish


add_dish_test()
