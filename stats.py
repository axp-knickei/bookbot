def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_num_characters(contents):
    char_no_duplicate = contents.lower()
    ## Trying without `.join()` method
    #onestringbook = char_no_duplicate.join()

    oneC_Dict = {}

    for character in char_no_duplicate:
        if character == oneC_Dict[character]:
            oneC_Dict[character] += 1
            return oneC_Dict
        else:
            oneC_Dict[character] = 1

    
    
    return oneC_Dict