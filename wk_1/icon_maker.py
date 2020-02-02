"""
1. Create a program in python that uses looping and basic data structures to display customized 10x10 student icons in various scales and orientations.

2. Create a data structure (list, tuple, dictionary) that can represent the sequence of on and off cells in each icon inside your python program

3. Read your custom data structure to display a visual representation of your icon using a single symbol, such as an asterisk or an at-sign.

4. Implement one or more transformations on a given icon, starting with scaling, such that each "cell" is represnted by not just one character, but a square of characters of a given size. Consider other transformations such as inverting on and off cells, or rotating by a specified amount of degrees

5. Review your code and break it up into as many sensible functions as possible, allowing for code re-use. Comment each function such that its purpose is clear to other users.

6. Post your code on your github account
"""

# create data structure in list form
bits = [
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

print(len(bits))

print('iterating through lists in bits')
for lists in bits:
  print('\n')
  for char in lists:
    print(char, end="")

