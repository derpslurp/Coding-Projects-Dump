from tkinter import *

window = Tk()
window.geometry('300x300')
def ageCalculator():
    y = year.get()
    m = month.get()
    d = day.get()
    y1 = int(y)
    m1 = int(m)
    d1 = int(d)
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y1, m1, d1)
    age = int((today-dob).days / 365.25)
    person_age.config(text='Age: {}'.format(age))

year_label = Label(window, text='Type the year you were born in:')
year_label.pack()
year = Entry(window)
year.pack()
month_label = Label(window, text='Type the month you were born in(number):')
month_label.pack()
month = Entry(window)
month.pack()
day_label = Label(window, text='Type the day you were born in:')
day_label.pack()
day = Entry(window)
day.pack()
button = Button(window, text='Calculate', command=ageCalculator)
button.pack()
person_age = Label(window, text='Age: ')
person_age.pack()


window.mainloop()
