import turtle

from ex1.alphabet import *


def print_menu():
    print("1. Zeichne Buchstaben")
    print("2. Ersetze Wörter")
    print("3. Schere, Stein, Papier")


# ex = {
#     "1": write_to_turtle
# }


# def menu():
#     print_menu()
#     option = input("Deine Auswahl: ").strip()
#
#     if option in ex:
#         ex[option]()
#         print()
#         menu()
#     else:
#         print('"' + str(option) + "\" ist keine gültige Auswahl")


# menu()

t = turtle.Pen()

turtle.exitonclick()
