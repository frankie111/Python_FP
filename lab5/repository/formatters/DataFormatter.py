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
        Converts a list of objects to a pickle string and writes it to self.__file
        :param obj_list:
        """
        self.write_to_file(self.convert_to_string(obj_list))

    def load(self):
        """
        Reads the pickle string from self.__file and converts it to a list of objects
        :returns: A list of objects | -1 if file is empty
        :rtype: list[Identifiable] | int
        """
        contents = self.read_file()
        if contents == "":
            return -1

        return self.convert_from_string(contents)

    def read_file(self):
        """
        Reads and returns the contents of self.__file
        :rtype: str
        """
        with open(self.__file, 'rb') as f:
            content = f.read()
            f.close()

        return content

    def write_to_file(self, content):
        """
        Writes content to self.__file
        :param content:
        """
        with open(self.__file, 'wb') as f:
            f.write(content)
            f.close()

    def clear_file(self):
        """
        Clears self.__file
        """
        open(self.__file, 'wb').close()

    def convert_to_string(self, obj_list):
        """
        Abstract method to be implemented in subclasses of DataFormatter.
        Converts a list of objects to a pickle string
        :param obj_list:
        :rtype: str
        """
        pass

    def convert_from_string(self, string):
        """
        Abstract method to be implemented in subclasses of DataFormatter.
        Converts a pickle string to a list of objects
        :param string:
        :rtype: list
        """
        pass
