# Notes from challenge

## Improving ```parse_char()```

How to create a more dynamic function where the passed argument will flip the symbols that are returned?

## OOP approach to ```flip_list()``` 

Naming is awkward, as it also involves a conditional to determine whether or not to return a list or flipped list.  I initially created a ternary operator in the ```create_icon``` like below, but I thought it should be split off into its own function:

```py
for l in (reversed(lists) if flip == True else lists)
```
