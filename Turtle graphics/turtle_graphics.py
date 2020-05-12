# This program asks the user for two points (x, y)
# Then draws two lines using turtle graphics.
# Calculates and print out the angle between the lines.
#
# @ Author: Adnan Hashem Mohamed


import turtle
from math import atan, pi

def point(coordinate):
    list_x_y = list(coordinate.strip('()').split(','))
    tuple_x_y = (float(list_x_y[0]), float(list_x_y[1]))
    return tuple_x_y

def angle(p1, p2):
    '''
    Precondition: p1, p2 are points in the x,y coordinate
    p1, p2 is a tuple of the form (x,y)
    Postcondition: The return value is the angle (in degrees) between
   two lines. Line 1: from (0,0) to p1, and second line is from p1 to p2.
    '''
    m1 = p1[1] / p1[0]
    try:
        m2 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    except(ZeroDivisionError):
        return 90
    
    answer = atan(abs(m2 - m1)/ (1 + m1 * m2)) * (180 / pi)
    return round(answer, 2)

# prompt the user
print('''Hello user! We are going to ask you to enter two points \n
      in the x, y coordinate. Afterwards we'll draw two lines forming 
      an angle and calculate the angle.\n''')
print("The form of the enrty should be: (x,y)\n")

entry = input("Enter the first point (x,y): ")
p1 = point(entry)
entry = input("Enter the second point (x,y): ")
p2 = point(entry)

turtle.goto(p1[0], p1[1])
turtle.goto(p2[0], p2[1])

turtle.write(angle(p1, p2))

turtle.done()
print("The program is done")