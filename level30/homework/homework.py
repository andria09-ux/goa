# 1

#    ?

# 2

#    ?

# 3
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum
# 4

# 5
def count_positives_sum_negatives(arr):
    if (len(arr) == 0 ):
        return []
    count_of_positives = 0
    sum_of_negatives = 0
    
    for el in arr: 
        if el > 0:
            count_of_positives += 1
        else:
            sum_of_negatives += el
    return [count_of_positives, sum_of_negatives]