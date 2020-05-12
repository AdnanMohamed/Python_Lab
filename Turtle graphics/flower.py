# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:44:19 2020

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

def draw_flower(turtle, size):
    '''
        Draws a flower-like shape of size 'size'
    '''
    for i in range(20):
        draw_square(tort, size)
        tort.left(360//20)

if(__name__ == "__main__"):   
    wn = make_window("lightgreen", "Flower")

    tort = make_turtle("darkBlue", 3, "classic")

    size = 60 # the flower size
    
    draw_flower(tort, size)

    wn.mainloop()
