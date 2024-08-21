import turtle
import random

turtle.clone()
for i in range(10):
    p = turtle.clone()
    p.goto(random.randint(-100,100),random.randint(-100,100))

turtle.done()