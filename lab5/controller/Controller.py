from lab5.models.Customer import Customer
from lab5.repository.CookedDishRepository import CookedDishRepository
from lab5.repository.CustomerRepository import CustomerRepository
from lab5.repository.DrinkRepository import DrinkRepository
from lab5.repository.OrderRepository import OrderRepository
from lab5.repository.Repository import Repository
from lab5.ui.UIController import menu, header, footer, warning


class Controller:
    def __init__(self, db_root="repository/database/"):
        self.customer_repo = CustomerRepository(f"{db_root}customers/customers.txt")
        self.order_repo = OrderRepository(f"{db_root}orders/orders.txt")
        self.cooked_dish_repo = CookedDishRepository(f"{db_root}menu/cooked_dishes.txt")
        self.drink_repo = DrinkRepository(f"{db_root}menu/drinks.txt")

    def run(self):
        self.main_menu()

    def main_menu(self):
        opt = menu("Restaurant Verwaltung app", ["Bestellungen", "Speisekarte", "Kunden"])
        if not opt.isnumeric():
            warning("ungültige Option")
            self.main_menu()

        opt = int(opt)

        match opt:
            case 1:
                self.order_menu()
            case 2:
                self.menu_menu()
            case 3:
                self.customer_menu()
            case _:
                warning("ungültige Option")
                self.main_menu()

    def order_menu(self):
        pass

    def menu_menu(self):
        pass

    def customer_menu(self):
        opt = menu("Kunden Verwaltung",
                   ["Alle Anzeigen", "Hinzufügen", "Aktualisieren", "Löschen", "Finden", "<-Zurück"])
        if not opt.isnumeric():
            warning("ungültige Option")
            self.customer_menu()

        opt = int(opt)

        match opt:
            case 1:
                self.show_all_customers()
                self.customer_menu()
            case 2:
                self.add_customer()
                self.customer_menu()
            case 3:
                pass
            case 4:
                pass
            case 5:
                self.find_customer()
                self.customer_menu()
            case 6:
                self.main_menu()
            case _:
                print("ungültige Option!")
                self.customer_menu()

    def show_all_customers(self):
        header("Kundenliste")
        for customer in self.customer_repo.get_all():
            print(customer)
        footer("Kundenliste")

    def add_customer(self):
        header("Neuer Kunde")
        name = input("Name=")
        address = input("Adresse=")
        footer("Neuer Kunde")

        new_customer = Customer(name=name, address=address)
        res = self.customer_repo.add(new_customer)
        if res == Repository.Result.SUCCESS:
            print(f"Neuer Kunde hinzugefügt [{new_customer}]")
        elif res == Repository.Result.ALREADY_EXISTS:
            print(f"Der Kunde [{new_customer}] ist bereits vorhanden!")

    def find_customer(self):
        opt = menu("Finde Kunden nach", ["Name", "Adresse"])
        if not opt.isnumeric():
            warning("ungültige Option")
            self.find_customer()

        opt = int(opt)
        customer = Customer()
        match opt:
            case 1:
                name = input("Name=")
                customer.name = name
            case 2:
                address = input("Adresse=")
                customer.address = address
            case _:
                warning("ungültige Option")
                self.find_customer()

        header("Passende Kunden")
        for cus in self.customer_repo.find(customer):
            print(cus)
        footer("Passende Kunden")