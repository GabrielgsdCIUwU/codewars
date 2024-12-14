def comp(array1, array2):
    
    if array1 == [] and array2 == []:
        return True
    
    if not array1 or not array2:
        return False
    
    for num in array1:
        timesAppearInA1 = array1.count(num)
        timesAppearInA2 = array2.count(num**2)
        if timesAppearInA1 != timesAppearInA2:
            return False

    return True