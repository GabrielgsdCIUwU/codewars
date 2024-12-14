def mix(s1, s2):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    temp = []
    result = ""
    for letter in letters:
        counts2 = s2.count(letter)
        counts1 = s1.count(letter)
        
        if counts2 > counts1 and counts2 > 1:
            temp.append(f"2:{letter*counts2}")
            
        elif counts1 > counts2 and counts1 > 1:
            temp.append(f"1:{letter*counts1}")

        elif counts2 > 1 or counts1 > 1:
            temp.append(f"=:{letter*counts1}")

    temp.sort(key=lambda x: (-len(x), x))

    for differences in temp:
        result = result + f"/{differences}"
    
    return result[1:]