def submit():
    print('You have ordered: ')
    print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(),entryBox.get())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia',35),
                  width=12)
listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(2,'cheese bread')
listbox.insert(3,'soup')
listbox.insert(4,'salad')

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text='submit',command=submit)
submitButton.pack()

addButton = Button(window,text='add',command=add)
addButton.pack()

window.mainloop()