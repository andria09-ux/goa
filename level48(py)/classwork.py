def xo(s):
    return s.lower().count("x") == s.lower().count("o")

def find_short(s):
    split_words = s.split(" ")
    arr = []
    word_length = len(split_words[0])
    for word in split_words:
        if len(word) < word_length:
            word_length = len(word)
    return word_length
    
def solution(text, ending):
    return text[-len(ending):] == ending
def solution(text, ending):
    return text.endswith(ending)

