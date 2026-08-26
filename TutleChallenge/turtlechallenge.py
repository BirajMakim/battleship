import turtle as t
from turtle import Screen
import random
tim = t.Turtle()



# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)


# for i in range(5):
#
#     tim.right(72)
#     tim.forward(100)
colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "brown", "black", "gray", "cyan", "magenta",
    "turquoise", "gold", "silver", "navy", "maroon", "olive",
    "lime", "teal", "fuchsia", "gainsboro", "light gray",
    "dark gray", "lavender", "beige", "chocolate",
    "coral", "crimson", "indigo", "khaki", "plum", "salmon",
    "sienna", "tan", "violet",
]

def draw_shape(num_side):
    angle = 360/num_side
    for i in range (num_side):
        tim.forward(100)
        tim.right(angle)
for shape_in_side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_in_side)




screen = Screen()
screen.mainloop()
