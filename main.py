#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest
import os
from datetime import datetime, timedelta
from directory_analyzer import print_dir_summary


def datetime_calculator():
    ''' A helper to demonstrate the datetime module '''

    start_date_1 = 'Feb 27, 2000'
    start_date_2 = 'Feb 27, 2017'

    start_date_1 = datetime.strptime(start_date_1, '%b %d, %Y')
    end_date_1 = start_date_1 + timedelta(days=3)
    print("The date three days after Feb 27, 2000 is", end_date_1.strftime('%b %d, %Y'), "\n")

    start_date_2 = datetime.strptime(start_date_2, '%b %d, %Y')
    end_date_2 = start_date_2 + timedelta(days=3)
    print("The date three days after Feb 27, 2017 is", end_date_2.strftime('%b %d, %Y'), "\n")

    date_diff_start = datetime.strptime('Jan 1, 2017', '%b %d, %Y')
    date_diff_end = datetime.strptime('Oct 31, 2017', '%b %d, %Y')

    date_diff = date_diff_end - date_diff_start
    print("{} days passed between Jan 1, 2017 and Oct 31, 2017".format(date_diff.days))


def file_reader(path, field_num, sep, header=False):
    ''' a generator function to read text files and return all of the values on a single line on each call to next() '''

    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print("\n\nError while opening {} for reading".format(os.path.basename(path)))
    else:
        with fp:
            # skip the first line if header is true
            if header: 
                next(fp)
            for line_num, line  in enumerate(fp):
                fields = line.strip().split(sep)
                if (len(fields) < field_num):
                    raise ValueError('\n\n {} has {} fields on line {} but expected {}'.format(os.path.basename(path), len(fields), line_num + 1, field_num))
                else:
                    # return fields from 0:field_num as tuple
                    yield tuple(fields[:field_num])


class FileOpsTest(unittest.TestCase):
    ''' Includes all test cases for file operations '''

    def test_file_reader(self):
        ''' test file_reader() '''

        # test ValueError is raised if expected number
        # of fields exceeds the actual fields
        with self.assertRaises(ValueError) as context:
            for fields in file_reader('test_file_reader.txt', 6, '|', False):
                print(fields)
                
            self.assertTrue('Caught error' in str(context.exception))

        # match the first returned tuple
        expected_result = ('John ', ' Doe ', ' 102000 ', ' Age: 36 ', ' NJ')
        self.assertEqual(next(file_reader('test_file_reader.txt', 5, '|', True)), expected_result)


if __name__ == "__main__":
    ''' This is executed when run from the command line '''

    print("\n\n************************* Problem 1 ******************************\n\n")
    datetime_calculator()
    
    print("\n\n************************* Problem 3 ******************************\n\n")
    print_dir_summary(os.getcwd())
    
    print("\n\n************************* Unit Tests ******************************\n\n")
    unittest.main(exit=False, verbosity=2)
