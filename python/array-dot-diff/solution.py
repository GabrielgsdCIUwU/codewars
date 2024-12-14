def array_diff(a, b):
    result_array = []
    for number in a:
        if number not in b:
            result_array.append(number)
    return result_array