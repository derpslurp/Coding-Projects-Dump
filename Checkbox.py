from tkinter import *

def display():
    if(x.get()==1):
        print('You agree!')
    else:
        print('You dont agree :(')

window = Tk()

x = IntVar()

photo = PhotoImage(file='Rebirth.png')

check_button = Checkbutton(window,
                           text='I agree to something',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20,'bold'),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')
check_button.pack()

window.mainloop()