from tkinter import *
from tkinter import messagebox

def click():
    while True:
        messagebox.showerror(title='C:\Drivers/network\X57YV\Windows\WIN10/64',
                             message='Error type: Virus\n'
                                     'Detected: PUABundler:Win32/ICBundler/Trojan\n'
                                     'Status: Active\n'
                                     'Date: 2/28/2023 2:41 PM\n'
                                     'Details: This program has potentially unwanted behavior\n'
                                     'Affected items:\n'
                                     '      Files: C:\Drivers/network\X57YV\Windows\WIN10/64')

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()