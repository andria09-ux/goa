def dec_to_bi(num):
    arr = ""
    while num / 2:
        if num / 2 == int:
            arr += "1"
        elif num / 2 == float:
            arr += "0"
    return arr

# print(dec_to_bi(15))

def to_binary(x):
    arr = []
    while x > 0:
        bin = x % 2
        arr.append(str(bin))
        x = x // 2
    return "".join(arr[::-1])

print(to_binary(120))

print(bin(5))