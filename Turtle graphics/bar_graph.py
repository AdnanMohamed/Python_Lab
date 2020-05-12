# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:23:05 2020

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


def make_turtle(pen_color,fill_color, size, shape = "turtle"):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(pen_color, fill_color)
    t.pensize(size)
    t.shape(shape)
    return t

def draw_bar(turt, h):
    """
        Precondition: turt is an object of type turtle, and h >= 0
        Postcondition: a bar -perhabs for a bar chart- is drawn with height 'h'
        The turtle is facing east at the end of this.
        The graph is filled with colors such that:-
        bar for any value of 200 or more is filled with red,
        values between [100 and 200) are filled with yellow,
        and bars representing values less than 100 are filled with green.
    """
    
    tort.begin_fill()
    tort.left(90)
    tort.forward(point)
    # mark the height
    if h < 0:
        tort.penup()
        tort.forward(-17)
        tort.write("  " + str(h))
        tort.back(-17)
        tort.pendown()
    else: 
        tort.write("  " + str(h))
    tort.right(90)
    tort.forward(30)
    tort.right(90)
    tort.forward(point)
    tort.left(90)
    tort.end_fill()
    
def get_color(h):
    """
    returns a string of the color name
    depending on the height 'h'.
    """
    if h >= 200:
        return "red"
    elif 100 <= h < 200:
        return "yellow"
    else:
        return "green"
    
if(__name__ == "__main__"):   
    wn = make_window("lightgreen", "Graph")

    tort = make_turtle("darkBlue","red", 3, "classic")
    
    data = [48, 117, 200, 240,0, 160,-37, 260, 220]
    
    for point in data:        
        tort.color("darkBlue", get_color(abs(point)))
        draw_bar(tort,point) 
        tort.penup()
        tort.forward(5)
        tort.pendown()

    wn.mainloop()
