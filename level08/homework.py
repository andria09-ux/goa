# 1.
age = int(input("input your age:"))
print(age > 13 or False)
print(age < 19 or False)
# 2.
grade = int(input("input your grade:"))
is_A = grade >= 9 or False
is_B = grade >= 8 or False
is_C = grade >= 7 or False
is_D = grade >= 6 or False
is_F = grade >= 5 or False
print(is_A, is_B, is_C, is_D, is_F)
# 3. ver gavige 😭
a = True
b = False
print(a or b)
print(a and b)
# 4.
a = int(input("input the first number:"))
b = int(input("input the second number:"))
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)
# 5.
print("---------------------------")
a = 6
b = 4
c = 2
is_a_greatest = a > b and True
is_b_middle = b > c and True
is_c_least = c < b and True
print(is_a_greatest)
print(is_b_middle)
print(is_c_least)
# 6.
print("---------------------------")
score = 99
is_pass = score > 50 and True
is_high_pass = 75 < score > 90 and True
is_perfect = score == 100 and True
is_failing = score < 50 and True
print(is_pass)
print(is_high_pass)
print(is_perfect)
print(is_failing)
# 7.
print("-----------------------------")
P = True
Q = False
P_and_not_Q = P == True, Q == False and True
not_P_and_Q = P == False, Q== True and True
P_xor_Q = P == True, Q == True and True
print(P_and_not_Q)
print(not_P_and_Q)
print(P_xor_Q)


