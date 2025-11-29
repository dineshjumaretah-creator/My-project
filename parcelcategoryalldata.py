import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from parcelcategorysave import *
from parcelcategorydelete import *
from parcelcategoryupdate import *
from parcelcategoryfind import *
from parcelcategorynavigate import *
from parcelcategoryshow import *
def parcelcategoryalldata():
    t = tkinter.Tk()
    t.config(bg='#35344e')
    t.geometry('1000x1000')
    t.title('Parcelcategory dashboard')
    l1 = Label(t, text='Parcelcategory Dashboard', font=('arial', 20), bg='#f2ede7')
    l1.place(x=500, y=30)
    b1 = Button(t, text='Parcelcategory insert', command=showpainsert, width=20, height=1,font=('arial', 12, 'bold'), bg='red')
    b1.place(x=560, y=80)
    b2 = Button(t, text='Parcelcategory delete', command=showpadelete, width=20, height=1,font=('arial', 12, 'bold'), bg='orange')
    b2.place(x=560, y=120)
    b3 = Button(t, text='Parcelcategory update', command=showpaupdate, width=20, height=1,font=('arial', 12, 'bold'), bg='green')
    b3.place(x=560, y=160)
    b4 = Button(t, text='Parcelcategory find', command=showpafind, width=20, height=1,font=('arial', 12, 'bold'), bg='yellow')
    b4.place(x=560, y=200)
    b5 = Button(t, text='Parcelcategory navigate', command=showpanavigate, width=20, height=1,font=('arial', 12, 'bold'), bg='blue')
    b5.place(x=560, y=240)
    b6 = Button(t, text='Parcelcategory show', command=showpashow, width=20, height=1,font=('arial', 12, 'bold'), bg='purple')
    b6.place(x=560, y=280)
    t.mainloop()