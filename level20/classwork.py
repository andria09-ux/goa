num = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# for i in range(len(num)):
#     if num[i] % 2 != 0:
#         num = ["odd"]
#     else:
#         num = ["even"]
# print(num)

for i in range(len(num)):
    if num[i] % 2 == 0:
        num[i] = "even"
print(num)