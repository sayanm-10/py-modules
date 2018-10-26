import os
from prettytable import PrettyTable

def print_dir_summary(dir_path):
    ''' given a directory name, searches that directory for Python files and summarises
        - the file name
        - the total number of lines in the file
        - the total number of characters in the file
        - the number of Python functions (lines that begin with 'def ') - you should include class methods in the number of functions
        - the number of Python classes (lines that begin with 'class ') '''

    try:
        py_files = [f for f in os.listdir(path=dir_path) if f.endswith('.py')]
    except FileNotFoundError:
        print("System cannot find the path specified", dir_path)
    else:
        if len(py_files) > 0:        
            print("\nSummary for", dir_path)
            pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])

            for f in py_files:
                try:
                    fp = open(f, 'r')
                except PermissionError:
                    pt.add_row([f, 'NA', 'NA', 'NA', 'NA'])
                else:
                    classes, functions, lines, chars = analyze_file(fp) 
                pt.add_row([f, classes, functions, lines, chars])

            print(pt)
            print("\n* NA denotes that file could not be read due to permission error.")
        else:
            print("No .py files found in", dir_path)

def analyze_file(fp):
    ''' given a filepointer returns a list containing
        number of classes, number of functions, 
        number of lines and number of chars in the file'''

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

        return class_count, function_count, line_count, char_count
