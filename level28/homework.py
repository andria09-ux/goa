# 1
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"         
# 2
def remove_char(s):
    return s[1: -1]
# 3
def string_to_number(s):
    if type(s) == str:
        return int(s)
# 4
def no_space(x):
    return x.replace(" ", "")
# 5
def sum_array(a):
    counter = 0
    for num in a:
#         counter = counter + num
        counter += num
    return counter
######
def sum_array(a):
    counter = 0
    for i in range(len(a)):
        counter += a[i]
    return counter
# ???