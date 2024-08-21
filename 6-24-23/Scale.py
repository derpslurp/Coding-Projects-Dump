from tkinter import *

def submit():
    print('The temperature is: '+str(scale.get())+' degrees C')

window = Tk()

scale = Scale(window,from_=100,to=0)
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()