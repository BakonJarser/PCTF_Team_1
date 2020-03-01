#!/usr/bin/env python3

# This class creates fake flags for the backup service.

from os import listdir
from os.path import isfile, join, dirname, abspath
import sys
import random

# Set the number of false flags to create
NUM_COPIES = 50
# Set the valid character set for the filenames
randomChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# Set the character that separates the flag name from the other text.
startSeparator = '_'
endSeparator = '.'

# Uncomment this if you want to input the path of the flag directory
# Otherwise this needs to be run in the same directory as the flag.
# if sys.argv[1] is None:
#     print("Usage: flagCloner <flag directory>")
#     exit(1)

path = dirname(abspath(__file__))
# Uncomment this if you want to input the path of the flag directory
# Otherwise this needs to be run in the same directory as the flag.
# path = sys.argv[1]

files = [file for file in listdir(path) if isfile(join(path, file))]

for filename in files:
    start = filename.find(startSeparator) + 1
    end = filename.find(endSeparator)
    if start < 1 or end < 0 or start > end:
        continue
    part_to_replace = filename[start:end]
    for i in range(0, NUM_COPIES):
        # generate a random replacement string
        tempFilename = ""
        for j in range(len(part_to_replace)):
            tempFilename += random.choice(randomChars)
        newFileName = filename.replace(part_to_replace, tempFilename)
        # write the new file
        open(newFileName, "w+")


