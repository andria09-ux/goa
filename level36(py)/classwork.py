def digitize(n):
    reversed_res = []
    n = str(n)[::-1]
    for i in str(n):
        reversed_res.append(int(i))
    return reversed_res


def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    return sorted(test) == sorted(original)



def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = 0
    for i in sentence:
        for vowel in vowels:
            if i == vowel:
                count_vowels += 1
    return count_vowels