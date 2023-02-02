class Square:
    def __init__(self, x, y, side=0):
        self.x = x
        self.y = y
        self.side = side


class Rectangle:
    def __init__(self, x, y, width, length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length


def contains(squares: list[Square], rect: Rectangle):
    for square in squares:
        if square.x < rect.x \
                or square.y < rect.y \
                or square.x + square.side > rect.x + rect.length \
                or square.y + square.side > rect.y + rect.width:
            return False

    return True
