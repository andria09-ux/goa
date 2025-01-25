def manual_difference(set1, set2):
    new_set = {}
    if set1 and set2 == set:
        for i in set1:
            for a in set2:
                if i == a:
                    return set1.remove(a)
                else:
                    return new_set.add(a)


manual_difference({"apple", "orange", "tengerene", "pear"}, {"apple", "banana", "orange"})


dict1 = {
    "age": 14,
    "score": 50,
    "name": "nika",
    "surname": "lobjanidze"
}

dict2 = {
    "age": 15,
    "score": 60,
    "name": "luka",
    "surname": "abesadze"
}

print(dict1, dict2)