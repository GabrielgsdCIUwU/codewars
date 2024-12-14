def disemvowel(string_):
    vowels = ["a", "e", "i", "o","u", "A", "E", "I", "O", "U"]
    result = ""
    for letter in string_:
        if letter not in vowels:
            result += letter
    return result