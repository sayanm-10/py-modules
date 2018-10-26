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

    if len(py_files) > 0:        
        print("\nSummary for", dir_path)
        pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])

        for f in py_files:
            try:
                fp = open(f, 'r')
            except PermissionError:
                pt.add_row([f, 'NA', 'NA', 'NA', 'NA'])
            else:
                with fp:
                    line_count = 0
                    char_count = 0
                    function_count = 0
                    class_count = 0
                    
                    for line in fp:
                        line_count += 1
                        char_count += len(line)
                        
                        if line.lstrip().startswith('def '):
                            function_count += 1

                        if line.lstrip().startswith('class '):
                            class_count += 1

            pt.add_row([f, class_count, function_count, line_count, char_count])

        print(pt)
        print("\n* NA denotes that file could not be read due to permission error.")
    else:
        print("No .py files found in", dir_path)
