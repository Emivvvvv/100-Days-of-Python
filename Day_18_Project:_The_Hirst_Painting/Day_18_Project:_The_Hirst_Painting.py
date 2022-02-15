import turtle
from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract('image.jpg', 32)


def random_color():
    return colors[random.randint(0, 31)].rgb


turtle.colormode(255)
tosbaa = Turtle()
tosbaa.pu()
tosbaa.setheading(225)
tosbaa.forward(250)
tosbaa.setheading(0)
for n in range(0, 10):
    for i in range(0, 10):
        tosbaa.dot(20, random_color())
        tosbaa.forward(50)
    tosbaa.back(50)
    tosbaa.setheading(90)
    tosbaa.forward(50)
    tosbaa.setheading((n+1)*180)

screen = Screen()
screen.exitonclick()
