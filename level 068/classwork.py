# num1 = 5
# number = lambda num1 : num1 + 10
# print(number(10))
# print(number(15))

# def func(n1):
#     return n1+5

# print(func(10))


# def func2(x):
#     x = lambda z : z + x
#     return x

# print()
# print(func2(2))

# lambda
# num = lambda n1, n2, n3 : n1 + n2 + n3
# print(num(3, 2, 5))

#function
# def num(n1, n2, n3):
#     return n1 + n2 + n3

# print(num(3,2,5))


x = lambda n1, n2, n3 : (n1 + n2 + n3) / 3
z = x(2,3,5)
print(z)
print(x(2,3,5))