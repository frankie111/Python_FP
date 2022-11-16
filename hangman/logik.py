import random

from hangman.repository import save_state, get_words
from hangman.state import HangState


def process_input(state, letter):
    """
    Processes a new letter inputted by the player.
    :param state:
    :param letter:
    :returns: -1 if game is over,
              1 if a duplicate letter was inputted,
              2 if a correct letter has been guessed,
              3 if game is won
    """
    res = 0
    if letter not in state.word:
        state.lives -= 1
        if state.lives == 0:
            res = -1
    else:
        if letter not in state.guessed_letters:
            state.guessed_letters += letter
            res = 2
        else:
            res = 1

    if state.is_complete():
        res = 3

    save_state(state)
    return [state, res]


def reset_game():
    word = random.choice(get_words())
    new_state = HangState(word, "", 6)
    save_state(new_state)
