import time
from tkinter import *

window = Tk()
window.geometry('300x300')


def gettime():
    entry2 = int(entry.get())
    countdown(entry2)


def countdown(user_time):
    while user_time >= 0:
        mins, secs = divmod(user_time, 60)
        timer = str('{:02d}:{:02d}'.format(mins, secs))
        print(timer)
        time.sleep(1)
        user_time -= 1


label = Label(text='Enter a time in seconds')
entry = Entry()
submit = Button(text='Submit', command=gettime)


label.pack()
entry.pack()
submit.pack()
window.mainloop()
