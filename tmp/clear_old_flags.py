#!/usr/bin/env

from os import listdir
from os.path import isfile, join, dirname, abspath

path = dirname(abspath(__file__))
files = [file for file in listdir(path) if isfile(join(path, file))]

for filename in files:
    if filename == 'submit_flags.py' or filename = clear_old_flags.py
        continue
    os.exec('rm -f %s' % filename)
