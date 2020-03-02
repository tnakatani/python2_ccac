import glob
import csv
import pandas as pd


def skip_header(reader):
    next(reader)


def get_file_paths(path):
    csv_list = []
    for f in glob.glob(path):
        csv_list.append(f)
    return csv_list


def merge_csv(files):
    master_list = []
    for f in files:
        with open(f) as f:
            reader = csv.reader(f)
            skip_header(reader)
            for row in reader:
                master_list.append(row)
    return master_list


def convert_to_dataframe(merged_list):
    header = ['listings', 'title', 'price', 'currency', 'url']
    df = pd.DataFrame.from_records(merged_list)
    df.columns = header
    df['price'] = df['price'].astype('float64')
    return df


# with open('./top_records.csv', 'w') as f:
if __name__ == '__main__':
    paths = get_file_paths('./output/*_listings.csv')
    merged_csv = merge_csv(paths)
    df = convert_to_dataframe(merged_csv)
    df_sortby_currency = df.sort_values(['currency','price'], 
                                        ascending=False).groupby('currency') \
                                        .head(10)
    df_sortby_currency.to_csv('output/top_records.csv', index=False)
