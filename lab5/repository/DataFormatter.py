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
        """
        Converts a list of objects to a JSON string and writes it to self.__file
        :param obj_list:
        """
        self.write_to_file(self.convert_to_string(obj_list))

    def load(self):
        """
        Reads the JSON string from self.__file and converts it to a list of objects to be returned
        :return:
        """
        return self.convert_from_string(self.read_file())

    def read_file(self):
        """
        Reads and returns the contents of self.__file
        """
        file = open(self.file, 'r')
        content = file.read()
        file.close()
        return content

    def write_to_file(self, content):
        """
        Writes content to self.__file
        :param content:
        """
        file = open(self.file, 'w')
        file.write(content)
        file.close()

    def convert_to_string(self, obj_list):
        """
        Abstract method to be implemented in subclasses of DataFormatter.
        Converts a list of objects to a JSON string
        :param obj_list:
        :return:
        """
        pass

    def convert_from_string(self, string):
        """
        Abstract method to be implemented in subclasses of DataFormatter.
        Converts a JSON string to a list of objects
        :param string:
        :return:
        """
        pass