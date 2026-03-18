def filter_list(l):
    arr = []
    for i in l:
        if type(i) == int:
            arr.append(i)
    return arr


def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    rest = ""
    for char in string_:
        if not char in vowels:
            rest += char
    return rest


