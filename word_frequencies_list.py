"""
Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method.
The file contains a list of words separated by commas. Your program should output the words and their frequencies
(the number of times each word appears in the file) without any duplicates.
"""

import csv

pointer = {}
# READ file
with open(input(), "r") as file:
    reader = csv.reader(file)
    # READ file row
    for row in reader:
        # READ each item in file row
        for name in row:
            # IF the name is not in pointer
            # THEN ADD name to the pointer dict. Start with 1 as key value for first iteration to begin count
            if name not in pointer:
                pointer[name] = 1
            # ELSE IF increment existing names by one
            elif name in pointer:
                pointer[name] +=1
        # OUTPUT the pointer keys and values
        for name in pointer:
            print(f'{name} {pointer[name]}')
