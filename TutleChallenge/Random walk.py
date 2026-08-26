import turtle
from turtle import *
import random
screen = Screen()
tim =turtle.Turtle()
directions = [0, 90, 180, 270]
tim.pensize(5)
turtle.colormode(255)
tim.speed(0)
# colors = [
#     "black", "navy", "maroon", "darkgreen", "darkblue",
#     "darkred", "darkcyan", "darkmagenta", "darkslategray",
#     "darkolivegreen", "sienna", "brown", "chocolate",
#     "firebrick", "indigo", "purple", "teal"
# ]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple



for i in range (300):
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(20)



screen.mainloop()

