#!/usr/bin/env python3

# This class will remove all files in the directory except for submit_flags.py and this file
# It is used to clear the directory before adding new flag files so that flags are not resubmitted.

import os
from os import listdir
from os.path import isfile, join, dirname, abspath

path = dirname(abspath(__file__))
files = [file for file in listdir(path) if isfile(join(path, file))]

for filename in files:
    if filename == 'submit_flags.py' or filename == 'clear_old_flags.py':
        continue
    os.remove(filename)
