# Notes from challenge

## Improving ```parse_char()```

How to create a more dynamic function where the passed argument will flip the symbols that are returned?  The nested if statements doesn't seem that elegant.

Reference: [create_icon.py, line 37](https://github.com/tnakatani/python2_ccac/blob/master/wk_1/create_icon.py#L37)

## Passing function arguments to nested functions

Rather than typing each argument down to the nested function, is there a way to pass these arguments without explicitly typing them?  Is ```kwargs``` the solution for this.

Reference: [create_icon.py, line 37](https://github.com/tnakatani/python2_ccac/blob/master/wk_1/create_icon.py#L37)

## Streaming vs Reading Entire File

Consider a situation where the input file is much larger.  How could this code be refactored to stream the incoming data rather than reading it?
