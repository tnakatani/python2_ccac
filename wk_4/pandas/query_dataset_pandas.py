import pandas as pd
import json
import csv


# Create Frequency Table of Null Values
def create_null_table(df, output):
    null_table = df.isnull().sum()
    null_table.to_json(output)

# Query Dataset Based on Specified Fields
def lowercase_list(l):
    """Transform list items to string type and convert to lowercase

    Args:
        l: List of specification values
    """
    return [str(i).lower() for i in l]

def compare_lists(spec, l):
    """Return a boolean series based on whether each dataframe contains specified value

    Args:
        spec: Specification column name (String)
        l: List of specification values
    """
    return df[spec].str.lower().isin(lowercase_list(l))

def main(dataframe, specification, query_output):
    with open(specs) as s:
        specification = json.load(s)
        status = specification['status']
        neighborhood = specification['neighborhood']
        fiscal_year = specification['fiscal_year']
        area = lowercase_list(specification['area'])

        # Set up step: Convert fiscal_year to string so we can use compare_lists()
        # on that column
        df['fiscal_year'] = df['fiscal_year'].astype(str)

        result = df.loc[compare_lists('status', status) \
              & compare_lists('neighborhood', neighborhood) \
              & compare_lists('fiscal_year', fiscal_year) \
              & compare_lists('area', area)][['id','status','neighborhood','fiscal_year','area']]

        result.to_json()

if __name__ == '__main__':
    df = pd.read_csv('../data/pgh_capital_projects.csv')
    specs = './specifications/specifications.json'
    null_table_output = './output/null_table_notebook.json'
    query_output = './output/query_output_notebook.json'

    print('Creating null table...')
    create_null_table(df, null_table_output)
    print(f'Null table done. File located at {null_table_output}\n')

    print('Starting query...')
    main(df, specs, query_output)
    print(f'Query done. File located at {query_output}')
