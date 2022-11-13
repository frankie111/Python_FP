from turtle import *

from ex1.symbol_dict import add_symbol, get_all_symbols
from ex1.turtle_move import *

inst_dict = {
    "w": move_forward,
    "s": move_backward,
    "d": rotate_right,
    "a": rotate_left,
    "f": move_up,
    "g": move_down
}


def draw_from_instructions(instr):
    f"""
    Draws a symbol by following the instructions from {instr}
    :param instr: A string containing instructions
    :return: None
    """
    for char in instr:
        inst_dict[char]()


def draw_str():
    txt = input("Enter the symbol / word to write: ")

    sym_dict = get_all_symbols()
    init_turtle()

    for char in txt:
        if char in sym_dict.keys():
            draw_from_instructions(sym_dict[char])

    turtle.exitonclick()
    delete_turtle()


def define_symbol():
    """
    Defines a new symbol by moving a turtle via keyboard and saves it to the dictionary
    :return: None
    """
    sym = input("Enter the symbol: ")
    sym_dict = get_all_symbols()
    if sym in sym_dict.keys():
        option = input("Do you wish to override the symbol " + sym + "? (y/n)")
        match option:
            case 'y':
                print("Overriding symbol " + sym + "...")
            case _:
                return None

    print("w - move forward 10 Pixels")
    print("s - move backwards 10 Pixels")
    print("a - rotate left 45 Degrees")
    print("d - rotate right 45 Degrees")
    print("f - pen up")
    print("g - pen down")

    # t = turtle.Pen()

    clear_sym()
    listen()
    onkey(move_forward, 'w')
    onkey(rotate_left, 'a')
    onkey(move_backward, 's')
    onkey(rotate_right, 'd')
    onkey(move_up, 'f')
    onkey(move_down, 'g')
    onkey(bye, 'Return')
    mainloop()

    sym_instr = get_sym()
    add_symbol(sym, sym_instr)
