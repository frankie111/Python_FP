import turtle

curr_sym = ""
pace = 3  # ~= font size


def get_pace():
    return pace


def move_forward(t):
    t.fd(pace)
    global curr_sym
    curr_sym += 'w'


def move_backward(t):
    t.back(pace)
    global curr_sym
    curr_sym += 's'


def rotate_right(t):
    t.right(45)
    global curr_sym
    curr_sym += 'd'


def rotate_left(t):
    t.left(45)
    global curr_sym
    curr_sym += 'a'


def move_up(t):
    t.pu()
    global curr_sym
    curr_sym += 'f'


def move_down(t):
    t.pd()
    global curr_sym
    curr_sym += 'g'


def draw_dot(t):
    t.dot(10)
    global curr_sym
    curr_sym += '.'


def clear_sym():
    global curr_sym
    curr_sym = ""


def get_sym():
    global curr_sym
    return curr_sym
