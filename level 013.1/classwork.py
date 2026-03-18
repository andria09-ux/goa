name = "two tower"
result = ""
result += name

for i in name:
    print(i)
    result +=i

print(result)
# -----------------------------------------------------
# 1
number = int(input("input number:"))
if number % 2 ==0:
    print("even")
else:
    print("uneven")

# 2
for i in range(1, 100):
    if i % 2 == 0:
        print("even")
    else:
        print("uneven")
