# Code progress

- 13.11.2025 14:40: The main.py for calling is working. But I need to work on `get_num_characters` function. I am still having a problem in this function. Here is the latest error message.

```
Traceback (most recent call last):
  File "/home/axp433/workspace/github.com/axp-knickei/bookbot/main.py", line 23, in <module>
    main()
  File "/home/axp433/workspace/github.com/axp-knickei/bookbot/main.py", line 20, in main
    get_num_characters(file_contents)
  File "/home/axp433/workspace/github.com/axp-knickei/bookbot/stats.py", line 7, in get_num_characters
    onestringbook = char_no_duplicate.join()
                    ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: str.join() takes exactly one argument (0 given)
```


- 14.11.2025 01:32

Without telling me the answer, I would like to ask your assistance to give hints why I am having the error `KeyError: 't`

```python script
def get_num_characters(contents):
    char_no_duplicate = contents.lower()
    # Trying without `.join()` method
    ## onestringbook = char_no_duplicate.join()

    # Create an empty dictionary for storing character
    oneC_Dict = {}

    for character in char_no_duplicate:
        if character == oneC_Dict[character]:
            oneC_Dict[character] += 1
            return oneC_Dict
        else:
            oneC_Dict[character] = 1
            return oneC_Dict

    
    
    return oneC_Dict
```
```output
Traceback (most recent call last):
  File "/home/axp433/workspace/github.com/axp-knickei/bookbot/main.py", line 23, in <module>
    main()
  File "/home/axp433/workspace/github.com/axp-knickei/bookbot/main.py", line 20, in main
    get_num_characters(file_contents)
  File "/home/axp433/workspace/github.com/axp-knickei/bookbot/stats.py", line 14, in get_num_characters
    if character == oneC_Dict[character]:
                    ~~~~~~~~~^^^^^^^^^^^
KeyError: 't'
```