# 2
def lovefunc( flower1, flower2 ):
    return True if (flower1%2==1 and flower2%2==0) or (flower1%2==0 and flower2%2==1) else False

# 4
def longest(a1, a2):
    combined_string = a1 + a2
    letters = []
    
    for letter in combined_string:
        if letter not in letters:
            letters.append(letter)
    
    letters.sort()
    result = "".join(letters)
    
    return result

