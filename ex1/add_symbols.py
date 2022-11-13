import turtle
from turtle import *

from turtle_move import *

inst_dict = {
    "w": move_forward,
    "s": move_backward,
    "d": rotate_right,
    "a": rotate_left,
    "f": move_up,
    "g": move_down
}


def draw_from_instructions(instr):
    t = turtle.Pen()

    for char in instr:
        inst_dict[char](t)

    turtle.exitonclick()


def define_symbol():
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

    new_sym = get_sym()
    print(new_sym)

    turtle.exitonclick()


define_symbol()
