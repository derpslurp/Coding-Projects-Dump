import turtle
from random import *
from turtle import *

window = turtle.Screen()
window.bgcolor('black')
squares = list(range(32)) * 2
state = {"spot": None}
show = [True] * 64

def tap(x, y):
    spot = int((x + 200) // 50 + ((y + 200) // 50) * 8)
    mark = state["spot"]

    if mark is None or mark == spot or squares[mark] != squares[spot]:
        state["spot"] = spot
    else:
        show[spot] = False
        show[mark] = False
        state["spot"] = None

def draw():
    clear()
    goto(0, 0)
    for count in range(64):
        if show[count]:
            x, y = (count % 8) * 50 - 200, (count // 8) * 50 - 200
            up()
            goto(x, y)
            down()
            color("black", "white")
            begin_fill()
            for i in range(4):
                forward(50)
                left(90)
            end_fill()

    mark = state["spot"]

    if mark is not None and show[mark]:
        x, y = (mark % 8) * 50 - 200, (mark // 8) * 50 - 200
        up()
        goto(x, y)
        color("black")
        write(squares[mark], align='left',font=("Arial", 30, "normal"))

    update()
    ontimer(draw)

shuffle(squares)
hideturtle()
tracer(0)
onscreenclick(tap)
draw()
done()