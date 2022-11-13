def show_word(word, found_letters):
    output = ""
    for letter in word:
        if letter in found_letters:
            output += letter
        else:
            output += '_'

    print(output)


def input_player():
    return input("Enter a letter: ")


def menu(word, found_letters, lives):
    show_word(word, found_letters)
    print("lives left: " + str(lives))
    return input_player()
