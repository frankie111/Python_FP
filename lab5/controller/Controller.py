from lab5.models.Customer import Customer
from lab5.repository.CookedDishRepository import CookedDishRepository
from lab5.repository.CustomerRepository import CustomerRepository
from lab5.repository.DrinkRepository import DrinkRepository
from lab5.repository.OrderRepository import OrderRepository
from lab5.repository.Repository import Repository
from lab5.ui.UIController import menu, header, footer, warning, invalid


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
            invalid()
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
                invalid()
                self.main_menu()

    def order_menu(self):
        pass

    def menu_menu(self):
        pass

    def customer_menu(self):
        opt = menu("Kunden Verwaltung",
                   ["Alle Anzeigen", "Hinzufügen", "Aktualisieren", "Löschen", "Finden", "<-Zurück"])
        if not opt.isnumeric():
            invalid()
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
                self.remove_customer()
                self.customer_menu()
            case 5:
                self.search_customer()
                self.customer_menu()
            case 6:
                self.main_menu()
            case _:
                print("ungültige Option!")
                self.customer_menu()

    def show_all_customers(self):
        header("Kundenliste")
        customers = self.customer_repo.get_all()
        for i in range(len(customers)):
            print(f"{i+1}. {customers[i]}")
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

    def remove_customer(self):
        header("Kunden Löschen nach index")
        opt = menu("Listentyp", ["Liste Anzeigen", "Suchen"])
        if not opt.isnumeric():
            invalid()
            self.remove_customer()

        opt = int(opt)
        customers = []

        match opt:
            case 1:
                customers = self.customer_repo.get_all()
            case 2:
                opt = menu("Suche Kunden nach", ["Name", "Adresse"])
                if not opt.isnumeric():
                    invalid()
                    self.remove_customer()
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
                        invalid()
                        self.remove_customer()
                customers = self.customer_repo.search(customer)
            case _:
                invalid()
                self.remove_customer()

        opt = menu("Kunde auswählen", customers, "=")
        if not opt.isnumeric():
            invalid()
            self.remove_customer()
        opt = int(opt)
        print(f"option = {opt}")
        if opt not in range(1, len(customers) + 1):
            invalid()
            self.remove_customer()

        cus = customers[opt - 1]
        res = self.customer_repo.remove(cus)
        if res == Repository.Result.SUCCESS:
            print(f"Der Kunde {cus} wurde gelöscht")
        elif res == Repository.Result.NOT_FOUND:
            warning(f"Der Kunde {cus} existiert nicht")

        footer("Kunden Löschen nach index")
        self.customer_menu()

    def search_customer(self):
        opt = menu("Suche Kunden nach", ["Name", "Adresse"])
        if not opt.isnumeric():
            invalid()
            self.search_customer()

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
                invalid()
                self.search_customer()

        header("Passende Kunden")
        customers = self.customer_repo.search(customer)
        for i in range(len(customers)):
            print(f"{i + 1}. {customers[i]}")
        footer("Passende Kunden")
