"""
Purpose: Create a program in python that uses looping and basic data structures to display customized 10x10 student icons in various scales and orientations.

1. Create a data structure (list, tuple, dictionary) that can represent the sequence of on and off cells in each icon inside your python program

2. Read your custom data structure to display a visual representation of your icon using a single symbol, such as an asterisk or an at-sign.

3. Implement one or more transformations on a given icon, starting with scaling, such that each "cell" is represnted by not just one character, but a square of characters of a given size. Consider other transformations such as inverting on and off cells, or rotating by a specified amount of degrees

4. Review your code and break it up into as many sensible functions as possible, allowing for code re-use. Comment each function such that its purpose is clear to other users.

5. Post your code on your github account
"""

# create data structure in list form
lists = [
    [0,0,0,0,1,0,0,0,0], # row 1
    [0,0,1,1,1,1,1,0,0], # row 2
    [0,0,1,0,1,0,1,0,0], # row 3
    [0,0,1,1,1,1,1,0,0], # row 4
    [0,0,0,0,1,0,0,0,0], # row 5
    [0,0,1,0,1,0,1,0,0], # row 6
    [0,0,0,1,0,1,0,0,0], # row 7
    [0,0,1,0,0,0,1,0,0], # row 8
    [0,0,0,1,1,1,0,0,0], # row 9
    [0,0,0,1,0,1,0,0,0]  # row 10
]

def line_break():
    """
    Helper function to create line breaks
    """
    print('\n\n' + '-'*50 + '\n')

def parse_char(char):
    """
    Return binary characters depending on the input
    """
    if char == 0:
        return '.'
    elif char == 1:
        return '@'

def print_lists(lists):
    """
    Print the contents of the list sans newline
    """

    print('Solution #1: Basic Display using a counter')
    i = 0
    for l in lists:
        i += 1
        if i > 1:
            print()
        for char in l:
            print(parse_char(char), end='')

    line_break()

    print('Solution #2: Basic Display using join()')
    for l in lists:
        temp_list = []
        for i in l:
            temp_list.append(parse_char(i))
        print(''.join(temp_list))



if __name__ == "__main__":
    print_lists(lists)    