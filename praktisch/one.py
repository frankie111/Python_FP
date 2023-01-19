from functools import reduce


def ub1(even_row=True):
    with open("zahlen.txt", 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda line: line.strip("\n").split("UBB"), lines))
        lines = list(map(lambda line: list(map(lambda element: int(element), line)), lines))

        target = not even_row
        lines = list(filter(lambda line: all(map(lambda nr: nr % 2 == target, line)), lines))

        print(lines)

        lines = list(map(lambda line: sum(line), lines))
        summe = sum(lines)

        return summe

print(ub1(False))

def false_test():
    assert ub1(True) == 98


def successful_test():
    assert ub1(False) == 98


# print(ub1(False))
false_test()
successful_test()
