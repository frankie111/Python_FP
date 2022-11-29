from lab5.models.Meal import Meal


class Drink(Meal):
    def __init__(self, alcohol_content):
        super().__init__()
        self.__alcohol_content = alcohol_content

    @property
    def alcohol_content(self):
        return self.__alcohol_content

    @alcohol_content.setter
    def alcohol_content(self, alcohol_content):
        self.__alcohol_content = alcohol_content
