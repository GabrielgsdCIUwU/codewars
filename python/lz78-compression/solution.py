def encoder(data):
    dictionary = {
        0: '',
    }


    def getKey(findValue):
        for key, value in dictionary.items():
            if value == findValue:
                return str(key)
        return "0"

    output = ""
    outputIndex = "0"
    bagLetters = ""
    for i in range(len(data)):
        
        nextLetter = data[i]
        bagLetters += nextLetter
        
        if bagLetters in dictionary.values():
            outputIndex = getKey(bagLetters)
            continue
        
        dictionaryNextKey =  max(dictionary.keys()) + 1
        dictionary[dictionaryNextKey] = bagLetters

        if len(bagLetters) == 1:
            outputIndex = "0"
        
        bagLetters = ""
        output += outputIndex + nextLetter
    
    if bagLetters != "":
        output += outputIndex

    return output


def decoder(data):
    dictionary = {
        0: ''
    }
    output = ""
    key = "0"
    for i in range(len(data)):
        if data[i].isdigit():
            key += data[i]
            if len(data) == i + 1:
                output += dictionary[int(key)] 
        else:
            dictionaryKey = int(key)
            letters = dictionary[dictionaryKey] 
            value = letters + data[i]

            dictionary[max(dictionary.keys()) + 1] = value
            output += value

            key = ""
    return output 