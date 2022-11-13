from ex1.add_symbols import define_symbol, draw_str


def menu():
    print("1. Write a letter / word")
    print("2. Add a symbol")
    option = int(input())

    match option:
        case 1:
            draw_str()
            menu()
        case 2:
            define_symbol()
            menu()
        case _:
            print('"' + str(option) + '"' + " Is not a valid option!")
