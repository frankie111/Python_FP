file = "symbols.txt"


def add_symbol(sym, inst):
    """
    Add a new symbol to the symbols.txt file if not existent
    :param sym: A string representing the key of the symbol
    :param inst: A string containing the instructions needed to draw the symbol
    :return: None
    """
    f = open(file, 'a')
    dic = get_all_symbols()
    dic[sym] = inst
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
        space = line.find(' ')
        key = line[0: space]
        val = line[space + 1: -1]
        dic[key] = val

    f.close()

    return dic
