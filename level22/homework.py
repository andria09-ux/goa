# 1
list_of_names = ["andria", "andria", "ani", "lado", "andria"]
print(list_of_names.count("andria"))
# 2
arr = [1,2,3,4,5,6,7,8,9]
arr.reverse()
print(arr)
# 3
list_of_numbers = [1, 2, 3]
len_list_of_numbers = len(list_of_numbers)
res = []
for i in range(len_list_of_numbers):
    for repeat_i in range(len_list_of_numbers):
        res.append(list_of_numbers[repeat_i])
print(res)
# 4
insert_arr = ["nika", "andria", "deme", "mari", "barbare"]
insert_arr.insert(4, "dato")
print(insert_arr)
# 5
arr = ["andria", "andria", "ani", "lado", "andria"]
print(arr.count("andria"))
arr.remove("andria")
print(arr)
arr.insert(1, "nika")
print(arr)