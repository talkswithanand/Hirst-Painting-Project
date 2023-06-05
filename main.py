# TURTLE DOC : https://docs.python.org/3/library/turtle.html#overview-of-available-turtle-and-screen-methods

# import colorgram

# colors = colorgram.extract("image.jpg", 25)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
t = Turtle()
t.hideturtle()


color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181)]

t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)

for _ in range(10):
    for _ in range(10):
        t.pendown()
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)

    t.goto(t.xcor() - 500, t.ycor() + 50)

t.speed("fastest")

screen = Screen()
screen.exitonclick()