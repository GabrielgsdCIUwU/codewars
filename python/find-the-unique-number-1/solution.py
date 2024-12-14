def find_uniq(arr):    
    numberDuplicates = []
    numberNotRepeated = []
    for number in arr:
        if number not in numberDuplicates:
            if number not in numberNotRepeated:
                numberNotRepeated.append(number)
        
                n = numberNotRepeated
            else:
                numberDuplicates.append(number)
                numberNotRepeated.remove(number)
    return n[0]