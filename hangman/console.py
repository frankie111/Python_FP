def show_word(word, guessed_letters):
    output = "Word: "
    for letter in word:
        if letter in guessed_letters:
            output += letter
        else:
            output += '_'

    print(output)


def input_player():
    return input("Enter a letter: ")


def show_state(state):
    show_word(state.word, state.guessed_letters)
    print(f"Lives: {state.lives}/6")


def menu():
    option = int(input("1. Play hangman \n2. Exit\n"))
    return option
