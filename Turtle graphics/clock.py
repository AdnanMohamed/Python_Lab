# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:24:47 2020

@author: adnan
"""

import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Clock")



tess = turtle.Turtle()       # Create tess and set some attributes
tess.penup()
tess.shape("turtle")
tess.color("blue")
tess.pensize(4)
tess.left(60)
for i in range(12):
    tess.forward(90)
    tess.pendown()
    tess.forward(10)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.forward(25)
    tess.write(i+1)
    tess.backward(145)
    tess.right(30)

wn.mainloop()