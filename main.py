import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sorted_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]


def main():
    # file_path = "./books/frankenstein.txt"
    file_contents = get_book_text(path_to_book)
    
    num_words = get_num_words(file_contents)
    print("============= BOOKBOT ==============")
    print(f"Analyzing book found at {path_to_book}...")
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