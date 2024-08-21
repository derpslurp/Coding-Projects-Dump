import turtle

pen = turtle.Turtle()
pen.speed(10)
pen.hideturtle()
pen.penup()
window = turtle.Screen()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'indigo', 'violet','white']
arc = 200
x = 0
y = -180
pen.goto(x, y)

cut = turtle.Turtle()
cut.shape('square')
cut.color('white')
cut.shapesize(20)
cut.goto(0,-180)
for i in colors:
    pen.color(i)
    pen.fillcolor(i)
    pen.begin_fill()
    pen.circle(arc)
    pen.end_fill()
    pen.goto(x,y+20)
    cut.goto(0, -180)
    y += 20
    arc -= 20
turtle.done()