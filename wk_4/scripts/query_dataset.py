import json
import csv
import os

############################################################
# Log Functions
############################################################

def log_specifications(specification):
    print('\nquerying the following specifications:\n'.upper())
    for spec, value in specification.items():
        msg = f'{spec.upper()} : {str(value)}'
        print(msg)

def log_count(match):
    msg = (f'\nquery matched {match} rows')
    print(msg.upper())

def log_status(message):
    div = "#"*80
    msg = (f'\n{div}\n{message}\n{div}')
    print(msg.upper())

def log_output_path(output):
    msg = f'\nOutput written to: '.upper() + output
    print(msg)

############################################################
# Create Null Table
############################################################

def create_null_table(dataset, specification, output):
    """Create a frequency table of null values for each dataset key

    Args:
        dataset: Path to CSV file
        specification: Path to JSON file
        output: Path to JSON output
    """
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(dataset) as d, open(specification) as s, \
        open(output, 'w') as o:
        dataset = csv.DictReader(d)
        specification = json.load(s)
        header = dataset.fieldnames
        null_table={}

        # skip header
        next(dataset)
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

        json.dump(null_table, o, indent=4)
        log_output_path(output)

############################################################
# Query Dataset
############################################################

def lowercase_list(l):
    """Transform list items to string type and convert to lowercase

    Args:
        l: List of specification values
    """
    return [str(i).lower() for i in l]

def spec_is_empty(specification):
    """Check if specification value is empty

    Args:
        specification: List of specification values
    """
    if len(specification) == 0:
        return True
    return False

def fields_exist_in_row(row, specification):
    """Check if row contains field that matches specifications for each key

    ToDo: How to iterate this without specifying key values?

    Args:
        row: Dataset row
        specification: List of specification values
    """

    # Attempt at iterating without specifying key values
    # for spec in specification:
    #     for s in specification[spec]:
    #         print(row[spec])
    #     if row[spec].lower() in lowercase_list(specification[spec]):
    #         return True

    statuses = lowercase_list(specification['status'])
    neighborhoods = lowercase_list(specification['neighborhood'])
    fiscal_years = lowercase_list(specification['fiscal_year'])
    areas = lowercase_list(specification['area'])
    if (row['status'].lower() in statuses or spec_is_empty(statuses)) \
            and (row['neighborhood'].lower() in neighborhoods \
                or spec_is_empty(statuses)) \
            and (row['fiscal_year'].lower() in fiscal_years \
                or spec_is_empty(fiscal_years)) \
            and (row['area'].lower() in areas
                or spec_is_empty(areas)): \
        return True

def query_dataset(dataset, specification, output):
    """Query dataset based on specified fields

    - A blank value in any specified query for a column/field will disqualify
      that record from inclusion in the results
    - Empty string: do not limit results by this specification at all

    Args:
        dataset: Path to CSV file
        specification: Path to JSON file
        output: Path to JSON output
    """
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(dataset) as d, open(specification) as s, \
        open(output, 'w') as o:
        dataset = csv.DictReader(d)
        specification = json.load(s)

        matched_rows = []
        matched_count = 0

        # skip header
        next(dataset)
        # loop through each row
        for row in dataset:
            # in each row, loop through each specification
            for spec in specification:
                # skip row if any of the specified fields are empty
                if not row[spec]: # use implicit boolean
                    continue
                # count and append to list if field values exist in row
                elif fields_exist_in_row(row, specification):
                    matched_count += 1
                    matched_rows.append(row)
                else: 
                    continue

        log_specifications(specification)
        log_count(matched_count)
        log_output_path(output)
        json.dump(matched_rows,o,indent=4)

if __name__ == '__main__':
    dataset = '../data/pgh_capital_projects.csv'
    specification = './specifications/specifications.json'
    null_table_output = './output/null_table.json'
    query_output = './output/query_output.json'

    log_status('return frequency table of null values for each key')
    create_null_table(dataset, specification, null_table_output)

    log_status('return rows that meets the imported specifications')
    query_dataset(dataset, specification, query_output)

