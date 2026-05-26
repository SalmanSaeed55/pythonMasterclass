import turtle
from math import radians, cos

turtle.pendown()


def encircle_square(length:int) -> None:
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    turtle.left(135)


def square(length: int) -> None:
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)

turtle.speed("fastest")

for s in range(72):
    encircle_square(120)
    turtle.left(5)

turtle.done()