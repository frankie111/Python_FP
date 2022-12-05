from lab5.models.Customer import Customer
from lab5.repository.CustomerRepository import CustomerRepository
from lab5.repository.Repository import Repository
from lab5.ui.UIController import menu, invalid, header, footer, warning, tooltip


class CustomerController:
    def __init__(self, customer_repo):
        self.__customer_repo = customer_repo

    def menu(self):
        opt = menu("Kunden Verwaltung",
                   ["Alle Anzeigen", "Hinzufügen", "Aktualisieren", "Löschen", "Finden", "<-Zurück"])
        if not opt.isnumeric():
            invalid()
            self.menu()

        opt = int(opt)

        match opt:
            case 1:
                self.__show_all_customers()
                self.menu()
            case 2:
                self.__add_customer()
                self.menu()
            case 3:
                self.__update_customer()
            case 4:
                self.__remove_customer()
                self.menu()
            case 5:
                self.__search_customer()
                self.menu()
            case 6:
                # caller menu will resume
                pass
            case _:
                invalid()
                self.menu()

    def __show_all_customers(self):
        header("Kundenliste")
        customers = self.__customer_repo.get_all()
        for i in range(len(customers)):
            print(f"{i + 1}. {customers[i]}")
        footer("Kundenliste")

    def __add_customer(self):
        header("Neuer Kunde")
        name = input("Name=")
        address = input("Adresse=")
        footer("Neuer Kunde")

        new_customer = Customer(name=name, address=address)
        res = self.__customer_repo.add(new_customer)
        if res == Repository.Result.SUCCESS:
            print(f"Neuer Kunde hinzugefügt [{new_customer}]")
        elif res == Repository.Result.ALREADY_EXISTS:
            warning(f"Der Kunde [{new_customer}] ist bereits vorhanden")

    def __update_customer(self):
        header("Kunden aktualisieren nach index")
        opt = menu("Listentyp", ["Liste Anzeigen", "Suchen"])
        if not opt.isnumeric():
            invalid()
            self.__update_customer()

        opt = int(opt)
        customers = []

        match opt:
            case 1:
                customers = self.__customer_repo.get_all()
            case 2:
                opt = menu("Suche Kunden nach", ["Name", "Adresse"])
                if not opt.isnumeric():
                    invalid()
                    self.__update_customer()
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
                        self.__update_customer()
                customers = self.__customer_repo.search(customer)
            case _:
                invalid()
                self.__update_customer()

        opt = menu("Kunde auswählen", customers, "=")
        if not opt.isnumeric():
            invalid()
            self.__update_customer()

        opt = int(opt)
        if opt not in range(1, len(customers) + 1):
            invalid()
            self.__update_customer()

        cus = customers[opt - 1]
        print(f"Ausgewählter Kunde: {cus}")

        header("Infos aktualisieren")
        tooltip("Um die aktuelle Infos zu behalten einfach ENTER drücken")
        name = input("Name=")
        address = input("Adresse=")

        updated_cus = Customer()
        if name != '':
            updated_cus.name = name
        if address != '':
            updated_cus.address = address

        res = self.__customer_repo.update(cus, updated_cus)
        if res == Repository.Result.SUCCESS:
            print(f"Der Kunde [{cus}] wurde zu [{updated_cus}] aktualisiert")
        elif res == Repository.Result.NOT_FOUND:
            warning(f"Der Kunde [{cus}] wurde nicht gefunden!")

        footer("Kunden aktualisieren nach index")

    def __remove_customer(self):
        header("Kunden Löschen nach index")
        opt = menu("Listentyp", ["Liste Anzeigen", "Suchen"])
        if not opt.isnumeric():
            invalid()
            self.__remove_customer()

        opt = int(opt)
        customers = []

        match opt:
            case 1:
                customers = self.__customer_repo.get_all()
            case 2:
                opt = menu("Suche Kunden nach", ["Name", "Adresse"])
                if not opt.isnumeric():
                    invalid()
                    self.__remove_customer()
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
                        self.__remove_customer()
                customers = self.__customer_repo.search(customer)
            case _:
                invalid()
                self.__remove_customer()

        opt = menu("Kunde auswählen", customers, "=")
        if not opt.isnumeric():
            invalid()
            self.__remove_customer()
        opt = int(opt)
        if opt not in range(1, len(customers) + 1):
            invalid()
            self.__remove_customer()

        cus = customers[opt - 1]
        res = self.__customer_repo.remove(cus)
        if res == Repository.Result.SUCCESS:
            print(f"Der Kunde {cus} wurde gelöscht")
        elif res == Repository.Result.NOT_FOUND:
            warning(f"Der Kunde {cus} existiert nicht")

        footer("Kunden Löschen nach index")
        self.menu()

    def __search_customer(self):
        opt = menu("Suche Kunden nach", ["Name", "Adresse"])
        if not opt.isnumeric():
            invalid()
            self.__search_customer()

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
                self.__search_customer()

        header("Passende Kunden")
        customers = self.__customer_repo.search(customer)
        for i in range(len(customers)):
            print(f"{i + 1}. {customers[i]}")
        footer("Passende Kunden")
