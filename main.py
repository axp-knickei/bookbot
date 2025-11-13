from stats import get_num_words
from stats import get_num_characters

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

#def number_of_words(contents):
#    words = contents.split()
#    return len(words)

def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    # print(file_contents)
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")

    total_character = get_num_characters(file_contents)
    print(total_character)

main()