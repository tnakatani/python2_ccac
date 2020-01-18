"""
Using Python’s CSV module, pull in data from gifts.csv, and create a dictionary where the keys
are the names, and the values are the gifts they like; print the dictionary to the console, nicely (every name and gift on its own line, neatly formatted).

Also create a list of (name, fav_gift) tuples. Print the list to the console, nicely.
"""

import csv

def print_dict(dictionary):
    for obj in dictionary:
        name = obj
        gift = dictionary[obj]
        template = '{} would like the following gift: {}'.format(name,gift)
        print(template)

def print_tuples(list_of_tuples):
    for i in list_of_tuples:
        name = i[0]
        gift = i[1]
        template = '{}: {}'.format(name,gift)
        print(template)

# Solution using DictReader
def convert_csv_1(csv_file):
    try:
        with open(csv_file) as f:
            dict_obj = csv.DictReader(f, delimiter=',')
            list_of_tuples = list()

            print('***Printing the dictionary***')
            for row in dict_obj:
                name = row['name']
                gift = row['fav_gift']

                template = '{} would like the following gift: {}'.format(name,gift)
                print(template)

                # Addtionally, populate list of tuples
                tuple_row = (name, gift)
                list_of_tuples.append(tuple_row)

            print('\n***Printing the list of tuples***')
            print_tuples(list_of_tuples)
    except IOError:
        print('IOError: File not found')

# Solution without DictReader
def convert_csv_2(csv_file):
    try:
        with open(csv_file) as f:
            reader = csv.reader(f)
            result = {}
            list_of_tuples = list()
            
            # Skip first row
            next(reader)

            # Populate dictionary / list of tuples
            for row in reader:
                key = row[0]
                value = row[1]
                tuple_row = (key,value)

                result[key] = value
                list_of_tuples.append(tuple_row)

            print('***Printing the dictionary***')
            print_dict(result)

            print('\n***Printing the list of tuples***')
            print_tuples(list_of_tuples)
    except IOError:
        print('IOError: File not found')

if __name__ == "__main__":
    print('-------Solution with DictReader-------')
    convert_csv_1('gifts.csv')
    print('\n-------Solution without DictReader-------')
    convert_csv_2('gifts.csv')
