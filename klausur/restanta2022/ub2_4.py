from functools import reduce
from math import sqrt


def e(n):
    if n == 1:
        return 2

    return e(n - 1) + (-1) ** (n + 1) * n * (n + 1)


# print(e(4))

def skprod(a: list[float], b: list[float], k: int):
    lis = [a[i] * b[i] for i in range(k)]
    return reduce(lambda x, y: x + y, lis)


def compute_f(a: list[float], b: list[float], k: int):
    prod = skprod(a, b, k)
    ma = sqrt(skprod(a, a, k))
    mb = sqrt(skprod(b, b, k))

    return prod // ma * mb

# va = [1, 2, 3]
# vb = [3, 2, 1]
#
# print(skprod(va, vb, 3))
