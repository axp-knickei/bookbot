from stats import get_num_words
from stats import get_num_characters
from stats import sorted_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    
    num_words = get_num_words(file_contents)
    print("============= BOOKBOT ==============")
    print(f"Analyzing book found at {file_path}...")
    print("============= Word Count =============")
    print(f"Found {num_words} total words")

    total_character = get_num_characters(file_contents)
    # print(total_character)

    two_key = sorted_dictionary(total_character) 
    
    print("--------- Character Count ---------")
    for item in two_key:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()