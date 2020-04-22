"""Tree Traversal Using os

"""

import os
from pathlib import Path
import pathlib
import argparse
import logging
import matplotlib.pyplot as plt


def parse_argument():
    """Create ArgumentParser class

    """
    parser = argparse.ArgumentParser(
        description='Recursively searches a directory and creates \
        a frequency table of file types'
    )
    parser.add_argument('-d', '--directory',
                        help='directory to search',
                        default='smokedfoods')
    parser.add_argument('-v', '--verbose',
                        help='prints each parsed filename and its extension',
                        default=False
                        )
    args = parser.parse_args()
    return args


def get_filenames_from_directory(directory):
    """Traverse a file directory and return list of filenames found within
    the directory.

    """
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        files.append(filenames)
    return files


def create_frequency_table(filename_lists, verbose):
    """Create a frequency table of file types from input.

    Explanation of why os.splitext is preferred over os.path.split('.')[-1]:
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
            if verbose:
                print(filename, file_extension)
    return freq_table


def sort_frequency_table(freq_table):
    """Sort a frequency table by its values

    Ref: https://docs.python.org/3/howto/sorting.html
    """
    sort_result = sorted(freq_table.items(),
                         key=lambda filetypes: filetypes[1],
                         reverse=True)
    return {key: value for key, value in sort_result}


def plot_frequency_table(freq_table, directory):
    """Plot frequency table into a bar chart using matplotlib

    Ref: https://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html
    """
    fig, ax = plt.subplots()
    counts = freq_table.values()
    y_pos = range(len(freq_table.keys()))
    ax.barh(y_pos, counts, align='center')
    ax.tick_params(axis='y', which='major', pad=15)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(freq_table.keys())
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Counts')
    if directory:
        ax.set_title(f'Most common filetypes in\n{directory} directory')
    else:
        ax.set_title(f'Most common filetypes')
    # After plt.show() is called, the figure is erased.
    # Save image prior to showing the plot.
    save_plot_to_png(plt, directory)
    plt.show()


def save_plot_to_png(plt, directory):
    """Save frequency table plot to a PNG file"""
    os.makedirs('./img', exist_ok=True)
    plt.savefig(f'./img/filetype_freq_table_{directory}.png')


def main():
    args = parse_argument()
    files = get_filenames_from_directory(args.directory)
    freq_table = create_frequency_table(files, verbose=args.verbose)
    sorted_table = sort_frequency_table(freq_table)
    plot_frequency_table(sorted_table, directory=args.directory)


if __name__ == '__main__':
    main()
