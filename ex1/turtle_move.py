import turtle

curr_sym = ""
tut = turtle.Pen()


def move_forward():
    tut.fd(10)
    global curr_sym
    curr_sym += 'w'


def move_backward():
    tut.back(10)
    global curr_sym
    curr_sym += 's'


def rotate_right():
    tut.right(45)
    global curr_sym
    curr_sym += 'd'


def rotate_left():
    tut.left(45)
    global curr_sym
    curr_sym += 'a'


def move_up():
    tut.pu()
    global curr_sym
    curr_sym += 'f'


def move_down():
    tut.pd()
    global curr_sym
    curr_sym += 'g'


def clear_sym():
    global curr_sym
    curr_sym = ""


def get_sym():
    global curr_sym
    return curr_sym
