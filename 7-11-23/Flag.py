import turtle

circle1 = turtle.Turtle()
circle2 = turtle.Turtle()
circle3 = turtle.Turtle()
circle4 = turtle.Turtle()
circle5 = turtle.Turtle()

circle1.pensize(3)
circle2.pensize(3)
circle3.pensize(3)
circle4.pensize(3)
circle5.pensize(3)

circle1.color("blue")
circle2.color("black")
circle3.color("red")
circle4.color("yellow")
circle5.color("green")

circle1.penup()
circle2.penup()
circle3.penup()
circle4.penup()
circle5.penup()

circle1.goto(-110, -25)
circle2.goto(0, -25)
circle3.goto(110, -25)
circle4.goto(-55, -75)
circle5.goto(55, -75)

circle1.pendown()
circle2.pendown()
circle3.pendown()
circle4.pendown()
circle5.pendown()

circle1.circle(45)
circle2.circle(45)
circle3.circle(45)
circle4.circle(45)
circle5.circle(45)

