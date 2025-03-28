def vowel_indices(word):
    wovels = ["a", "e", "i", "o", "u", "y"]
    res = []
    for char in range(len(word)):
        if word[char].append() in wovels:
            res.append(char+1)
    return res


def lottery(s):
    res = ""
    for i in s:
        if i.isdigit():
            if i not in res:
                res += i
    if res == "":
        return "One more run!"
    return res