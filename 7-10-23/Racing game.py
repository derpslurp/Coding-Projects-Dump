from turtle import *
import random

speed(0)
penup()
goto(-140, 140)

for i in range(11):
    write(i, align='center')
    right(90)

    for num in range(4):
        pendown()
        forward(40)

    penup()
    backward(160)
    left(90)
    forward(20)

player_1 = Turtle()
player_1.shape('turtle')
player_1.color('red')

player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()


player_2 = Turtle()
player_2.shape('turtle')
player_2.color('orange')

player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

player_3 = Turtle()
player_3.shape('turtle')
player_3.color('yellow')

player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

player_4 = Turtle()
player_4.shape('turtle')
player_4.color('green')

player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()

for turn in range(68):
    player_1.forward(random.randint(1, 5))
    player_2.forward(random.randint(1, 5))
    player_3.forward(random.randint(1, 5))
    player_4.forward(random.randint(1, 5))

x1 = player_1.xcor()
x2 = player_2.xcor()
x3 = player_3.xcor()
x4 = player_4.xcor()

if x1 > x2 and x3 and x4:
    write('Red wins!')
    while True:
        player_1.forward(90)
        player_1.left(144)
elif x2 > x1 and x3 and x4:
    write('Orange wins!')
    while True:
        player_2.forward(90)
        player_2.left(144)
elif x3 > x1 and x2 and x4:
    write('Yellow wins!')
    while True:
        player_3.forward(90)
        player_3.left(144)
elif x4 > x1 and x2 and x3:
    write('Green wins!')
    while True:
        player_4.forward(90)
        player_4.left(144)