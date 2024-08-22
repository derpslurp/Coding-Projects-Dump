from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,3,1,'white')
tennis_ball = Ball(canvas,0,0,50,3,4,'green')
basket_ball = Ball(canvas,0,0,125,8,7,'orange')
base_ball = Ball(canvas,0,0,40,10,6,'black')
base_ball1 = Ball(canvas,0,0,200,6,10,'blue')

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    base_ball.move()
    base_ball1.move()
    window.update()
    time.sleep(0.01)

window.mainloop()