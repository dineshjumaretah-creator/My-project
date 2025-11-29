import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cofficesave import *
from cofficedelete import *
from cofficeupdate import *
from cofficefind import *
from cofficenavigate import *
from cofficeshow import *
def cofficealldata():
    t = tkinter.Tk()
    t.config(bg='#35344e')
    t.geometry('1000x1000')
    t.title('Coffice dashboard')
    l1 = Label(t, text='Cofficealldata dashboard', font=('arial', 20,'bold'), bg='#f2ede7')
    l1.place(x=500, y=30)
    b1 = Button(t, text='Coffice insert', command=showcoffinsert, width=30, height=1,font=('arial', 12, 'bold'), bg='red')
    b1.place(x=515, y=80)
    b2 = Button(t, text='Coffice delete', command=showcoffdelete, width=30, height=1,font=('arial', 12, 'bold'), bg='orange')
    b2.place(x=515, y=120)
    b3 = Button(t, text='Coffice update', command=showcoffupdate, width=30, height=1,font=('arial', 12, 'bold'), bg='green')
    b3.place(x=515, y=160)
    b4 = Button(t, text='Coffice find', command=showcofffind, width=30, height=1,font=('arial', 12, 'bold'), bg='yellow')
    b4.place(x=515, y=200)
    b5 = Button(t, text='Coffice navigate', command=showcoffnavigate, width=30, height=1,font=('arial', 12, 'bold'), bg='blue')
    b5.place(x=515, y=240)
    b6 = Button(t, text='Coffice show', command=showcoffshow, width=30, height=1,font=('arial', 12, 'bold'), bg='purple')
    b6.place(x=515, y=280)
    t.mainloop()