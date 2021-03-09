import turtle as t
from random import choice

screen = t.Screen()
hirst = t.Turtle()
t.colormode(255)

rgb_colors = [(37, 107, 142), (220, 156, 93), (11, 53, 89), (203, 133, 158), (134, 174, 196), (141, 80, 38),
              (37, 129, 79), (26, 166, 198), (228, 210, 103), (200, 159, 27), (132, 30, 47), (204, 94, 124),
              (144, 181, 163), (13, 98, 61), (15, 48, 42), (14, 67, 125)]

hirst.penup()
hirst.hideturtle()
hirst.speed("fastest")
hirst.setpos(-200.0, -200.0)

for _ in range(10):
    for _ in range(10):
        hirst.dot(20, choice(rgb_colors))
        hirst.forward(50)
    hirst.sety(hirst.ycor() + 50)
    hirst.setx(-200.0)

screen.exitonclick()
