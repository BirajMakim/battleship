# import colorgram
# rbg_color = []
# colors = colorgram.extract('image.JPEG', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g , b)
#     rbg_color.append(new_color)
# print(rbg_color)

import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)
screen = turtle_module.Screen()
tim.speed(0)
tim.penup()
tim.hideturtle()
color_list = [(244, 244, 243), (242, 242, 245), (241, 244, 242), (49, 109, 64), (245, 236, 241), (92, 108, 196), (248, 76, 24), (151, 26, 52), (43, 91, 143), (67, 33, 47), (236, 124, 34), (194, 124, 44), (227, 43, 68), (253, 168, 197), (32, 39, 85), (35, 157, 145), (238, 199, 12), (136, 47, 95), (56, 73, 52), (237, 202, 39), (45, 46, 93), (134, 156, 194), (130, 177, 153), (192, 143, 162), (131, 85, 63), (79, 43, 35), (159, 211, 188), (176, 184, 222), (241, 171, 154), (96, 40, 38)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_dot = 100
for dot_count in range(1, numbers_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()


