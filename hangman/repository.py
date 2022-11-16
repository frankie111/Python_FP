import json

from hangman.state import HangState

repo_file = "repo.txt"
words_file = "words.txt"


def save_state(state):
    file = open(repo_file, 'w')
    json.dump(state.encode(), file)
    file.close()


def get_state():
    file = open(repo_file, 'r')
    state = HangState(j=json.load(file))
    file.close()
    return state


def add_word(word):
    file = open(words_file, 'a')
    file.write(word + '\n')
    file.close()


def get_words():
    file = open(words_file, 'r')
    words = []
    for line in file.readlines():
        words.append(line[0:len(line) - 1])
    file.close()
    return words
