from tkinter import *
from Ball import *
import time

window = Tk()

W = 500
H = 500

canvas = Canvas(window,width=W,height=H)
canvas.pack()

ball1 = Ball(canvas,0,0,100,2,4,'white')
ball2 = Ball(canvas,0,0,200,2,5,'red')
ball3 = Ball(canvas,0,0,150,4,2,'orange')

while True:
    ball1.move()
    ball2.move()
    ball3.move()
    window.update()
    time.sleep(0.01)

window.mainloop()