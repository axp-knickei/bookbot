def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_num_characters(contents):
    char_no_duplicate = contents.lower()
    # Trying without `.join()` method
    ## onestringbook = char_no_duplicate.join()

    # Create an empty dictionary for storing character
    oneC_Dict = {}

    for character in char_no_duplicate:
        if character in oneC_Dict: # the `==` operator probably making problem. Instead use `in` and removing checking character through the dictionary.
            oneC_Dict[character] += 1
            #return oneC_Dict # return inside the loop causing problem. So it only runs for the first iteration.
        else:
            oneC_Dict[character] = 1
            #return oneC_Dict  
    return oneC_Dict


def sorted_dictionary(total_character):
    
    items = []

    for ch, ch_count in total_character.items():
        two_key_values.append({"char": ch, "num": ch_count})
    
    def sort_on(two_key_values):
        return item["num"]
    
    items.sort(reverse = True, key = sort_on)

    return two_key_values


#    .sort()

