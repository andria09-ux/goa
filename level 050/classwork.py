def monkey_count(n):
    return [i for i in range(1, n+1)]

def is_isogram(string):
    arr = [i for i in string.lower() if string.lower().count(i) > 1]
    return arr

