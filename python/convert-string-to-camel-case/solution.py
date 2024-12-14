def to_camel_case(text):
    result = ""
    next_Upper = -1

    for word_position in range(len(text)):
        if text[word_position] == "-" or text[word_position] == "_":
            next_Upper = word_position + 1
        elif word_position == next_Upper:
            result += text[word_position].upper()
        else:
            result += text[word_position]
    return result