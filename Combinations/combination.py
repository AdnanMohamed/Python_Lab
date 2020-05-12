
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:00:43 2020

@author: Adnan H. Mohamed
"""

def C(n,r):
    '''
    Precondition: 1 ≤ r ≤ n where n, r are positive integers
    Postcondition: returns the number of ways to choose r elements
    from a set of n elements (order does not matter).
    '''
    if(n == r or r == 0):
        return 1
    elif(r == 1):
        return n
    else:
        return C(n-1,r-1) + C(n-1,r)
    
if(__name__ == "__main__"):
    count = 0
    
    for r in range(0, 8):
        print(f"C(7, {r}) =", C(7, r))
    

        
