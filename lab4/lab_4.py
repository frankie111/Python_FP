import lab4.ex1.ex_1
import lab4.ex2.ex_2
import lab4.ex3.ex_3


def menu():
    print("1. Zeichne Charakter / Wort")
    print("2. Ersetze Wörter")
    print("3. Schere, Stein, Papier (best of 3)")

    option = int(input("Your option: "))
    match option:
        case 1:
            lab4.ex1.ex_1.menu()
            menu()
        case 2:
            lab4.ex2.ex_2.menu()
            menu()
        case 3:
            lab4.ex3.ex_3.menu()
            menu()
        case _:
            print(str(option) + " is not a valid option!")


menu()
