def merge(*dictionaries):
    
    result = {}
    for dict in dictionaries:
        for keys in dict.keys():
            if keys in result:
                result[keys] = sorted(result[keys] + [dict[keys]])
            else:
                result[keys] = [dict[keys]]
    return result