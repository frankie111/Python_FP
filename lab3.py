import turtle


# 1.
def zeichne_rechtecke():
    height = 100
    width = 200

    _height = 25
    _width = 50

    t = turtle.Pen()

    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)

    t.up()
    t.left(90)
    t.forward((width - _width) // 2)
    t.left(90)
    t.forward((height - _height) // 2)
    t.down()
    t.forward(_height)
    t.right(90)
    t.forward(_width)
    t.right(90)
    t.forward(_height)
    t.right(90)
    t.forward(_width)

    # t.reset()
    turtle.exitonclick()


# 2.
def zeichne_herz():
    radius = 60
    steps = 10
    length = 160
    t = turtle.Pen()

    t.width(6)
    t.left(50)
    t.forward(length)
    t.circle(radius, 200, steps)
    t.left(220)
    t.circle(radius, 200, steps)
    t.forward(length)

    # t.reset()
    turtle.exitonclick()


def zeichne_rechteck(t, w, h=None):
    if h is None:
        h = w

    t.setheading(0)
    t.down()
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)


def zeichne_dreieck(t, base):
    t.down()
    t.forward(base)
    t.left(120)
    t.forward(base)
    t.left(120)
    t.forward(base)
    t.left(120)


def zeichne_linie(t, a, b):
    t.up()
    t.setpos(a)
    t.down()
    t.setpos(b)


def zeichne_haus(t, width=200, height=120, window_size=0, door_width=0, door_height=0):
    if door_width == 0:
        door_width = height // 2
        door_height = door_width * 1.5

    if window_size == 0:
        window_size = width // 4

    t.speed(4)
    origin_pos = t.pos()

    # house + roof
    zeichne_rechteck(t, width, height)
    t.up()
    t.left(180)
    t.forward(height)
    t.down()
    t.right(90)
    zeichne_dreieck(t, width)

    # window
    window_origin = [origin_pos[0] + (width - window_size * 2 - door_width) // 2,
                     origin_pos[1] + (height - window_size) // 2]

    t.up()
    t.setpos(window_origin)

    t.down()
    zeichne_rechteck(t, window_size)

    # door
    door_origin = [window_origin[0] + width - (window_size + door_width),
                   origin_pos[1] + 10]

    t.up()
    t.setpos(door_origin)
    t.down()
    t.left(90)
    zeichne_rechteck(t, door_width, door_height)


# 3.
def zeichne_hauser():
    t = turtle.Pen()

    t.up()
    t.goto(-300, -250)
    zeichne_haus(t, 120, 80)

    t.up()
    t.goto(0, -250)
    t.left(90)

    zeichne_haus(t, 250, 180)

    # t.reset()
    turtle.exitonclick()


def zeichne_hauser_2():
    width = 220
    height = 160
    window_size = 40
    window_left_padding = 40
    window_bottom_padding = 50
    door_width = 40
    door_height = 80
    door_bottom_padding = 20
    door_right_padding = 40
    roof_height = 80
    house_dist = 100
    o1 = [-250, -200]
    o2 = [o1[0] + width + house_dist, o1[1]]
    o3 = [100, 100]
    o4 = [-200, 100]

    origins = [o1, o2]  # , o3, o4]

    t = turtle.Pen()
    t.speed(6)
    t.up()

    for o in origins:
        zeichne_linie(t, o, [o[0] + width, o[1]])

    for o in origins:
        zeichne_linie(t, [o[0], o[1] + height], [o[0] + width, o[1] + height])

    for o in origins:
        zeichne_linie(t, o, [o[0], o[1] + height])

    for o in origins:
        zeichne_linie(t, [o[0] + width, o[1]], [o[0] + width, o[1] + height])

    for o in origins:
        zeichne_linie(t, [o[0], o[1] + height], [o[0] + width // 2, o[1] + height + roof_height])

    for o in origins:
        zeichne_linie(t, [o[0] + width // 2, o[1] + height + roof_height], [o[0] + width, o[1] + height])

    # window
    for o in origins:
        t.up()
        t.setpos(o[0] + window_left_padding, o[1] + window_bottom_padding)
        zeichne_rechteck(t, window_size)

    # door
    for o in origins:
        t.up()
        t.setpos(o[0] + width - door_width - door_right_padding, o[1] + door_bottom_padding)
        zeichne_rechteck(t, door_width, door_height)

    turtle.exitonclick()


def menu():
    option = int(input("Wählen Sie eine Zeichnung aus: \n \t 1. Rechteck \n \t 2. Herz \n \t 3. Häuser \n"))
    match option:
        case 1:
            zeichne_rechtecke()
        case 2:
            zeichne_herz()
        case 3:
            zeichne_hauser_2()
        case _:
            print('"' + str(option) + '"' + " ist keine gültige option!")
            menu()

# zeichne_rechtecke()
# zeichne_herz()
# zeichne_hauser()
# zeichne_hauser_2()


menu()
