# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:03:38 2020

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

wn = make_window("lightgreen", "squares")

tort = make_turtle("darkBlue", 3)

for i in range(5):
    draw_square(tort, 40)
    tort.penup()
    tort.forward(80)
    tort.pendown()
    

wn.mainloop()
