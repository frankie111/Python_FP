import math


def summe(n):
    """
    1. Schreiben Sie eine Funktion,
    die die Summe aller geraden Ziffer einer angegebenen Zahl berechnet
    """
    if n == 0:
        return 0

    uc = n % 10
    return (uc if uc % 2 == 0 else 0) + summe(n // 10)


# print(summe(1234))

def last_capital(string):
    """
    2. Schreiben Sie eine Funktion,
    die den letzten erhaltenen Großbuchstabe der Zeichenkette zurückgibt
    """
    if len(string) == 0:
        return None
    if string[-1].isupper():
        return string[-1]

    return last_capital(string[:-1])


# satz = "Heute machen wir Python und Assembly"
# print(last_capital(satz))


def vokale(string):
    """
    3. Schreiben Sie für eine gegebene Zeichenkette eine Funktion,    if len(string) == 0:
    die die Gesamtzahl der darin enthaltenen Vokalen (a, e, i, o und u) zählt.        return 0
    """
    if string[-1] in "aeiou":
        return (1 if string[-1].lower() in "aeiou" else 0) + vokale(string[1:])

    return vokale(string)


# print(vokale("Pythoane"))


def palindrom(n):
    """
    4. Schreiben Sie für eine Zahl eine Funktion, die true zurückgibt,
     wenn die angegebene Zahl Palindrom ist, andernfalls falsch.
    """
    if n < 10:
        return True
    if n % 10 != n // 10 ** (int(math.log10(n))):
        return False
    return palindrom(n // 10 % (10 ** (int(math.log10(n)))) // 10)


# print(palindrom(12321))


def maxim(liste):
    """
    5. Schreiben sie eine Funktion, die das größte Element einer Liste zurückgibt
    """
    if len(liste) == 1:
        return liste[0]

    return max(maxim(liste[1:]), liste[0])


# lis = [5, 6, 2, 1, 7, 3]
# print(maxim(lis))


def findlist(l, c):
    """
    6. Schreiben Sie eine Funktion, die prüft, ob eine Zahl in einer Liste erhalten ist.
    Jedes Element kann entweder eine Liste onder eine Zahl sein.
    """

    for el in l:
        if type(el) is list:
            if findlist(el, c):
                return True
        if el == c:
            return True

    return False
