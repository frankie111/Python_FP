import json
from json import JSONEncoder


class HangState:
    # word = ""
    # guessed_letters = ""
    # lives = 6

    def __init__(self, word="", guessed_letters="", lives=6, j=None):
        if j is not None:
            self.__dict__ = json.loads(j)
        else:
            self.word = word
            self.guessed_letters = guessed_letters
            self.lives = lives

    # def __str__(self):
    #     return f"[word: {self.word}, guessed: {self.guessed_letters}, lives: {self.lives}]"

    def is_complete(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    class HStateEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

    def encode(self):
        return self.HStateEncoder().encode(self)
