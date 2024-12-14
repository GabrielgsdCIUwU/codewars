def solution(number):
    if number <= 0:
        return 0
    check = number - 1
    result = 0
    while check >= 3:
        if check % 3 == 0:
            result += check
        
        if check % 3 != 0:
            if check % 5 == 0:
                result += check
        
        check -= 1
    return result