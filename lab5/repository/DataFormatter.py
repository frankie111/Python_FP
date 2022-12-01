class DataFormatter:
    def __init__(self, file):
        self.__file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file = file

    def save(self, obj_list):
        pass

    def load(self):
        pass

    def read_file(self):
        file = open(self.file, 'r')
        content = file.read()
        file.close()
        return content

    def write_to_file(self, string):
        file = open(self.file, 'w')
        file.write(string)
        file.close()

    def convert_to_string(self, obj_list):
        pass

    def convert_from_string(self, string):
        pass
