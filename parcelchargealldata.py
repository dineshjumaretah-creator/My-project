import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from parcelchargesave import *
from parcelchargedelete import *
from parcelchargeupdate import *
from parcelchargefind import *
from parcelchargenavigate import *
from parcelchargeshow import *
def parcelchargealldata():
    t = tkinter.Tk()
    t.config(bg='#35344e')
    t.geometry('1000x1000')
    t.title('ParcelCharge dashboard')
    l1 = Label(t, text='ParcelCharge Dashboard', font=('arial', 20), bg='#f2ede7')
    l1.place(x=500, y=30)
    b1 = Button(t, text='ParcelCharge insert', command=showparinsert, width=20, height=1,font=('arial', 12, 'bold'), bg='red')
    b1.place(x=550, y=80)
    b2 = Button(t, text='ParcelCharge delete', command=showpardelete, width=20, height=1,font=('arial', 12, 'bold'), bg='orange')
    b2.place(x=550, y=120)
    b3 = Button(t, text='ParcelCharge update', command=showparupdate, width=20, height=1,font=('arial', 12, 'bold'), bg='green')
    b3.place(x=550, y=160)
    b4 = Button(t, text='ParcelCharge find', command=showparfind, width=20, height=1,font=('arial', 12, 'bold'), bg='yellow')
    b4.place(x=550, y=200)
    b5 = Button(t, text='ParcelCharge navigate', command=showparnavigate, width=20, height=1,font=('arial', 12, 'bold'), bg='blue')
    b5.place(x=550, y=240)
    b6 = Button(t, text='ParcelCharge show', command=showparshow, width=20, height=1,font=('arial', 12, 'bold'), bg='purple')
    b6.place(x=550, y=280)
    t.mainloop()