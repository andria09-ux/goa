# def highest_lowest(_str):
#     res = _str.split(" ")
#     _arr = []
#     for elem in res:
#         _arr.append(int(elem))
#     return f"{ min(_arr) } { max(_arr) }"

# print(highest_lowest("1 2 3 4 5"))
#

def find_vowel(x):
    vowel = "a e i o u"
    if x in vowel:
        return "like"
    else:
        return "l bozo"

def find_vowel(x):
    vowel = "a e i o u"
    if x not in vowel:
        return "like"
    else:
        return "l bozo"


print(find_vowel("d"))
print(find_vowel("a"))
