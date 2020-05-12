import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("The STAR!")

tort = turtle.Turtle()
tort.penup()
tort.left(36)
tort.forward(100)
tort.pendown()
tort.pensize(2)

for c in ["red", "blue", "yellow", "green", "purple"]:
    tort.color(c)
    tort.left(180-36)
    tort.forward(100)
tort.hideturtle()
