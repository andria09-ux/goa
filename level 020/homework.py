# 1
array = ["a", "b", "c", "d", "e", "f", "g"]
print(array[0])
print(array[4])
# 2
array = [10, 15, 20, 25, 30]
for i in range(len(array)):
    if array[i] % 5 or array[i] % 3 == 0:
        array[i] = "even"
print(array)
# 3
arr = ["a", "d", "d", "f", "f", "s", "a", 'y']
arr_of_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
counter_of_vowels = 0

for char in arr:
    for vowel in arr_of_vowels:
        if char == vowel:
            counter_of_vowels += 1
print(counter_of_vowels)
# 
# 4
for i in range(1, 5):
   print(i * " " + "******") # OMFGGGGGGGGGG I DID IT
# 5
age = int(input("your age:"))
if age > 12:
    print("შენ არ ხარ 12 წლის")
else:
    print("grow up first :p")
