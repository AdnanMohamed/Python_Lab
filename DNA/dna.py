# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:12:26 2020

@author: adnan
"""
# The program reads files in command line about people and their
# unique DNA sequences. Then the program identifies to whom a sequence of DNA belongs.

import sys

def longest_chain(string1, string2):
    ''' string1, a string to be searched in string2
        string2, a string
        The function returns the maximum number of
        consecutive occurrences of string1 in string2
    '''
    import re
    occurences = [m.start() for m in re.finditer(string1, string2)]
    if string1 in string2:

        count = 1
        max_num = 0

        for i in range(1,len(occurences)):
            if occurences[i] - occurences[i-1] == len(string1):
                count += 1
            else:
                if max_num < count:
                    max_num = count
                count = 1
        if max_num < count:
            max_num = count
        return max_num
    else:
        return 0

args = sys.argv

if (len(args) != 3):                                        # Making sure that
    print("Usage: python dna.py data.csv sequence.txt")     # the user enters
    exit(1)                                                 # the proper form

csv_file = args[1]
sequence_file = args[2]

with open(csv_file, 'r') as fin:
    try:
        fin.seek(5)
        first_line = fin.readline() # now first_line contains columns' names AGATC,TTAGA,....
    except:
        print("Things went wrong")

first_line = first_line.strip('\n')
STR_components = list(first_line.split(','))

with open(sequence_file, 'r') as fin:
    try:
        DNA_string = fin.read() # now DNA_string contains the sequence of AGATCTTAGA....
    except:
        print("Things went wrong")

target_dict = {}

for component in STR_components:
    target_dict[component] = longest_chain(component, DNA_string) # now target_dict keys are the DNA components such as: AGATC
                                                                  #and the values are the longest consecutive number of occurence

people_dna_dict = {}

with open(csv_file, 'r') as fin:                    # This block creates a dictionary.
    try:                                            # The keys are names of people in the
        #ignore first line                          # file and the values are lists of the
        fin.readline()                              # dna unique number of longest concurrent
        for line in fin:                            # of a component of the dna.
            line = line.strip('\n')
            line = line.split(',')
            people_dna_dict[line[0]] = line[1::]
    except:
        print("Things went wrong")

for person in people_dna_dict:
    if(list(map(int, people_dna_dict[person])) == list(target_dict.values())):
        print(person)
        break
else:
    print("No match")
