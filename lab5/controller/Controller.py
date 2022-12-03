from lab5.repository.CookedDishRepository import CookedDishRepository
from lab5.repository.CustomerRepository import CustomerRepository
from lab5.repository.DrinkRepository import DrinkRepository
from lab5.repository.OrderRepository import OrderRepository


class Controller:
    def __init__(self, db_root="repository/database/"):
        self.customer_repo = CustomerRepository(f"{db_root}customers/customers.txt")
        self.order_repo = OrderRepository(f"{db_root}orders/orders.txt")
        self.cooked_dish_repo = CookedDishRepository(f"{db_root}menu/cooked_dishes.txt")
        self.drink_repo = DrinkRepository(f"{db_root}menu/drinks.txt")

    def run(self):
        pass