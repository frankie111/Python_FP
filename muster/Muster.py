from functools import reduce


def ub1(subject):
    with open("text.txt", 'r') as file:
        lines = file.readlines()
        lines = list(filter(lambda line: line.split(',')[2] == subject, lines))
        average = reduce(lambda suma, line: suma + int(line.split(',')[3]), lines, 0) / len(lines)
        return average


# print(ub1("Advanced programming"))

def working_test():
    assert ub1("Advanced programming") == 8.166666666666666


def fail_test():
    assert ub1("Acting 101") == 9


# working_test()
# fail_test()

class NoMoneyError(Exception):
    def __init__(self, message):
        self.message = message


class BankAccount:
    def __init__(self, owner):
        self.amount = 0
        self.owner = owner

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.amount:
            raise NoMoneyError("No money")

        return self.amount - withdrawal_amount


class CreditBankAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)
        self.credit_score = 1

    def withdraw(self, withdrawal_amount):
        try:
            dif = super().withdraw(withdrawal_amount)
            self.credit_score += 1
        except NoMoneyError as e:
            print(e.message)
            self.credit_score -= 1
            dif = -1

        return dif

    def __add__(self, other):
        new = CreditBankAccount(self.owner)
        new.amount = self.amount + other.amount
        new.credit_score = self.credit_score + other.credit_score
        return new


acc1 = CreditBankAccount("Mircea")
acc1.amount = 30
acc2 = CreditBankAccount("Gion")
# acc2.amount = 20
acc2.withdraw(400)

acc3 = acc1 + acc2
# print(f"{acc3.owner} {acc3.amount}")

def my_func(n):
    if n in (0, 1):
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def my_func_rec(n):
    if n in (0, 1):
        return n

    return my_func_rec(n - 1) + my_func_rec(n - 2)
