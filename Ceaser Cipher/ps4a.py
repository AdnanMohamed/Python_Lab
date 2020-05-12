# Problem Set 4A
# Name: Adnan Mohamed
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
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
        return temp

    if(len(sequence) == 1):
        return [sequence]
    else:
        return insert(sequence[0], get_permutations(sequence[1::]))
    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations('abc'))
    print(get_permutations('you'))
    print(get_permutations('must'))
