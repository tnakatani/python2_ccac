"""
Prompt the user for two words and for two numbers.

If the user makes a mistake (e.g. putting in a word where a number is expected), give them useful feedback and a chance to fix it.

Write a function that takes those inputs as parameters. Your function should loop through all of the numbers from 1 through 100. For each number, if it is divisible by the user’s first number, you should print the user’s first word; if it is divisible by the user’s second number, you should print the user’s second word; if it is divisible by both of the user’s numbers, you should print both words; and if it is not divisible by either, you should print the number itself.
"""

def get_input():
    while True:
        try:
            num_1 = int(input('Please provide number #1: '))
            num_2 = int(input('Please provide number #2: '))
            break
        except ValueError:
            print("Not a valid number, try again")
    
    while True:
        try:
            animal_1 = input('Please provide animal name #1: ')
            animal_2 = input('Please provide animal name #2: ')
            if animal_1.isdigit() | animal_2.isdigit():
                raise ValueError('Not an animal name')
            break
        except ValueError as e:
            print("Not a valid string, try again")
    
    output = [num_1,num_2,animal_1,animal_2]
    print("OK, your provided inputs are:", *output, sep=", ") 
    return output


def print_num(inputs):
    numbers = range(1,101)
    for i in numbers:
        if i%inputs[0] == 0:
            print(inputs[2])
        elif i%inputs[1] == 0:
            print(inputs[3])
        else:
            print(i)

if __name__ == "__main__":
    user_input = get_input()
    print_num(user_input)
