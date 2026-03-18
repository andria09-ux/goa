# 3
def binary_array_to_number(arr):
    # return int(''.join(map(str, arr)), 2)
    _str = ""
    for digit in arr:
        _str += str(digit)
    return int(_str, 2)


# print(binary_array_to_number([0, 0, 0, 1]))
# print(binary_array_to_number([0, 0, 1, 0]))
# print(binary_array_to_number([0, 1, 0, 1]))
# print(binary_array_to_number([1, 0, 0, 1]))
# print(binary_array_to_number([0, 0, 1, 0]))
# print(binary_array_to_number([0, 1, 1, 0]))
# print(binary_array_to_number([1, 1, 1, 1]))
# print(binary_array_to_number([1, 0, 1, 1]))

# 4
def min_max(lst):
    return [min(lst), max(lst)]

# 5
def divisors(int):
    arr = []
    for i in range(2, int):
        if int % i == 0:
            arr.append(i)
    if not arr:
        return f'{int} is prime'
    else:
        return arr