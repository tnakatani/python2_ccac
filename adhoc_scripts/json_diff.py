import difflib
import os
import argparse
from pathlib import Path
d = difflib.Differ()

def compare_json(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        result = d.compare(f1.readlines(), f2.readlines())
        output = (''.join(result))
        return output

def write_to_file(result, name):
    file_name = name + '.json'
    path = Path('diff')
    os.makedirs('diff', exist_ok=True)
    with open('./diff/{}'.format(file_name),'w') as f:
        f.write(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Diff two JSON files using difflib library.  Outputs text file indicating additions and deletions from file1 to file2.  difflib ref: https://docs.python.org/3/library/difflib.html#difflib.Differ')
    parser.add_argument('file1', help='1st comparison file')
    parser.add_argument('file2', help='2nd comparison file')
    parser.add_argument('output_file_name', help='Name of output JSON file')
    args = parser.parse_args()

    diff_result = compare_json(args.file1, args.file2)
    write_to_file(diff_result, args.output_file_name)
