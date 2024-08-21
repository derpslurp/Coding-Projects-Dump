import turtle
import random

screen = turtle.Screen()
screen.screensize()

ball = turtle.Turtle()
ball.shape('circle')
ball.color('green')

while True:
    ball.goto(random.randint(-200,-200))