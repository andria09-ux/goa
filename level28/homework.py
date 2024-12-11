# 1
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"         
# 2
    # ?
# 3
def string_to_number(s):
    if type(s) == str:
        return int(s)
# 4
def no_space(x):
    return x.replace(" ", "")
# 5
def remove_char(s):
    new_s = s.replace(s[0], "")
    newer_s = s.replace(new_s[-1], "")
    return newer_s
remove_char("country")
# ???