from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='Rebirth.png')

button = Button(window,
                text='click me!',
                command=click,
                font=('Arial',30),
                fg="#00FF00",
                bg='black',
                activeforeground='#00FF00',
                activebackground='black',
                image=photo,
                compound="left")
button.pack()

window.mainloop()