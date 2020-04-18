"""Tree Traversal Using os

"""

import os
import argparse
import logging


def parse_argument():
    """Create ArgumentParser class

    """
    parser = argparse.ArgumentParser(
        description='Recursively searches a directory and creates \
        a frequency table of file types'
    )
    parser.add_argument('-d', '--directory',
                        help='directory to search',
                        default='.')
    parser.add_argument('-v', '--verbose',
                        help='prints each parsed filename and its extension',
                        action='store_true'
                        )
    args = parser.parse_args()
    return args


def create_frequency_table(filename_lists, args):
    """Create a frequency table of file types from input.

    Explanation of why os.splitext is preferred over os.path.split('.')[-1]
    https://stackoverflow.com/a/541394
    """
    freq_table = {}
    for filename_list in filename_lists:
        for filename in filename_list:
            file_extension = os.path.splitext(filename)[-1].lower()
            if not file_extension:
                logging.info('%s does not have an extension', filename)
                continue
            if file_extension in freq_table:
                freq_table[file_extension] += 1
            else:
                freq_table[file_extension] = 1
            if args.verbose:
                print(filename, file_extension)
    return freq_table


def get_filenames_from_directory(directory):
    """Traverse a file directory and return list of filenames found within
    the directory.

    """
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        files.append(filenames)
    return files


def main():
    args = parse_argument()
    files = get_filenames_from_directory(args.directory)
    print(create_frequency_table(files, args))


if __name__ == '__main__':
    main()
