from hangman.console import show_state, input_player, menu
from hangman.logik import process_input, reset_game
from hangman.repository import get_state


def game():
    running = True
    state = get_state()
    if state.lives == 0:
        print("Game Over! you are out of lives :(")
        running = False

    if state.is_complete():
        print(f"You won! The word was {state.word}")
        running = False

    while running:
        show_state(state)
        letter = input_player()
        result = process_input(state, letter)
        state = result[0]
        ret = result[1]

        match ret:
            case -1:
                running = False
                print("Game Over! you are out of lives :(")
            case 0:
                print(f"{letter} is wrong!")
            case 1:
                print(f"{letter} was already guessed!")
            case 2:
                print(f"{letter} is correct!")
            case 3:
                running = False
                print(f"You won! The word was {state.word}")

        print()
        state = get_state()


def run():
    option = menu()

    match option:
        case 1:
            reset_game()
            game()
            run()


run()
