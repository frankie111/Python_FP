

def ub1(even_row):
    with open('zahlen.txt', 'r') as f:
        lines = f.readlines()
        numbers = [line.split('UBB') for line in lines]
        if even_row:
            numbers = list(filter(lambda x: all(int(num) % 2 == 0 for num in x), numbers))
        else:
            numbers = list(filter(lambda x: all(int(num) % 2 != 0 for num in x), numbers))
        return sum(map(lambda x: sum(map(int, x)), numbers))

# Test 1:
assert ub1(True) == 6

# Test 2:
assert ub1(False) != 6