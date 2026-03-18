def longest_word(string_of_words):
    string_of_words = string_of_words.split(" ")
    longest_word = string_of_words[0]
    for word in string_of_words:
        if len(longest_word) <= len(word):
            longest_word = word
    return longest_word