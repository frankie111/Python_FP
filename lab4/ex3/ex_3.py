import random

ascii_path = "lab4/ex3/rps_ascii.txt"


def menu():
    drawings_dict = load_ascii_drawings(ascii_path)
    results = [0, 0]

    for i in range(1, 4):
        print(f"Runde {i}/3: " + ' ' * 20 + f"Scor Spieler-Computer: {results[1]} - {results[0]}")
        result = rps_round(drawings_dict)

        print(f"Runde {i}: ")
        match result:
            case 0:
                print("Gleichheit!")
            case 1:
                print("Du hast verloren!")
                results[0] += 1
            case 2:
                print("Du hast gewonnen!")
                results[1] += 1

    print()
    if results[0] == results[1]:
        print("Gleichheit! ")
    elif results[0] > results[1]:
        print("Du hast verloren!")
    elif results[0] < results[1]:
        print("Du hast gewonnen!")
    print()


def rps_round(drawings_dict):
    """
    Plays a round of Rock, Paper, Scissors and returns the result
    :param drawings_dict:
    :return:
    """
    computer_opt = get_random()
    player_opt = input("Wähle aus: Schere(r), Stein(s) oder Papier(p): ")
    print(drawings_dict[computer_opt])
    result = get_winner(computer_opt, player_opt)
    return result


def get_winner(o1, o2):
    """
    Get the winner in Rock, Paper, Scissors between o1, o2:
    :param o1: option 1
    :type o1: str
    :param o2: option 2
    :type o2: str
    :returns: 0 -> draw, 1 -> player1, 2 -> player2
    """
    if o1 == o2:
        return 0

    if o1 == 'r':
        if o2 == 's':
            return 1
        else:
            return 2

    if o1 == 'p':
        if o2 == 'r':
            return 1
        else:
            return 2

    if o1 == 's':
        if o2 == 'p':
            return 1
        else:
            return 2


def get_random():
    """
    Returns a random choice from [r, p, s]
    :return: 'r' or 'p' or 's' randomly
    """
    options = ['r', 'p', 's']
    return random.choice(options)


def load_ascii_drawings(path):
    """
    Reads ascii drawings from path and returns a dictionary with 3 pairs representing Rock, Paper and Scissors
    :return:
    """
    file = open(path)
    lines = file.readlines()
    rps = []
    sign = ""
    for line in lines:
        if line[0] != "*":
            sign += line
        else:
            rps.append(sign)
            sign = ""

    drawings_dict = {'r': rps[0], 'p': rps[1], 's': rps[2]}

    return drawings_dict
