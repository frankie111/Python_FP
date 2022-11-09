def summe(zahlen, summe):
    for i in range(len(zahlen)):
        for j in range(i + 1, len(zahlen)):
            if zahlen[i] + zahlen[j] == summe:
                return i, j

    return None


# zahlen = [1, 3, 2, 4]
# print(summe(zahlen, 8))


def big_sum(a, b):
    res = ""
    carry = 0

    for i in range(len(a) - 1, -1, -1):
        s = int(a[i]) + int(b[i])

        if carry:
            s += 1
            carry = 0

        if s > 10:
            carry = 1
            s -= 10

        res = _str(s) + res

    return res


# print(big_sum("1212312231231", "5553412313231"))


def reverse(word):
    voc = "aeiou"
    voc_list = ""
    for i in word:
        if i in voc:
            voc_list += i

    res = ""

    ct = len(voc_list) - 1
    for i in word:
        if i in voc:
            res += voc_list[ct]
            ct -= 1
            continue

        res += i

    return res


# print(reverse("Terminator"))

def aufgabe_5(string):
    vok = "aeiou"
    svok = ""
    ns = ""
    i = 0
    while i < len(string):
        if string[i] in vok:
            svok = svok + string[i]
        i += 1
    j = len(svok) - 1
    i = 0
    while i < len(string):
        if string[i] not in svok:
            ns += string[i]



def get_digits(n):
    digits = [0] * 10
    while n > 0:
        digits[n % 10] += 1
        n //= 10

    return digits


def max_vektor(lista):
    mx = []
    aux = [lista[0]]
    for i in range(1, len(lista)):
        if get_digits(lista[i - 1]) == get_digits(lista[i]):
            aux.append(lista[i])
        else:
            if len(aux) > len(mx):
                mx = aux
            aux = [lista[i]]

    if len(aux) > len(mx):
        mx = aux

    return mx


mat = [
    ['A', 'L', 'C', 'A'],
    ['L', 'E', 'G', 'H'],
    ['Q', 'R', 'T', 'F']
]

_str = "ALERT"

"""
pos_list: 
Randurile = literele cuvantului cautat
Coloanele = pozitiile literelor gasite in matrice

A: [0, 0], [0, 3]
L: [1, 0], [0, 1]
E: [1, 1]
R: [2, 1]
T: [2, 2]
"""



"""
# Not tested!
def is_neighbour(i, j, _i, _j):
    return (i == _i and (j == _j - 1 or j == _j + 1)) or (j == _j and (i == _i - 1 or i == _i + 1))


def find_in_matrix(matrix, word):
    pos_list = []
    word_len = len(word)

    for i in range(word_len):
        pos_list.append([])

    rows = len(matrix)
    col = len(matrix[0])
    for i in range(rows):
        for j in range(col):
            if matrix[i][j] in word:
                pos = word.find(matrix[i][j])
                pos_list[pos].append([i, j])

    for i in pos_list:
        print(i)

    print()

    for i in range(len(pos_list)):
        for letter in pos_list[i]:
            for j in range(i + 1, len(pos_list)):
                for k in range(len(pos_list[j])):
                    print(str(letter) + ' ' + str(pos_list[j][k]))

            print()


find_in_matrix(mat, _str)
"""