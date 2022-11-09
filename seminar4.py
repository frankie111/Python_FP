def read_rational():
    n = int(input('n=='))
    m = int(input('m=='))

    return {'n': n, 'm': m}


def add(a, b):
    s = {'n': 0, 'm': 0}
    s['n'] = a['n'] * b['m'] + b['n'] * a['m']
    s['m'] = a['m'] * b['m']
    return s


def mul(a, b):
    s = {}
    s['n'] = a['n'] * b['n']
    s['m'] = a['m'] * b['m']
    return s


m = mul({'n': 1, 'm': 2}, {'n': 2, 'm': 3})


# print(m)

def cmmdc(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def simp(a):
    s = {}
    c = cmmdc(a['n'], a['m'])
    s = {'n': a['n'] // c, 'm': a['m'] // c}
    return s


print(simp(m))


def addtolist(l, a):
    l.append(a)


def sumlist(l):
    s = {'n': 0, 'm': 1}
    for i in range(len(l)):
        s = add(l[i], s)

    return s


def loschen(l, a):
    nl = []
    for i in range(len(l)):
        if l[i] == a:
            l.pop(i)

    return nl


numbers = []
addtolist(numbers, {'n': 1, 'm': 2})
addtolist(numbers, {'n': 3, 'm': 4})
print(sumlist(numbers))

loschen(numbers, {'n': 1, 'm': 2})
