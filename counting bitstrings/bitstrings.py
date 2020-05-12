# -*- coding: utf-8 -*-
"""

@author: Adnan Hashem Mohamed

This program answers the following question:
How many bit strings of length eight contain either three consecutive 0s or four consecutive 1s?
"""


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Returns: a list of all permutations of sequence (excluding repeated permuations)

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    >>> get_permutations("111")
    ['111']
    '''
    def insert(letter, lst):
        ''' letter, single charachter
            lst, is a list of at least one letter
            Return: list of the letter inserted in all ways 
            in the lst elements.
            So insert('a', ['c']) returns ['ac', 'ca']
        '''
        temp = []
        for i in lst:
            for j in range(len(i)):
                temp.append(i[:j] + letter + i[j::])
            temp.append(i + letter)
        return list(set(temp))

    if(len(sequence) == 1):
        return [sequence]
    else:
        return insert(sequence[0], get_permutations(sequence[1::]))
    
def count_permutations(possible_permutations):
    '''
    Precondition: possible_permutations is a list of all possible permutations
    of the 8 bits long bitstring
    Postcondition: The returned value is the number of bit strings of 
    length eight contain either three consecutive 0s or four consecutive 1s
    '''
    count = 0
    for bit_string in possible_permutations:
        if("000" in bit_string or "1111" in bit_string):
            count += 1
    return count

if(__name__ == "__main__"):
    
    permutations = []
    # get all 256 possible permutations for the 8 long bit string
    for zeros in range(9):
        permutations += get_permutations("0"*zeros+"1"*(8-zeros))
    
    answer = count_permutations(permutations)
    print(f'''There are {answer} bit strings such that it consists from either
three consecutive zeros or 4 consecutive 1s.''')
