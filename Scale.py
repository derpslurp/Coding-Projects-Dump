from tkinter import *

def submit():
    print('The temperature is: '+ str(scale.get())+' degrees C')

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              font=('Consolas',20),
              tickinterval=10,
              resolution=5,
              troughcolor='#69FAFF',
              fg='#FF1C00',
              bg='black')
scale.set((scale['from']-scale['to'])/2+scale['to'])
scale.pack()

button = Button(window,text='sumbit',command=submit)
button.pack()

window.mainloop()