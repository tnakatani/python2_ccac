# Notes from challenge

## Improving ```parse_char()```

How to create a more dynamic function where the passed argument will flip the symbols that are returned?

## OOP approach to ```flip_list()``` 

Naming is awkward, as it also involves a conditional to determine whether or not to return a list or flipped list.  I initially created a ternary operator in the ```create_icon``` like below, but I thought it should be split off into its own function:

```py
for l in (reversed(lists) if flip == True else lists)
```

## Passing function arguments to nested functions

Rather than typing each argument down to the nested function, is there a way to pass these arguments without explicitly typing them?  Is ```kwargs``` the solution for this.

## Streaming vs Reading Entire File

Consider a situation where the input file is much larger.  How could this code be refactored to stream the incoming data rather than reading it.
