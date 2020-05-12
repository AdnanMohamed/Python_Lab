# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:35:15 2020

@author: adnan
"""

def hypo(adj, opp):
    return (adj**2 + opp**2)**.5

def is_right(a, b, c):
    """
    Precondition: a, b, and c are the lengths of a triangle.
    Postcondition: returns true if the given lengths may form
    a right triangle.
    """
    p = ((a,b),(b,c),(a,c))
    test1 = hypo(*p[0]) == c
    test2 = hypo(*p[1]) == a
    test3 = hypo(*p[2]) == b
    
    return test1 or test2 or test3


print(is_right(.5*40, 0.5*9, 0.5*41))