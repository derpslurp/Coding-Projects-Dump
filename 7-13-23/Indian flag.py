import turtle

screen = turtle.Screen()

t = turtle.Turtle()
t.speed(10)

t.penup()
t.goto(-400, 250)
t.pendown()
t.pensize(10)

t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(170)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(170)

t.color("green")
t.begin_fill()
t.forward(170)
t.left(90)
t.forward(800)
t.left(90)
t.forward(170)
t.end_fill()
t.penup()

t.goto(70, -6)
t.pendown()
t.color("navy")
t.fillcolor('white')
t.begin_fill()
t.circle(70)
t.end_fill()

t.penup()
t.goto(-60, -15)
t.pendown()
t.color("navy")
for i in range(24):
    t.pensize(3)
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(16)
    t.right(15)
    t.pendown()

t.penup()
t.goto(21, -7)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(70)
    t.goto(0, 0)
    t.left(15)

turtle.done()