from lab5.controller.CustomerController import CustomerController
from lab5.controller.MenuController import MenuController
from lab5.controller.OrderController import OrderController
from lab5.repository.CookedDishRepository import CookedDishRepository
from lab5.repository.CustomerRepository import CustomerRepository
from lab5.repository.DrinkRepository import DrinkRepository
from lab5.repository.OrderRepository import OrderRepository
from lab5.ui.UIController import menu, invalid


class Controller:
    def __init__(self, db_root="repository/database/"):
        self.__customer_repo = CustomerRepository(f"{db_root}customers/customers.pickle")
        self.__order_repo = OrderRepository(f"{db_root}orders/orders.pickle")
        self.__cooked_dish_repo = CookedDishRepository(f"{db_root}menu/cooked_dishes.pickle")
        self.__drink_repo = DrinkRepository(f"{db_root}menu/drinks.pickle")

        self.customer_controller = CustomerController(self.__customer_repo)
        self.menu_controller = MenuController(self.__drink_repo, self.__cooked_dish_repo)
        self.order_controller = OrderController(self.__customer_repo, self.__order_repo, self.__cooked_dish_repo,
                                                self.__drink_repo)

    def run(self):
        """
        The main method of Controller
        """
        self.main_menu()

    def main_menu(self):
        """
        The main menu of the application
        """
        opt = menu("Restaurant Verwaltung app", ["Bestellungen", "Speisekarte", "Kunden", "<-Exit"])
        if not opt.isnumeric():
            invalid()
            self.main_menu()

        opt = int(opt)

        match opt:
            case 1:
                self.order_controller.menu()
                self.main_menu()
            case 2:
                self.menu_controller.menu()
                self.main_menu()
            case 3:
                self.customer_controller.menu()
                self.main_menu()
            case 4:
                # Exit program
                pass
            case _:
                invalid()
                self.main_menu()
