import functools
from turtle import *

from ex1.symbol_dict import add_symbol, get_all_symbols
from ex1.turtle_move import *

inst_dict = {
    "w": move_forward,
    "s": move_backward,
    "d": rotate_right,
    "a": rotate_left,
    "f": move_up,
    "g": move_down,
    ".": draw_dot
}


def draw_from_instructions(instr, t):
    """
    Draws a symbol by following the instructions from {instr}
    :param t: Turtle used to draw
    :type t: turtle.Turtle
    :param instr: A string containing drawing instructions
    :type instr: str
    :return: None
    """
    for char in instr:
        inst_dict[char](t)


def draw_str():
    """
    Asks for a string input and draws it via turtle
    :return: None
    """
    letter_spacing = get_pace() * 8
    t_speed = 6
    txt = input("Enter the symbol / word to write: ")

    sym_dict = get_all_symbols()

    turtle.TurtleScreen._RUNNING = True
    t = turtle.Turtle()

    for char in txt:
        t.setheading(0)
        t.speed(t_speed)
        t.up()
        t.setx(t.pos()[0] + letter_spacing)
        t.sety(0)
        t.down()
        if char in sym_dict.keys():
            draw_from_instructions(sym_dict[char], t)

    turtle.exitonclick()


def event_handler(key, tur):
    """
    Handles key presses
    :param key: The keycode of the latest key press
    :type key: str
    :param tur: a Turtle object
    :type tur: turtle.Turtle
    :return: None
    """
    functions = {'w': move_forward, 'a': rotate_left, 's': move_backward,
                 'd': rotate_right, 'f': move_up, 'g': move_down,
                 '.': draw_dot}

    functions[key](tur)


def define_symbol():
    """
    Defines a new symbol by moving a turtle via keyboard and saves it to the dictionary
    :return: None
    """
    letter_spacing = get_pace() * 8
    sym = input("Enter the symbol: ")
    sym_dict = get_all_symbols()
    if sym in sym_dict.keys():
        option = input("Do you wish to override the symbol " + sym + "? (y/n)")
        match option:
            case 'y':
                turtle.TurtleScreen._RUNNING = True
                t = turtle.Turtle()

                print("Overriding symbol " + sym + "...")
                draw_from_instructions(sym_dict[sym], t)
                t.setheading(0)
                t.up()
                t.setx(t.pos()[0] + letter_spacing)
                t.sety(0)
                t.down()
            case _:
                return None
    else:
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle()

    print("w - move forward 10 Pixels")
    print("s - move backwards 10 Pixels")
    print("a - rotate left 45 Degrees")
    print("d - rotate right 45 Degrees")
    print("f - pen up")
    print("g - pen down")

    clear_sym()
    listen()
    for k in 'wasdfg.':
        onkey(functools.partial(event_handler, k, t), k)
    onkey(bye, 'Return')
    mainloop()

    sym_instr = get_sym()
    add_symbol(sym, sym_instr)
