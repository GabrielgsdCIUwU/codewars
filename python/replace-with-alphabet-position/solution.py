def alphabet_position(text):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = ''
    for letter in text:
        letter_lower = letter.lower()
        if letter_lower in alphabet:
            for letter_alphabet in alphabet:
                if letter_lower == letter_alphabet:
                    letter_value =  alphabet.index(letter_alphabet) + 1
                    if result == '': result = '{}'.format(letter_value)
                    else: result = '{} {}'.format(result, letter_value)
                    
    return result