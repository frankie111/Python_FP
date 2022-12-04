from lab5.models.CookedDish import CookedDish
from lab5.models.Drink import Drink
from lab5.repository.CookedDishRepository import CookedDishRepository
from lab5.repository.DrinkRepository import DrinkRepository
from lab5.repository.Repository import Repository
from lab5.ui.UIController import menu, invalid, header, footer, warning


class MenuController:
    def __init__(self, db_root):
        self.cooked_dish_repo = CookedDishRepository(f"{db_root}menu/cooked_dishes.txt")
        self.drink_repo = DrinkRepository(f"{db_root}menu/drinks.txt")

    def menu(self):
        opt = menu("Speisekarte Verwaltung",
                   ["Alle Anzeigen", "Hinzufügen", "Aktualisieren", "Löschen", "Finden", "<-Zurück"])

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
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                # caller menu will resume
                pass
            case _:
                invalid()
                self.menu()

    def __show_all_items(self):
        header("Speisekarte", '=_=')
        drinks = self.drink_repo.get_all()
        dishes = self.cooked_dish_repo.get_all()
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
        res = self.drink_repo.add(new_drink)
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
        res = self.cooked_dish_repo.add(new_dish)
        if res == Repository.Result.SUCCESS:
            print(f"Neue Speise hinzugefügt: [{new_dish}]")
        elif res == Repository.Result.ALREADY_EXISTS:
            warning(f"Die Speise {new_dish} ist bereits vorhanden")
        footer("Neue Speise")
