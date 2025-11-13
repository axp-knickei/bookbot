def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_num_characters(contents):
    char_no_duplicate = contents.lower()
    onestringbook = char_no_duplicate.join()

    oneC_Dict = {}

    for oneC in onestringbook:
        if oneC == oneC:
            oneC_Dict[oneC] += 1
            return oneC_Dict
        else:
            oneC_Dict[oneC] = 1
    
    oneC_Dict = {oneC: count_oneC}
    
    return oneC_Dict
        
