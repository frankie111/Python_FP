repo_file = "Repo.txt"

word = "hangman"
found_letters = ""
lives = 6


def fetch_data():
    file = open(repo_file, "r+")
    global word, found_letters, lives
    word = file.readline()
    found_letters = file.readline()
    lives = int(file.readline())


def get_word():
    return word


def get_lives():
    return lives


def get_found_letters():
    return found_letters


def decrement_lives():
    global lives
    lives -= 1


def add_letter(letter):
    global found_letters
    if letter in word:
        if letter not in found_letters:
            found_letters += letter
    else:
        decrement_lives()


fetch_data()
print(word)
print(lives)
print(found_letters)