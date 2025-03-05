# 1
def multi_table(number):
    table = ""
    for i in range(1, 11):
        table += "i * number = i * number\n"
    return table

# 2

# 3
def string_clean(s):
    cleaned_string = ""
    for i in s:
        if not i.isdigit():
            cleaned_string += i
    return cleaned_string

# 4

# 5
def between_extremes(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return (largest - smallest)