# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:33:53 2020

@author: adnan
"""

import turtle

def make_window(color, title):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w


def make_turtle(color, size, shape = "turtle"):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.shape(shape)
    return t

def draw_square(turtle, size):
    '''
        Draws a square of size 'size'.
    '''
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def new_spot(turtle, steps):
    '''
        Moves the turtle 'steps' east, then
        'steps' north <without drawing>
    '''
    tort.penup()

    tort.forward(square_size+space)
    tort.left(90)
    tort.forward(square_size+space)
    tort.pendown()

if(__name__ == "__main__"):   
    wn = make_window("lightgreen", "squares")

    tort = make_turtle("darkBlue", 3, "classic")

    space = 15       # space between squares
    square_size = 30 # length of the square sides
    
    for i in range(5):
        draw_square(tort, square_size)
        # move to the next spot
        new_spot(tort, square_size+space)
        square_size+=2*space        
        tort.left(90)

    wn.mainloop()