def spin_words(sentence):
    
    MAX_LENGTH = 5
    return " ".join([word if len(word) < MAX_LENGTH else word[::-1] for word in sentence.split()])