import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from customerdatasave import *
from customerdatadelete import *
from customerdataupdate import *
from customerdatafind import *
from customerdatanavigate import *
from customerdatashow import *
def customeralldata():
    t=tkinter.Tk()
    t.config(bg='#35344e')
    t.geometry('1000x1000')
    t.title('City dashboard')
    l1=Label(t,text='Customer Dashboard',font=('arial', 20),bg='#f2ede7')
    l1.place(x=495,y=30)
    b1=Button(t,text='Customer insert',command=showcusinsert,width=20,height=1,font=('arial', 12, 'bold'), bg='red')
    b1.place(x=520, y=80)
    b2=Button(t,text='Customer delete',command=showcusdelete,width=20,height=1,font=('arial', 12, 'bold'), bg='orange')
    b2.place(x=520,y=120)
    b3=Button(t,text='Customer update',command=showcusupdate,width=20,height=1,font=('arial', 12, 'bold'), bg='green')
    b3.place(x=520,y=160)
    b4=Button(t,text='Customer find',command=showcusfind,width=20,height=1,font=('arial', 12, 'bold'), bg='yellow')
    b4.place(x=520,y=200)
    b5=Button(t,text='Customer navigate',command=showcusnavigate,width=20,height=1,font=('arial', 12, 'bold'), bg='blue')
    b5.place(x=520, y=240)
    b6=Button(t,text='Customer show',command=showcusshow,width=20,height=1,font=('arial', 12, 'bold'), bg='purple')
    b6.place(x=520, y=280)
    t.mainloop()