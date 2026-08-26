import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
turtle_colors = ["green", "red", "yellow", "blue", "orange", "purple"]
y_position = [ -70, -40, -10, 20, 50, 80]
is_race_start = False
user_bet = turtle.textinput("Bet", "Which turtle will win. Enter the color: ")
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(x = -230, y= y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_start = True

while is_race_start:


    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_start = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won!. The {winning_turtle} is winner.")
            else:
                print(f"You've lost!. The {winning_turtle} is winner.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()