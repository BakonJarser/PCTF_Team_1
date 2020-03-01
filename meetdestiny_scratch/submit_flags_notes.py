#!/usr/bin/env python3

# Create files with the flag hash as the file name in the same directory as
# this script and they will be submitted when the script is run.

from os import listdir
from os.path import isfile, join, dirname, abspath
import swpag_client as sc

url='http://34.195.187.175'
token= '66978175b387ba7b6dee386d16b40b29'
t = sc.Team(url, token); 
print(t.submit_flag(['what????']))
