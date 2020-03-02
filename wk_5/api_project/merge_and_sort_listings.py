"""Merge Discogs merchant listing output and sort by most valuable record"""

import glob
import csv
import pandas as pd


def skip_header(reader):
    """Skip the header of a CSV file"""
    next(reader)


def get_file_paths(path_pattern):
    """Get all the filepaths in a directory"""
    csv_list = []
    for path in glob.glob(path_pattern):
        csv_list.append(path)
    return csv_list


def get_column_names(file_paths):
    """Get the header of a CSV file

    Args:
        file_paths: list of file paths to extract CSV column names

    Returns:
        csv_header: List of CSV column names
    """
    with open(file_paths[0], 'r') as sample:
        reader = csv.reader(sample)
        header = next(reader)
        return header


def merge_csv(file_paths):
    """Read all CSV files that matches input glob pattern and merge all of the
    CSV rows into a 2D array.

    Args:
        file_paths: Path to CSV files to merge. Accepts glob patterns.

    Returns:
        master_list: 2D array of all CSV rows
    """
    master_list = []
    for path in file_paths:
        with open(path) as csv_file:
            reader = csv.reader(csv_file)
            skip_header(reader)
            for row in reader:
                master_list.append(row)
    return master_list


def convert_to_dataframe(merged_list, header):
    """Convert a 2D array of listings into to a Pandas dataframe

    Args:
       merged_list: 2D array of CSV rows

    Returns:
        df: Pandas dataframe
    """
    df = pd.DataFrame.from_records(merged_list)
    df.columns = header
    df['price'] = df['price'].astype('float64')
    return df


def sort_and_group_dataframe(dataframe, sort_fields, group_fields):
    """Sort and group dataframe by given column names"""
    return dataframe.sort_values(
        sort_fields,
        ascending=False
    ).groupby(group_fields).head(10)


def main():
    """
    1. Glob list of directory paths to desired CSV files.
    2. Copy and merge all rows from CSVs into one.
    3. Convert merged CSVs into a Pandas dataframe
    4. Sort dataframe by currency and price and group top 10 most expensive
       records by currency.
    5. Write sorted and grouped result to output CSV.
    """
    paths = get_file_paths('./output/*_listings.csv')
    merged_csv = merge_csv(paths)
    csv_columns = get_column_names(paths)
    df = convert_to_dataframe(merged_csv, csv_columns)
    df_sorted_by_currency = sort_and_group_dataframe(
        df,
        ['currency', 'price'],
        'currency'
    )
    output_path = 'output/top_listings.csv'
    df_sorted_by_currency.to_csv(output_path, index=False)
    print(
        f'Record listings merged, sorted and compiled into {output_path}\n'
        f'Take a look!'
    )


if __name__ == '__main__':
    main()
