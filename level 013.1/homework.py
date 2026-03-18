name = input("input your name:")
result = ""
for i in name:
    print(i)
    i += result
# 2
idk = int(input("in range:"))
for i in range(idk):
    if idk % 2 and 3 == 0:
        print("ეს ციფრები არის 3-ისა და 2-ის ჯერადები")
    else:
        print("fuk u")
    print(i)
# 3 ver gavige
# 4
for i in range(-100, 100):
    if i > 0:
        print(i)
    else:
        print("lol")
# 5
guess = int(input("enter number:"))
if guess < 0:
    print("access granted")
else:
    print(int(input("try again:")))