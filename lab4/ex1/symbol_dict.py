file = "ex1/symbols.txt"


def add_symbol(sym, instructions):
    """
    Add a new symbol to the symbols.txt file if not existent
    :param sym: A string representing the key of the symbol
    :param instructions: A string containing the instructions needed to draw the symbol
    :return: None
    """
    dic = get_all_symbols()
    f = open(file, 'w')
    dic[sym] = instructions

    for key in dic.keys():
        f.write(str(key) + ' ' + str(dic[key]) + '\n')

    f.close()


def get_all_symbols():
    """
    Read all symbols from the symbols.txt file and compile them into a dictionary
    :return dic: A dictionary containing all symbols and the instructions on drawing them
    """
    dic = {}
    f = open(file, 'r')

    lines = f.readlines()
    for line in lines:
        space = line.split(' ')
        key = space[0]
        val = space[1].strip()
        dic[key] = val

    f.close()

    return dic
