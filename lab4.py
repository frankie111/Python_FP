import ex1.ex_1


def menu():
    print("1. Draw character / word")
    print("2. Replace words")
    print("3. Rock, Paper, Scissors")

    option = int(input("Your option: "))
    match option:
        case 1:
            ex1.ex_1.menu()
            menu()
        case _:
            print(str(option) + " is not a valid option!")


menu()
