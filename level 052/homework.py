# 1
def multi_table(number):
    _str = ""
    for num in range(1, 11):
        if num != 10:
            _str += f"{num} * {number} = {num * number}\n"
        else:
            _str += f"{num} * {number} = {num * number}"
    return _str
# 2

# 3
def string_clean(s):
    cleaned_string = ""
    for i in s:
        if not i.isdigit():
            cleaned_string += i
    return cleaned_string

# 4
def remove_consecutive_duplicates(s):
    splied_words = s.split(" ")
    result_arr = []
    for i in range(len(splied_words)):
        if (splied_words[i] != splied_words[i-1]) or (i == 0):
            result_arr.append(splied_words[i])
    return " ".join(result_arr)

# 5
def between_extremes(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return (largest - smallest)