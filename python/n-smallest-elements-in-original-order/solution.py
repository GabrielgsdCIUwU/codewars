def first_n_smallest(array, number_length):
    search_n_smallest = sorted(array[:])[:number_length]
    return [search_n_smallest.pop(search_n_smallest.index(number)) for number in array if number in search_n_smallest]