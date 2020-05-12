# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:11:41 2020

@author: adnan
"""

import turtle

color_list = ['dark goldenrod','dark gray','dark green', 'gold',
'ivory','LemonChiffon3','LightSteelBlue','orange2']

print("Here are some background colors to choose from:-\n")
for i in range(len(color_list)):print(i+1,'- '+color_list[i]) #show colors

user_choice = int(input("Enter choice: "))
while(user_choice < 1 or user_choice > len(color_list)):
        user_choice = int(input("Enter choice from the above: "))

back_color = color_list[user_choice - 1]  # assigning the background color chosen by user

pen_size = int(input("Enter the pen size: "))
while(pen_size < 0 ):
        pen_size = int(input("Enter the pen size (can't be negative!): "))

wn = turtle.Screen()
wn.bgcolor(back_color)      # Set the window background color
wn.title("Hello, World!")      # Set the window title

tess = turtle.Turtle()
tess.color("purple")            # Tell tess to change her color
tess.pensize(pen_size)               # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
