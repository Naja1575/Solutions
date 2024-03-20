import turtle
from math import sin, cos, pi

t = turtle.Turtle()
t.speed(0)

n = 5  # number of spirals
d = 10  # distance between 2 spirals
r = 0  # radius
x, y = 0, 0

cur_r = r
for i in range(n):
    for a in range(1, 360, 4):
        r = cur_r + d * a / 360.0
        a *= pi / 180.0
        y = r * sin(a)
        x = r * cos(a)
        turtle.goto(x, y)
    cur_r += d
