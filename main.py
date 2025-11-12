# How to do for this step

# with Block
#with open(path_to_file) as f:
    # do something with f (the file) here

# The `with` block will automatically close the file when the block is exited

# .read() Method
# You can use the `.read()` method to read the contents of a file into a string
## f is a file object
#file_contents = f.read()

def get_book_text(file_path): # it takes fileparth as input and returns the contents of the file as a string
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    file_path = "/books/frankenstein.txt"

main()


