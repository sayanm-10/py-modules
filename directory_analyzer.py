import os
from prettytable import PrettyTable

def print_dir_summary(dir_path):
    ''' given a directory name, searches that directory for Python files and summarises
        - the file name
        - the total number of lines in the file
        - the total number of characters in the file
        - the number of Python functions (lines that begin with 'def ') - you should include class methods in the number of functions
        - the number of Python classes (lines that begin with 'class ') '''

    py_files = [f for f in os.listdir(path=dir_path) if f.endswith('.py')]

    print("Summary for", dir_path)
    pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])

    for f in py_files:
        pt.add_row([f, 0, 0, 0, 0])

    print(pt)

print_dir_summary(os.getcwd())