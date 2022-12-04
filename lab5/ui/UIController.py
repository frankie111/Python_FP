def cls():
    print('\n' * 100)


def header(title, sym='-'):
    print()
    print(sym * (len(title) // 2) + title + sym * (len(title) // 2))


def footer(title, sym='-'):
    print(sym * (2 * (len(title) - len(sym))))


def tooltip(tip):
    print(f"~~Tip: {tip}~~")


def warning(warn):
    print(f"!!{warn}!!")


def invalid(msg="ungültige Option"):
    warning(msg)


def menu(title, options, sym='-'):
    """
    Prints a menu
    :param sym: Symbol for header line
    :param title: Title of the menu
    :param options: A list of options to be displayed
    :returns: the selected option
    """
    header(title, sym)

    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    footer(title, sym)
    return input("->")
