from lab5.controller.CustomerController import CustomerController
from lab5.controller.MenuController import MenuController
from lab5.repository.OrderRepository import OrderRepository
from lab5.ui.UIController import menu, invalid


class Controller:
    def __init__(self, db_root="repository/database/"):
        self.customer_controller = CustomerController(db_root)
        self.menu_controller = MenuController(db_root)
        self.order_repo = OrderRepository(f"{db_root}orders/orders.txt")

    def run(self):
        self.main_menu()

    def main_menu(self):
        opt = menu("Restaurant Verwaltung app", ["Bestellungen", "Speisekarte", "Kunden", "<-Exit"])
        if not opt.isnumeric():
            invalid()
            self.main_menu()

        opt = int(opt)

        match opt:
            case 1:
                self.order_menu()
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

    def order_menu(self):
        pass

    def menu_menu(self):
        pass
