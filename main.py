import random
import turtle

import colorgram
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.hideturtle()
turtle.colormode(255)

colors = colorgram.extract('hirst.jpeg', 6)

rgb_colors = [(248, 248, 247), (227, 151, 41), (247, 244, 245), (185, 156, 32), (120, 38, 73), (208, 82, 92)]

my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(250)
my_turtle.setheading(0)


def put_dot():
    for step in range(10):
        my_turtle.color(random.choice(rgb_colors))
        my_turtle.dot(10)
        my_turtle.forward(30)


def move_pos():
    my_turtle.setheading(90)
    my_turtle.forward(20)
    my_turtle.setheading(180)
    my_turtle.forward(300)
    my_turtle.setheading(0)


for x in range(4):
    put_dot()
    move_pos()

screen = Screen()
screen.exitonclick()
