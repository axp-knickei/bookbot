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