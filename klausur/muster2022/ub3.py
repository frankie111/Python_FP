from functools import reduce

testStr = "22a3(abcd)Xy2Z"


def klammer(s):
    if s[-1] != ')':
        return klammer(s[:-1])

    if s[0] != '(':
        return klammer(s[1:])

    return s


# print(klammer(testStr))

mat = [
    [1, 1, 1],
    [1, 2],
    [3, 1]
]


def matrix_sum(m):
    return reduce(lambda line1, line2: line1 + reduce(lambda a, b: a + b, line2), m, 0)

# print(matrix_sum(mat))


