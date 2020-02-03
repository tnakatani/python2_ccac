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
    [0,1,0,1,1,1,0,1,0], # row 9
    [0,0,0,1,0,1,0,0,0]  # row 10
]

def line_break():
    """Helper function to create line breaks"""
    print('\n' + '-'*50 + '\n')

def parse_char(char, invert=False):
    """Return symbols depending on the binary input
    
    Keyword arguments:
    char   -- binary integer streamed into the function
    invert -- boolean to invert returned symbols
    """
    if invert == False:
        if char == 0:
            return '.'
        elif char == 1:
            return '@'
    if char == 0:
        return '@'
    elif char == 1:
        return '.'

def flip_list(lists, flip):
    """Return list as-is or in reversed order
    
    Keyword arguments: Inherited from create_icon
    """
    if flip == True:
        return reversed(lists)
    return lists

def create_file_name(scale=1, invert=False, flip=False):
    """Helper function to dynamically create a file name
    
    Keyword arguments: Inherited from create_icon
    """
    return ('icon_scaled_x' 
        + str(scale) 
        + ('_inverted' if invert == True else '') 
        + ('_flipped' if flip == True else '') 
        + '.txt')

def create_icon(lists, scale=1, invert=False, flip=False):
    """Create icon in a dynamically named text file with the ability to:
    1. Scale at n-times
    2. Invert symbols
    3. Flip icon 180 degres

    Keyword arguments:
    lists  -- input data to process, expects a list of lists
    scale  -- scale of the printed icon
    invert -- boolean to invert the binary symbols
    flip   -- boolean to flip icon 180 degrees
    """
    file_name = create_file_name(scale, invert, flip)
    print('Printing icon to ' + file_name + '...')
    with open(file_name,'w') as f:
        for l in flip_list(lists, flip):
            temp = list()
            for i in l:
                temp.append(parse_char(i,invert)*scale)
            for i in temp:
                f.write(''.join(temp) + '\n')

if __name__ == '__main__':
    create_icon(lists, 1)
    create_icon(lists, 3)
    create_icon(lists, 5, invert=True)
    create_icon(lists, 10, invert=True, flip=True)
