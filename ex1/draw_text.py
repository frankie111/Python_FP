import turtle
from ex1.alphabet import *

ch = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "o": o,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z,
    # ".": point,
    # "?": point,
    # "!": point
}


def draw_text():
    txt = input("Enter the text to draw: ")
    turt = turtle.Pen()

    for char in txt:
        ch[char](turt)

    turtle.exitonclick()


def menu():
    print("Enter 1 to write a letter")
    print("Enter 2 to add a character")
    option = int(input())

    match option:
        case 1:
            draw_text()
            menu()
        case _:
            print('"' + str(option) + '"' + " Is not a valid option!")


menu()
