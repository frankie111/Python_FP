def str_find(target, source):
    target_len = len(target)
    source_len = len(source)
    for i in range(target_len):
        if target[i] == source[0]:
            if target[i: i + source_len] == source:
                return i + 1

        if target_len - i < source_len:
            break

    return -1


# print(str_find("testing", "ing"))


def caesar_encrypt(string, x):
    verschlusselt = ""
    for char in string:
        if char < 'd':
            char1 = chr(ord(char) - (26 - x))
        else:
            char1 = chr(ord(char) + x)
        verschlusselt += char1
        return verschlusselt


result = caesar_encrypt("string", 1)
print(result)
