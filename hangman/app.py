from hangman.console import menu
from hangman.repository import get_word, get_found_letters, get_lives, add_letter

running = True


def run():
    while running:
        letter = menu(get_word(), get_found_letters(), get_lives())
        add_letter(letter)


run()
