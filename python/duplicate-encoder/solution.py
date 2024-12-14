def duplicate_encode(word):
    
    return "".join(["(" if word.lower().count(letter) == 1 else ")" for letter in word.lower()])