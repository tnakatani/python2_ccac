import csv

def read_csv(input_file, column_name):
    table = {}
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            column = row[column_name]
            if column in table:
                table[column] += 1
            else:
                table[column] = 1
    return table

def write_to_csv(table, column_name):
    output_file = column_name + '_count.csv'
    with open(output_file, 'w', newline='') as o:
        fieldnames = [column_name, 'count']
        writer = csv.DictWriter(o, fieldnames=fieldnames)
        writer.writeheader()
        for item in table:
            writer.writerow({column_name: item, 'count':table[item]})

def create_frequency_table(input_file, column_name):
    frequency_table = read_csv(input_file, column_name)
    write_to_csv(frequency_table, column_name)

if __name__ == '__main__':
    path = '../data/pgh_capital_projects.csv'
    column_list = ['area', 'neighborhood','asset_type','fiscal_year','name']
    for item in column_list:
        create_frequency_table(path,item)

