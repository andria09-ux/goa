# 1
def sum_mix(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum

# 2
def double_char(s):
    doubled = ""
    for char in s:
        doubled += char * 2
    return doubled

# 3
def array_plus_array(arr1,arr2):
    sum = 0
    for i in arr1:
        sum += i
    for i in arr2:
        sum += i
    return sum

# 4 ?

# 5
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    new_a = int(a)
    new_b = int(b)
    sum = new_a + new_b
    return str(sum)