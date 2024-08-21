from tkinter import *

food = ['pizza','hamburger','hotdog']

window = Tk()

x = IntVar()

for index in range (len(food)):
    radiobutton = Radiobutton(window,text=food[index],variable=x,value=index)
    radiobutton.pack()
window.mainloop()