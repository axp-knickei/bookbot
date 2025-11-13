# Refactoring

- [Link](https://www.boot.dev/lessons/bea7b054-305c-4d25-9464-97b6c5606e31) to the ecture for the refactoring module

Refactoring is a fancy word for "rewriting your god-awful cod so it's not so terrible." Refactoring doesn't change the behavior of your code, just the way *it's written*.

Let's refactor our project to use multiple Python files. Not only will it be useful for me to learn how to split code across files, but in this case, it will help me organize my code. This lecture will use this structure:

- `main.py` - The entry point to my program and any code that doesn't fit elsewehere
- `stats.py` - A file that contain functions for analyzing the text

## Assignment

- [ ] Move my function that counts the words into a new `stats.py` file.
- [ ] Import the function in my `main.py` file, it will look something like this:

```
from stats import get_num_words
```

*Where `stats` is the name of file (without the `.py` extension) and `get_num_words` is the name of the function I want to import*
