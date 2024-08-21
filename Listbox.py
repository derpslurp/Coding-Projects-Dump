from tkinter import *

def submit():
    print('You have ordered:')
    print(listbox.get(listbox.curselection()))

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia',35),
                  width=12)
listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(1,'hamburger')

listbox.config(height=listbox.size())

submitButton = Button(window,text='submit',command=submit)
submitButton.pack()

window.mainloop()