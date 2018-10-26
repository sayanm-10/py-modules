#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest
from datetime import datetime, timedelta

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


if __name__ == "__main__":
    ''' This is executed when run from the command line '''

    datetime_calculator()
    unittest.main(exit=False, verbosity=2)