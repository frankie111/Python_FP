def cls():
    print('\n' * 100)


def header(title):
    print()
    print('-' * (len(title) // 2) + title + '-' * (len(title) // 2))


def footer(title):
    print('-' * 2 * len(title))


def tooltip(tip):
    print(f"~~{tip}~~")


def warning(warn):
    print(f"!!{warn}!!")


def menu(title, options):
    """
    Prints a menu
    :param title: Title of the menu
    :param options: A list of options to be displayed
    :returns: the selected option
    """
    header(title)

    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    footer(title)
    return input("->")
