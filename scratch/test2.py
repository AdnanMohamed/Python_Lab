# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:00:43 2020

@author: adnan
"""

def grade_category(g):
    """
    returns a string specifying the category
    which the grade 'g' falls in.
    """
    if(g >= 75):
        return "First"
    elif(70 <= g < 75):
        return "Upper Second"
    elif(60 <= g < 70):
        return "Second"
    elif(50 <= g < 60):
        return "Third"
    elif(45 <= g < 50):
        return "F1 Supp"
    elif(40 <= g < 45):
        return "F2"
    else:
        return "F3"
    
if(__name__ == "__main__"):

    grades = [83, 75, 74.9, 70, 69.9, 65, 60,
              59.9, 55, 50, 49.9, 45, 44.9,
              40, 39.9, 2, 0]
    
    for grade in grades:
        print(str(grade)+": " + grade_category(grade))