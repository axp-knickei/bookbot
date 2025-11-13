def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_num_characters(contents):
    char_no_duplicate = contents.lower()
    onestringbook = char_no_duplicate.join()

    oneC_Dict = {}

    for oneC in onestringbook:
        count_oneC = 0
        if oneC == oneC:
            count_oneC =+ 1
            return count_oneC
        else:
            return count_oneC
    
    oneC_Dict = {oneC: count_oneC}
    
    return oneC_Dict
        
