import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bookingdatasave import *
from bookingdatadelete import *
from bookingdataupdate import *
from bookingdatafind import *
from bookingdatanavigate import *
from bookingdatashow import *
def bookingalldata():
    t = tkinter.Tk()
    t.config(bg='#35344e')
    t.geometry('1000x1000')
    t.title('Booking dashboard')
    l1 = Label(t, text='courier office dashboard', font=('arial', 20), bg='#f2ede7')
    l1.place(x=500, y=30)
    b1 = Button(t, text='Booking insert', command=showbookinsert, width=20, height=1,font=('arial', 12, 'bold'), bg='red')
    b1.place(x=545, y=80)
    b2 = Button(t, text='Booking delete', command=showbookdelete, width=20, height=1,font=('arial', 12, 'bold'), bg='orange')
    b2.place(x=545, y=120)
    b3 = Button(t, text='Booking update', command=showbookupdate, width=20, height=1,font=('arial', 12, 'bold'), bg='green')
    b3.place(x=545, y=160)
    b4 = Button(t, text='Booking find', command=showbookfind, width=20, height=1,font=('arial', 12, 'bold'), bg='yellow')
    b4.place(x=545, y=200)
    b5 = Button(t, text='Booking navigate', command=showbooknavigate, width=20, height=1,font=('arial', 12, 'bold'), bg='blue')
    b5.place(x=545, y=240)
    b6 = Button(t, text='Booking show', command=showbookshow, width=20, height=1,font=('arial', 12, 'bold'), bg='purple')
    b6.place(x=545, y=280)
    t.mainloop()