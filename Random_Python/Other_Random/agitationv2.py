"""
    Grey out min max and x
"""

from turtle import *


STEP = -12  # should be divisor of 360
GAP = 45  # in degrees
PEN_SIZE = 4  # emulated pen width
RADIUS = 24


def await_loading(degrees=[0], color=[1.0, 0.0, 0.0]):  # intentionally dangerous default values

    if degrees[0] == 0:
        color.append(color.pop(0))
        loading.color(color)

    loading.tilt(STEP)

    degrees[0] = (degrees[0] + STEP) % 360

    screen.ontimer(await_loading, 10)


loading = Turtle()
loading.speed('fastest')
loading.backward(RADIUS)
loading.right(90)

loading.begin_poly()
loading.circle(RADIUS, 360 - GAP, 60)
loading.left(90)
loading.forward(PEN_SIZE)
loading.right(90)
loading.circle(RADIUS - PEN_SIZE, GAP - 360, 60)
loading.end_poly()

writer = Turtle()
writer.penup()
writer.goto(0, 50)
writer.write("Loading...", align="center", font=("Courier", 24, "normal"))
writer.ht()

screen = Screen()
screen.addshape('loading', loading.get_poly())
screen.title('Loading...[Not Responding]')
screen.bgcolor('grey')

loading.reset()
loading.shape('loading')

await_loading()

screen.exitonclick()
