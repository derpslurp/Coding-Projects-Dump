from tkinter import *
import random
window=Tk()
window.config(bg='black')
window.geometry("600x400")
m=['a','b','c']
r = ['Red','Blue','Green','Pink',
		'Yellow','Orange','White','Purple','Brown']
score=0
done=0
right=0
e=StringVar()
e1=Entry(window,textvariable=e,font='vardana 25',fg='red',bg='black',insertbackground='red')
st=Label(window,text="Let's start",width=600,height=400,font='vardana 90',fg='green',bg='black')
st.pack()
q=Label(window,font='vardana 50',bg='black')
q.place(x=230,y=50)
uu=Label(window)
sc=Label(window,text='score : 0',font='vardana 30',fg='green',bg='black')
tm=31
t=Label(window)
def re(event):
    m.start(event)
def  sp(score):
    return score

def result():
    b=Label(window,text='score : '+str(sp(score)),fg='green',font='vardana 50',bg='black')
    b.pack()
    bm=Label(window,text='speed : '+str(round(30/(score)))+' sec/word',width=200,fg='green',font='vardana 40',bg='black')
    bm.pack()
    ac = Label(window,text='Accuracy : '+str(round(right/done*100))+'%',width=200,fg='green',font='vardana 40',bg='black')
    ac.pack()
    uu.pack_forget()
    sc.place_forget()
def ti():
    global tm
    if tm>0:
        tm-=1
        t.config(text='time left : '+str(tm),font='vardana 30',bg='black',fg='orange')
        t.place(x=2,y=2)
        window.after(1000,ti)
    else:
        e1.place_forget()
        uu.config(text="time's up",font='vardana 90',bg='black',fg='green',width=600,height=600)
        uu.pack()
        sc.place_forget()
        t.place_forget()
        window.after(2000,result)
class m():
    def start(event):
        try:
            st.pack_forget()
            global tm
            if tm==31:
                ti()
            global l1
            i=random.randint(0,9)
            kk=random.randint(0,9)
            q.config(text=str(r[i]),fg=r[kk])
            e1.place(x=120,y=200)
            sc.place(x=400,y=2)
            def n(event):
                global score
                global done
                global right
                if e.get()==r[i].lower():
                    e1.delete(0,END)
                    score+=1
                    done+=1
                    right+=1
                    sc.config(text='score :'+str(score))
                    sp(score)
                    m.start(event)
                else:
                    done+=1
                    e1.delete(0,END)
                    m.start(event)
            window.bind("<Return>",n)
        except:
            pass
    window.bind("<Return>",start)

window.mainloop()