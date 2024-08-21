from tkinter import *

def submit():
    username = entry.get()
    print('hello '+username)

window = Tk()
entry = Entry(window,
              font=('Arial',50))
entry.pack(side=LEFT)

submit_button = Button(window,text='submit',command=submit)
submit_button.pack(side=RIGHT)

entry.pack()

window.mainloop()