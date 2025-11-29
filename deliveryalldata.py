import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from deliverydatasave import *
from deliverydatadelete import *
from deliverydataupdate import *
from deliverydatafind import *
from deliverydatanavigate import *
from deliverydatashow import *
def deliveryalldata():
    t = tkinter.Tk()
    t.config(bg='#35344e')
    t.geometry('1000x1000')
    t.title('Delivery dashboard')
    l1 = Label(t, text='Delivery Dashboard', font=('arial', 20), bg='#f2ede7')
    l1.place(x=500, y=30)
    b1 = Button(t, text='Delivery insert', command=showdelinsert, width=20, height=1,font=('arial', 12, 'bold'), bg='red')
    b1.place(x=520, y=80)
    b2 = Button(t, text='Delivery delete', command=showdeldelete, width=20, height=1,font=('arial', 12, 'bold'), bg='orange')
    b2.place(x=520, y=120)
    b3 = Button(t, text='Delivery update', command=showdelupdate, width=20, height=1,font=('arial', 12, 'bold'), bg='green')
    b3.place(x=520, y=160)
    b4 = Button(t, text='Delivery find', command=showdelfind, width=20, height=1,font=('arial', 12, 'bold'), bg='yellow')
    b4.place(x=520, y=200)
    b5 = Button(t, text='Delivery navigate', command=showdelnavigate, width=20, height=1,font=('arial', 12, 'bold'), bg='blue')
    b5.place(x=520, y=240)
    b6 = Button(t, text='Delivery show', command=showdelshow, width=20, height=1,font=('arial', 12, 'bold'), bg='purple')
    b6.place(x=520, y=280)
    t.mainloop()