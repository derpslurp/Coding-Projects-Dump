from tkinter import *

food = ['pizza','hamburger','hotdog']

def order():
    if(x.get()==0):
        print('You ordered pizza')
    elif(x.get()==1):
        print('You ordered a hamburger')
    elif(x.get()==2):
        print('You ordered a hotdog')
    else:
        print('chupapi')

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impact',50),
                              indicatoron=0,
                              width = 375,
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()