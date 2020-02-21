import json
import csv
import pandas as pd

def value_is_empty(row, item):
    return row[item] == ''

def return_null_table(dataset):
    """
    Return a frequency table of null values for each dataset key
    """
    null_table={}
    header = dataset.fieldnames
    # skip header
    next(dataset)
    for row in dataset:
        for item in header:
            #if value_is_empty(row,item):
            if row[item] == '':
                if item not in null_table:
                    null_table[item] = 1
                else:
                    null_table[item] += 1
            else:
                if item not in null_table:
                    null_table[item] = 0
    return null_table

def return_filtered_table(dataset, specification):
    """
    Read specification from specification file, and return only rows that meet
    its specifications

    - A blank value in any specified query for a column/field will disqualify
      that record from inclusion in the results
    - Empty string: do not limit results by this specification at all
    """
    match_table = {}
    header = dataset.fieldnames
    for row in dataset:
        for item in header:
            if row[item] == '':
                continue
        if row['status'] == specification['status'][0] and \
            row['neighborhood'] == specification['neighborhood'][0]:
            print(row)


    # try to loop through each list of specs and use each as a combination
    # of conditions (ie. status - completed and neighborhood - shadyside,
    # status - completed and neighborhood - squirrel hill
    for spec in specification:
        print(specification[spec])
       
        # this is more or less an "or" condition for any specification
        # for item in specification:
        #     if row[item] == specification[item][0]:
        #         print('result',row)
        

if __name__ == '__main__':
    """ Vanilla Python """
    print('Vanilla Python')

    with open('./data/pgh_capital_projects.csv') as d, \
        open('search_criteria.json') as c:
        dataset = csv.DictReader(d)
        specification = json.load(c)

        # Return null table
        print("\nReturn null table:")
        # print(return_null_table(dataset))

        # Return rows that meets the imported specification
        print("\nReturn rows that meets the imported specification")
        return_filtered_table(dataset, specification)


    """ Pandas version"""
    """
    print('\nPandas version:')
    df = pd.read_csv('data/pgh_capital_projects.csv')
    
    # return_null_table
    print("\nReturn null table:")
    print(df.isnull().sum())
    """

# mock json
# {"fiscal_year": [2018], "start_date": [""], "area": [""], "asset_type": [""],  "status": [""]}

