import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from staffdatasave import *
from staffdatadelete import *
from staffdataupdate import *
from staffdatafind import *
from staffdatanavigate import *
from staffdatashow import *
def staffalldata():
    t = tkinter.Tk()
    t.config(bg='#35344e')
    t.geometry('1000x1000')
    t.title('Staff dashboard')
    l1 = Label(t, text='Staff Dashboard', font=('arial', 20,'bold'), bg='#f2ede7')
    l1.place(x=500, y=30)
    b1 = Button(t, text='Staff insert', command=showstinsert, width=20, height=1,font=('arial', 12, 'bold'), bg='red')
    b1.place(x=505, y=80)
    b2 = Button(t, text='Staff delete', command=showstdelete, width=20, height=1,font=('arial', 12, 'bold'), bg='orange')
    b2.place(x=505, y=120)
    b3 = Button(t, text='Staff update', command=showstupdate, width=20, height=1,font=('arial', 12, 'bold'), bg='yellow')
    b3.place(x=505, y=160)
    b4 = Button(t, text='Staff find', command=showstfind, width=20, height=1,font=('arial', 12, 'bold'), bg='green')
    b4.place(x=505, y=200)
    b5 = Button(t, text='Staff navigate', command=showstnavigate, width=20, height=1,font=('arial', 12, 'bold'), bg='blue')
    b5.place(x=505, y=240)
    b6 = Button(t, text='Staff show', command=showstshow, width=20, height=1,font=('arial', 12, 'bold'), bg='purple')
    b6.place(x=505, y=280)
    t.mainloop()