import turtle
from turtle import *
import random
screen = Screen()
tim =turtle.Turtle()

turtle.colormode(255)
tim.speed(0)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(80, )
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)


screen.mainloop()