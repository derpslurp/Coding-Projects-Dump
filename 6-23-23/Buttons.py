from tkinter import *

count = 0
def click():
    global count
    count+=1
    print(count)
window = Tk()
button = Button(window,
                text='click me!',
                command=click)
button.pack()

window.mainloop()