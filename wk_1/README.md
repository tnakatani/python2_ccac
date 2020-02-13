# Notes from challenge

## Improving ```parse_char()```

How to create a more dynamic function where the passed argument will flip the symbols that are returned?  The nested if statements doesn't seem that elegant.

Reference: [create_icon.py, line 37](https://github.com/tnakatani/python2_ccac/blob/master/wk_1/create_icon.py#L37)

## Streaming vs Reading Entire File

Consider a situation where the input file is much larger.  How could this code be refactored to stream incoming data rather than reading it?  Note to self: consider putting the list-of-lists in a separate text file, or just as a simple block of 10x10 binary numbers.
