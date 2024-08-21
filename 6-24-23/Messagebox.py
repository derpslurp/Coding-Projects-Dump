from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showwarning(title='WARNING',message='YOU HAVE A VIRUS')

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()