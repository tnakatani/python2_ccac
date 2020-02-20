"""
id,name,task_description,area,budgeted_amount,status,asset_id,asset_type,fiscal_year,start_date,inactive,neighborhood,council_district,ward,tract,public_works_division,pli_division,police_zone,fire_zone,latitude,longitude
"""

import json
import csv

# def reject_empty_field_rows(dataset):


def read_dataset(dataset, criteria):
    with open(dataset,'r') as f:
        reader = csv.DictReader(f)
        print(reader)
        for i, row in enumerate(reader):
            if i <= 5:
                print(row)
        print(criteria)
        blank_table={}
        criterias = ['fiscal_year', 'area']
        """
        if any cell in this row is empty, move to the new row
        """
        #for i, row in enumerate(reader):
            #if i <= 100:
                # for every criteria in criterias:
                    # if row[criteria] = ''
                        # blank_table[criteria] += 1
                        # else:
                        # blank_table[criteria] + 1
                #if row['fiscal_year'] = ''
                #    if 'fiscal_year' in table:
                #        blank_table['fiscal_year'] += 1
                #    else:
                #        blank_table['fiscal_year'] = 1
                #    continue
                #elif: row['start_date'] = ''
                #    if 'fiscal_year' in table:
                #        blank_table['fiscal_year'] += 1
                #    else:
                #        blank_table['fiscal_year'] = 1
                #elif: row['area'] = ''
                #    if 'fiscal_year' in table:
                #        blank_table['fiscal_year'] += 1
                #    else:
                #        blank_table['fiscal_year'] = 1
                #elif: row['asset_type'] = ''
                #    if 'fiscal_year' in table:
                #        blank_table['fiscal_year'] += 1
                #    else:
                #        blank_table['fiscal_year'] = 1
                #elif: row['planning_status'] = ''
                #    if 'fiscal_year' in table:
                #        blank_table['fiscal_year'] += 1
                #    else:
                #        blank_table['fiscal_year'] = 1

   # return table



def read_criteria(criteria):
    with open(criteria) as f:
        reader = json.load(f)
    return reader

if __name__ == '__main__':
    dataset_path = './data/pgh_capital_projects.csv'
    json_path = 'search_criteria.json'
    
    json_criteria = read_criteria(json_path)
    read_dataset(dataset_path, json_criteria)
