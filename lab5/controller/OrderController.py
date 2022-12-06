from lab5.models.Customer import Customer
from lab5.models.Order import Order
from lab5.repository.CookedDishRepository import CookedDishRepository
from lab5.repository.CustomerRepository import CustomerRepository
from lab5.repository.DrinkRepository import DrinkRepository
from lab5.repository.OrderRepository import OrderRepository
from lab5.repository.Repository import Repository
from lab5.ui.UIController import menu, invalid, header, footer, warning, tooltip


class OrderController:
    def __init__(self, customer_repo: CustomerRepository, order_repo: OrderRepository,
                 cooked_dish_repo: CookedDishRepository, drink_repo: DrinkRepository):
        self.__customer_repo = customer_repo
        self.__order_repo = order_repo
        self.__cooked_dish_repo = cooked_dish_repo
        self.__drink_repo = drink_repo

    def menu(self):
        opt = menu("Bestellungen Verwaltung",
                   ["Alle Anzeigen", "Hinzufügen", "Aktualisieren", "Löschen", "Finden", "<-Zurück"])
        if not opt.isnumeric():
            invalid()
            self.menu()

        opt = int(opt)

        match opt:
            case 1:
                self.__show_all_orders()
                self.menu()
            case 2:
                self.__add_order()
                self.menu()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                # caller menu will resume
                return
            case _:
                invalid()
                self.menu()

    def __show_all_orders(self):
        header("Bestellungen")
        orders = self.__order_repo.get_all()

        for i in range(len(orders)):
            cus = self.__customer_repo.find_by_id(orders[i].customer_id)
            items = [*self.__drink_repo.find_by_ids(orders[i].item_ids),
                     *self.__cooked_dish_repo.find_by_ids(orders[i].item_ids)]
            print(f"{i + 1}. {orders[i].pprint(cus, items)}\n")

        footer("Bestellungen")

    def __add_order(self):
        """
        Menu for adding a new order
        :return:
        """
        # orders = self.__order_repo.get_all()
        customers = self.__customer_repo.get_all()
        dishes = self.__cooked_dish_repo.get_all()
        drinks = self.__drink_repo.get_all()
        header("Neue Bestellung")

        customer_ids = self.__select_customer(customers)
        items = self.__select_items(drinks, dishes)

        footer("Neue Bestellung")
        item_ids = list(map(lambda it: it.id, items))
        new_order = Order(0, customer_ids, item_ids)
        new_order.compute_total_price(items)

        res = self.__order_repo.add(new_order)
        if res == Repository.Result.SUCCESS:
            print(f"Bestellung hinzugefügt: {new_order}")
        elif res == Repository.Result.ALREADY_EXISTS:
            warning(f"Diese Bestellung ist bereits vorhanden")

    def __select_customer(self, customers: list[Customer]):
        """
        Menu for selecting a customer when creating an order
        :param customers:
        :return:
        """
        opt = menu("Kunden auswählen", ["Liste Anzeigen", "Suchen", "Neuer Kunde"])
        if not opt.isnumeric():
            invalid()
            self.__add_order()

        opt = int(opt)

        cus = 0
        match opt:
            case 1:
                cus = self.__select_customer_from_list(customers)
            case 2:
                cus = self.__select_customer_by_search()
            case 3:
                cus = self.__select_customer_add_new()
            case _:
                invalid()
                self.__add_order()

        return cus

    def __select_customer_from_list(self, customers: list[Customer]):
        opt = menu("Kunden auswählen", customers, "=")
        if not opt.isnumeric():
            invalid()
            self.__select_customer_from_list(customers)

        opt = int(opt)

        if opt in range(1, len(customers) + 1):
            cus = customers[opt - 1]
            return cus.id
        else:
            invalid()
            self.__select_customer_from_list(customers)

    def __select_customer_by_search(self):
        opt = menu("Suche Kunden nach", ["Name", "Adresse"])
        if not opt.isnumeric():
            invalid()
            self.__select_customer_by_search()

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
                self.__select_customer_by_search()

        filtered = self.__customer_repo.search(customer)
        option = menu("Passende Kunden", filtered, "=")
        if not option.isnumeric():
            invalid()
            self.__select_customer_by_search()

        option = int(option)

        if option not in range(1, len(filtered) + 1):
            invalid()
            self.__select_customer_by_search()

        cus = filtered[option - 1]
        print(f"Der Kunde [{cus}] wurde gewählt")
        return cus.id

    def __select_customer_add_new(self):
        header("Neuer Kunde")
        name = input("Name=")
        address = input("Adresse=")
        footer("Neuer Kunde")

        new_customer = Customer(0, name, address)
        res = self.__customer_repo.add(new_customer)
        if res == Repository.Result.SUCCESS:
            print(f"Neuer Kunde hinzugefügt [{new_customer}]")
        elif res == Repository.Result.ALREADY_EXISTS:
            warning(f"Der Kunde [{new_customer}] ist bereits vorhanden")

        return new_customer.__hash__()

    @staticmethod
    def __select_items(drinks, dishes):
        header("Artikel wählen")
        tooltip("Tippen sie die Artikel getrennt mit Kommas")
        opt = menu("Getränke", drinks, "=")
        indexes = opt.split(',')
        indexes = list(map(lambda idx: int(idx.strip()) - 1, indexes))
        drink_list = []
        for i in indexes:
            if i in range(len(drinks)):
                drink_list.append(drinks[i])
            else:
                warning(f"{i + 1} ist keine gültige Option")

        opt = menu("Speisen", dishes, "=")
        indexes = opt.split(',')
        indexes = list(map(lambda idx: int(idx.strip()) - 1, indexes))
        dish_list = []
        for i in indexes:
            if i in range(len(dishes)):
                dish_list.append(dishes[i])
            else:
                warning(f"{i + 1} ist keine gültige Option")

        footer("Artikel wählen")
        return [*drink_list, *dish_list]
