import turtle

screen = turtle.Screen()

pen = turtle.Turtle()
pen.color("Blue")
pen.width('5')
pen.speed(2)
pen.penup()
x = -200
y = -200
pen.goto(x,y)

for i in range(3):
    pen.pendown()
    pen.forward(300)
    pen.up()
    pen.goto(x,y+100)
    y += 100

pen.pendown()
pen.forward(300)
pen.goto(x,y)

for j in range(3):
    pen.left(90)

for k in range(4):
    pen.pendown()
    pen.forward(300)
    pen.up()
    pen.goto(x+100,y)
    x += 100

