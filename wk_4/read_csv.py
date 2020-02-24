import json
import csv
import logging as log
#import pandas as pd

############################################################
# Helper Functions
############################################################

def lowercase_list(l):
    return [i.lower() for i in l]

def log_specifications(specification):
    print('querying the following specifications:\n'.upper())
    for spec, value in specification.items():
        msg = f'{spec.upper()} : {str(value)}'
        print(msg.upper())

def log_count(match):
    msg = (f'\nquery matched {count} rows:\n')
    print(msg.upper())

def log_status(message):
    div = "#"*80
    msg = (f'\n{div}\n{message}\n{div}\n')
    print(msg.upper())

############################################################
# Analysis Logic
############################################################

def create_null_table(dataset):
    """
    Return a frequency table of null values for each dataset key
    """
    null_table={}
    header = dataset.fieldnames

    next(dataset) # skip header
    for row in dataset:
        for item in header:
            if not row[item]: # using 'implicit booleanness'
                if item in null_table:
                    null_table[item] += 1
                else:
                    null_table[item] = 1
            else:
                if item not in null_table:
                    null_table[item] = 0
    return null_table

def fields_exist_in_row(row, specification):
    """
    Returns boolean of whether row contains field that matches specifications
    for each key

    ToDo: How to iterate this without specifying key values?
    """
    statuses = lowercase_list(specification['status'])
    neighborhoods = lowercase_list(specification['neighborhood'])
    fiscal_years = str(specification['fiscal_year'])
    areas = lowercase_list(specification['area'])
    if row['status'].lower() in statuses \
            and row['neighborhood'].lower() in neighborhoods \
            and row['fiscal_year'] in fiscal_years \
            and row['area'].lower() in areas:
        return True

def query_dataset(dataset, specification):
    """
    Read specification from specification file, and return only rows that meet
    its specifications

    - A blank value in any specified query for a column/field will disqualify
      that record from inclusion in the results
    - Empty string: do not limit results by this specification at all
    """
    matched_rows = []
    matched_count = 0

    next(dataset) # skip header
    # loop through each row
    for row in dataset:
        # loop through each spec
        for spec in specification:
            # skip any values where there is an empty field
            if row[spec] == '':
                continue
            elif fields_exist_in_row(row, specification):
                matched_count += 1
                matched_rows.append(row)
    return matched_rows, matched_count

if __name__ == '__main__':
    log_status('return frequency table of null values for each key')

    with open('./data/pgh_capital_projects.csv') as d, \
        open('search_criteria.json') as c:
        dataset = csv.DictReader(d)
        specification = json.load(c)

        print(create_null_table(dataset))

    log_status('return rows that meets the imported specifications')
    with open('./data/pgh_capital_projects.csv') as d, \
        open('search_criteria.json') as c:
        dataset = csv.DictReader(d)
        specification = json.load(c)

        rows, count = query_dataset(dataset, specification)
        log_specifications(specification)
        log_count(count)
        for row in rows:
            print(row)


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

