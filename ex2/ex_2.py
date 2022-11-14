def menu():
    path = input("Pfad zur Datei: ")
    word = input("Wort zu ersetzen: ")
    replacement = input("Ersatzwort: ")

    replacement_count = replace_in_file(path, word, replacement)
    if replacement_count != 0:
        print(f"Ersetzt '{word}' mit '{replacement}' an '{replacement_count}' Stellen")
    else:
        print(f"'{word}' wurde nicht in '{path}' gefunden")


def replace_in_file(path, word, replacement):
    """
    Replaces all occurrences of word in path with replacement
    :param path: Path to source file
    :param word: Word to be replaced
    :param replacement: replacement word
    :returns: The number of replacements
    """
    source_string = read_whole_file(path)
    replacement_res = replace_in_str(source_string, word, replacement)
    new_string = replacement_res[0]
    write_to_file(path, new_string)

    replacement_count = replacement_res[1]
    return replacement_count


def replace_in_str(string, word, replacement):
    """
    Replaces all occurrences of word in string with replacement
    :param string: Source string
    :param word: Word to replace
    :param replacement: replacement word
    :returns: [new_str, rep_count]: A tuple with the modified string and the replacements count
    """
    new_str = ""
    word_size = len(word)
    rep_count = 0
    i = 0

    while i < len(string):
        new_str += string[i]
        if string[i] == word[0]:
            if string[i: i + word_size] == word:
                new_str = new_str[:-1]
                new_str += replacement
                i += word_size
                rep_count += 1
                continue

        i += 1

    return new_str, rep_count


def read_whole_file(path):
    """
    Returns all text from the file at path
    :param path: path to the file
    :type path: str
    :return: txt: Text contents from path
    :rtype: str
    """
    file = open(path, 'r')
    txt = file.read()
    file.close()
    return txt


def write_to_file(path, txt):
    """
    Writes txt to the file at path
    :param path: Path to file
    :type path: str 
    :param txt: Text to write to file
    :type txt: str
    :return: None 
    """
    file = open(path, 'w')
    file.write(txt)
    file.close()
