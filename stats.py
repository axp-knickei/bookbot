def get_num_words(contents):
    words = contents.split()
    return len(words)

def get_num_characters(contents):
    char_no_duplicate = contents.lower()

    oneC_Dict = {}

    for character in char_no_duplicate:
        if character in oneC_Dict:
            oneC_Dict[character] += 1

        else:
            oneC_Dict[character] = 1
  
    return oneC_Dict


def sorted_dictionary(total_character):
    
    items = []

    for ch, ch_count in total_character.items():
        items.append({"char": ch, "num": ch_count})
    
    def sort_on(item):
        return item["num"]
    
    items.sort(reverse = True, key = sort_on)

    return items


