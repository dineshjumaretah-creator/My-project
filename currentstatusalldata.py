import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from currentstatussave import *
from currentstatusdelete import *
from currentstatusupdate import *
from currentstatusfind import *
from currnetstatusnavigate import *
from currnetstatusshow import *
def currentstatusalldata():
    t=tkinter.Tk()
    t.config(bg='#35344e')
    t.geometry('1000x1000')
    t.title('City dashboard')
    l1=Label(t,text='City Dashboard',font=('arial', 30), bg='#f2ede7')
    l1.place(x=500,y=30)
    b1=Button(t, text='Currentstatus insert',command=showcurinsert,width=20,height=1,font=('arial', 12, 'bold'), bg='red')
    b1.place(x=520,y=100)
    b2=Button(t, text='Currentstatus delete',command=showcurdelete,width=20,height=1,font=('arial', 12, 'bold'), bg='orange')
    b2.place(x=520,y=140)
    b3=Button(t, text='Currentstatus update',command=showcurupdate,width=20,height=1,font=('arial', 12, 'bold'), bg='green')
    b3.place(x=520,y=180)
    b4=Button(t, text='Currentstatus find',command=showcurfind,width=20,height=1,font=('arial', 12, 'bold'), bg='yellow')
    b4.place(x=520,y=220)
    b5=Button(t, text='Currentstatus navigate',command=showcurnavigate,width=20,height=1,font=('arial', 12, 'bold'), bg='blue')
    b5.place(x=520,y=260)
    b6=Button(t, text='Currentstatus show',command=showcurshow,width=20,height=1,font=('arial', 12, 'bold'), bg='purple')
    b6.place(x=520,y=300)
    t.mainloop()