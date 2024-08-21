import requests
from tkinter import *

def ShowData():
    city = entrybox.get()
    url = base_url + 'appid=' + api_key + '&q=' + city
    response = requests.get(url).json()
    row = 0
    for i in response:
        Label(frame2, text=f'{i}:').grid(row=row, column=0, pady=10, padx=10)
        Label(frame2, text=response.get(i)).grid(row=row, column=1, pady=10)
        row += 1
window = Tk()
window.geometry('700x700')

frame = Frame(window)
frame.pack(fill=BOTH,expand=1)

canvas = Canvas(frame)
canvas.pack(side=LEFT,fill=BOTH,expand=1)

scroll1 = Scrollbar(frame, orient=VERTICAL,command=canvas.yview)
scroll1.pack(side=RIGHT,fill=Y)

scroll2 = Scrollbar(frame, orient=HORIZONTAL,command=canvas.xview)
scroll2.pack(side=BOTTOM,fill=X)

canvas.config(yscrollcommand=scroll1.set)
canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

canvas.config(xscrollcommand=scroll2.set)
canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

frame2 = Frame(canvas)

canvas.create_window((0,0),window=frame2,anchor='nw')

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window,text='SUBMIT',command=ShowData)
submitbutton.pack()



base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = '845e511023bab0cc43659a3db4dd3d91'

window.mainloop()