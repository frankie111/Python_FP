from lab5.models.CookedDish import CookedDish
from lab5.models.Drink import Drink
from lab5.repository.Repository import Repository
from lab5.ui.UIController import menu, invalid, header, footer, warning, tooltip


class MenuController:
    def __init__(self, drink_repo, cooked_dish_repo):
        self.__drink_repo = drink_repo
        self.__cooked_dish_repo = cooked_dish_repo

    def menu(self):
        opt = menu("Speisekarte Verwaltung",
                   ["Alle Anzeigen", "Hinzufügen", "Aktualisieren", "Löschen", "<-Zurück"])

        if not opt.isnumeric():
            invalid()
            self.menu()

        opt = int(opt)

        match opt:
            case 1:
                self.__show_all_items()
                self.menu()
            case 2:
                self.__add_item()
                self.menu()
            case 3:
                self.__update_item()
                self.menu()
            case 4:
                self.__remove_item()
                self.menu()
            case 5:
                # caller menu will resume
                pass
            case _:
                invalid()
                self.menu()

    def __show_all_items(self):
        header("Speisekarte", '=_=')
        drinks = self.__drink_repo.get_all()
        dishes = self.__cooked_dish_repo.get_all()
        header("Getränke", "=")
        for i in range(len(drinks)):
            print(f"{i + 1}. {drinks[i]}")
        header("Speisen", "=")
        for i in range(len(dishes)):
            print(f"{i + 1}. {dishes[i]}")
        print()
        footer("Speisekarte", '=_=')

    def __add_item(self):
        opt = menu("Artikel hinzufügen", ["Getränk", "Speise", "<-Zurück"])
        if not opt.isnumeric():
            invalid()
            self.__add_item()

        opt = int(opt)
        match opt:
            case 1:
                self.__add_drink()
                self.__add_item()
            case 2:
                self.__add_dish()
                self.__add_item()
            case 3:
                # caller menu will resume
                pass
            case _:
                invalid()
                self.__add_item()

    def __add_drink(self):
        header("Neues Getränk")
        name = input("Name=")
        portion_size = input("PortionsGröße=")
        price = input("Preis=")
        alcohol_content = input("Alkoholgehalt=")

        new_drink = Drink(id_=0, name=name, portion_size=portion_size, price=price, alcohol_content=alcohol_content)
        res = self.__drink_repo.add(new_drink)
        if res == Repository.Result.SUCCESS:
            print(f"Neues Getränk hinzugefügt: [{new_drink}]")
        elif res == Repository.Result.ALREADY_EXISTS:
            warning(f"Das Getränk {new_drink.name} ist bereits vorhanden")
        footer("Neues Getränk")

    def __add_dish(self):
        header("Neue Speise")
        name = input("Name=")
        portion_size = input("PortionsGröße=")
        price = input("Preis=")
        prep_time = input("Zubereitungszeit=")

        new_dish = CookedDish(id_=0, name=name, portion_size=portion_size, price=price, prep_time=prep_time)
        res = self.__cooked_dish_repo.add(new_dish)
        if res == Repository.Result.SUCCESS:
            print(f"Neue Speise hinzugefügt: [{new_dish}]")
        elif res == Repository.Result.ALREADY_EXISTS:
            warning(f"Die Speise {new_dish} ist bereits vorhanden")
        footer("Neue Speise")

    def __update_item(self):
        header("Artikel aktualisieren nach index")
        opt = menu("Artikeltyp", ["Getränk", "Speise", "<-Zurück"])
        if not opt.isnumeric():
            invalid()
            self.__update_item()

        opt = int(opt)

        match opt:
            case 1:
                self.__update_drink()
                self.__update_item()
            case 2:
                self.__update_dish()
                self.__update_item()
            case 3:
                # caller menu will resume
                pass
            case _:
                invalid()
                self.__update_item()

        footer("Artikel aktualisieren nach index")

    def __update_drink(self):
        drinks = self.__drink_repo.get_all()
        opt = menu("Getränk aktualisieren", drinks, "=")
        if not opt.isnumeric():
            invalid()
            self.__update_drink()
        opt = int(opt)
        if opt not in range(1, len(drinks) + 1):
            invalid()
            self.__update_drink()

        drink = drinks[opt - 1]
        print(f"Ausgewählter Getränk: {drink}")
        header("Infos aktualisieren")
        tooltip("Um die aktuelle Infos zu behalten einfach ENTER drücken")
        name = input("Name=")
        portion_size = input("Portionsgröße=")
        price = input("Preis=")
        alcohol_content = input("Alkoholgehalt=")
        updated_drink = Drink(id_=0)

        if name != '':
            updated_drink.name = name
        if portion_size != '':
            updated_drink.portion_size = portion_size
        if price != '':
            updated_drink.price = price
        if alcohol_content != '':
            updated_drink.alcohol_content = alcohol_content

        res = self.__drink_repo.update(drink, updated_drink)
        if res == Repository.Result.SUCCESS:
            print(f"Das Getränk [{drink}] wurde zu [{updated_drink}] aktualisiert")
        elif res == Repository.Result.NOT_FOUND:
            warning(f"Das Getränk [{drink}] wurde nicht gefunden!")

        footer("Infos aktualisieren")

    def __update_dish(self):
        dishes = self.__cooked_dish_repo.get_all()
        opt = menu("Speise aktualisieren", dishes, "=")
        if not opt.isnumeric():
            invalid()
            self.__update_dish()
        opt = int(opt)
        if opt not in range(1, len(dishes) + 1):
            invalid()
            self.__update_dish()

        dish = dishes[opt - 1]
        print(f"Ausgewählte Speise: {dish}")
        header("Infos aktualisieren")
        tooltip("Um die aktuelle Infos zu behalten einfach ENTER drücken")
        name = input("Name=")
        portion_size = input("Portionsgröße=")
        price = input("Preis=")
        prep_time = input("Zubereitungszeit=")
        updated_dish = CookedDish(id_=0)

        if name != '':
            updated_dish.name = name
        if portion_size != '':
            updated_dish.portion_size = portion_size
        if price != '':
            updated_dish.price = price
        if prep_time != '':
            updated_dish.prep_time = prep_time

        res = self.__cooked_dish_repo.update(dish, updated_dish)
        if res == Repository.Result.SUCCESS:
            print(f"Die Speise [{dish}] wurde zu [{updated_dish}] aktualisiert")
        elif res == Repository.Result.NOT_FOUND:
            warning(f"Die Speise [{dish}] wurde nicht gefunden!")

        footer("Infos aktualisieren")

    def __remove_item(self):
        header("Artikel löschen")
        opt = menu("Artikeltyp", ["Getränk", "Speise", "<-Zurück"])
        if not opt.isnumeric():
            invalid()
            self.__remove_item()

        opt = int(opt)

        match opt:
            case 1:
                self.__remove_drink()
                self.__remove_item()
            case 2:
                self.__remove_dish()
                self.__remove_item()
            case 3:
                # Caller menu will resume
                pass
            case _:
                invalid()
                self.__remove_item()

    def __remove_drink(self):
        drinks = self.__drink_repo.get_all()
        opt = menu("Getränk löschen", drinks, "=")
        if not opt.isnumeric():
            invalid()
            self.__remove_drink()
        opt = int(opt)
        if opt not in range(1, len(drinks) + 1):
            invalid()
            self.__remove_drink()

        drink = drinks[opt - 1]
        res = self.__drink_repo.remove(drink)

        if res == Repository.Result.SUCCESS:
            print(f"Das Getränk [{drink}] wurde gelöscht")
        elif res == Repository.Result.NOT_FOUND:
            warning(f"Das Getränk [{drink}] wurde nicht gefunden")

    def __remove_dish(self):
        dishes = self.__cooked_dish_repo.get_all()
        opt = menu("Speise löschen", dishes, "=")
        if not opt.isnumeric():
            invalid()
            self.__remove_dish()
        opt = int(opt)
        if opt not in range(1, len(dishes) + 1):
            invalid()
            self.__remove_dish()

        dish = dishes[opt - 1]
        res = self.__cooked_dish_repo.remove(dish)

        if res == Repository.Result.SUCCESS:
            print(f"Die Speise [{dish}] wurde gelöscht")
        elif res == Repository.Result.NOT_FOUND:
            warning(f"Die Speise [{dish}] wurde nicht gefunden")
