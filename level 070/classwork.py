def func1(num1 = 5, num2 = 5):
    return num1 + num2

print(func1())

name = lambda name: name + " hello"

print(name("luka"))

num = 0
while num < 10:
    print("goa best")
    num += 1


x = [3, -2, 6, 5, 1, -7, -4, 9, 11, 43]
num = []

for i in x:
    if i > 0:
        num.append(i)

for i in range(1, 10, 2):
    print(i)


class guy:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


guy1 = guy("john", "kenedy", 2002)

print(guy1.color, guy1.brand, guy1.year)