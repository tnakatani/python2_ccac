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
    output = get_input()
    print_num(output)
