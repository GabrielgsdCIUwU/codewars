def repeats(array):
    from functools import reduce
    return reduce((lambda x, y: x + y), [number for number in array if array.count(number) == 1] )