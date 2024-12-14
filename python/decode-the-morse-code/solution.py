from preloaded import MORSE_CODE

def decode_morse(morse_code):
    morse_code = morse_code.strip()
    
    result = ""

    while morse_code != "":
        next_letter = morse_code.find(" ")
        next_space = morse_code.find("  ")

        if next_space != -1 and next_letter == 0:
            result += " "
            morse_code = morse_code[2:]
        else:
            if next_letter == -1:
                result += MORSE_CODE[morse_code]
                break;

            else:
                result += MORSE_CODE[morse_code[:next_letter]]
                morse_code = morse_code[next_letter+1:]


        
    return result