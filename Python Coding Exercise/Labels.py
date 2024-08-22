from tkinter import *

window = Tk()

photo = PhotoImage(file='Rebirth.png')

label = Label(window,
              text='Mens',
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()

window.mainloop()