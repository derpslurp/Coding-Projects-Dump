import json
from difflib import get_close_matches
from tkinter import *
from PIL import ImageTk, Image
import time

window = Tk()
window.geometry('400x500')

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data,file,indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question,questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base:dict) -> str | None:
    for q in knowledge_base['questions']:
        if q['question'] == question:
            return q['answer']
row = 0
row2 = 1
bot = Label(window, text='Bot: Thank you, I learned a new response!')
def pp():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    new_answer = newentry.get()
    user_input = entrybox.get()
    if new_answer.lower() != 'skip':
        knowledge_base['questions'].append({'question': user_input, 'answer': new_answer})
        save_knowledge_base('knowledge_base.json', knowledge_base)
        bot2 = Label(window, text='Bot: Thank you, I learned a new response!')
        bot2.pack()
    newentry.pack_forget()
    newsubmit.pack_forget()
def chat_bot():
    global row, row2, bot, typing
    typing.pack_forget()
    bot.pack_forget()
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    user_input = str(entrybox.get())
    Label(frame2,text=f'You: {user_input}').grid(row=row,column=0)

    best_match: str | None = find_best_match(user_input, [q['question'] for q in knowledge_base['questions']])

    if best_match:
        answer: str = get_answer_for_question(best_match,knowledge_base)
        for i in range(3):
            typing.pack()
            time.sleep(0.4)
            window.update()
            typing.config(text='Bot typing.')
            time.sleep(0.4)
            window.update()
            typing.config(text='Bot typing..')
            typing.pack()
            time.sleep(0.4)
            window.update()
            typing.config(text='Bot typing...')
            typing.pack()
            window.update()
            time.sleep(0.4)
        Label(frame2,text=f'Bot: {answer}').grid(row=row2,column=0)
        typing.pack_forget()
    else:
        bot = Label(window, text='Bot: I don\'t know the answer. Can you teach me?')
        bot.pack()
        newanswer = newentry
        newanswer.pack()
        newbutton = newsubmit
        newbutton.pack()
    row += 2
    row2 += 2

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

frame3 = Frame(window)
frame3.pack(fill=BOTH)

frame4 = Frame(window)
frame4.pack(fill=BOTH)

newentry = Entry(window)
newsubmit = Button(window,text='SUBMIT',command=pp)

image_submit = Image.open('send.png')

resized1 = image_submit.resize((60,50))

image_submit = ImageTk.PhotoImage(resized1)

entrybox = Entry(frame4)
entrybox.grid(row=0,column=0)

submitbutton = Button(frame4,text='SUBMIT',image=image_submit,height=25,width=55,command=chat_bot).grid(row=0,column=1)

typing = Label(frame3, text='Bot typing')

window.mainloop()