# 3
def password(st):
    if len(st) < 8:
        return False
    is_upper = False
    is_lower = False
    is_digit_num = False
    for char in st:
        if char.isdigit():
            is_digit_num = True
        if char.islower():
            is_lower = True
        if char.isupper():
            is_upper = True
    return is_upper and is_lower and is_digit_num
            
# 4
