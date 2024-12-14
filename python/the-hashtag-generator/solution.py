def generate_hashtag(s):
    if s == "":
        return False
    result = "#"
    split_words = s.split(" ")
    for words in split_words:
        if words != "":
            result = result + words[0].upper() + words[1:].lower()
    if len(result) > 140:
        return False
    return result