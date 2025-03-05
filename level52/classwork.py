def find_next_square(sq):
    if sq**.5 % 1 == 0:
        return ((sq ** .5)+1)**2
    else:
        return -1


def min_max(lst):
    arr = []
    return [min(lst), max(lst)]