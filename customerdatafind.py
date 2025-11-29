import pymysql
from tkinter import messagebox
from tkinter import ttk
import tkinter
from tkinter import *
def showcusfind():
    t = tkinter.Tk()
    t.geometry('700x700')
    t.title("CustomerData")
    t.configure(bg='cyan')
    def finddata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        xa = int(e1.get())
        sql = "SELECT name, address, email, phone FROM customerdata WHERE custid = %d" % xa
        cur.execute(sql)
        data = cur.fetchone()
        db.close()
        if data:
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e2.insert(0, data[0])
            e3.insert(0, data[1])
            e4.insert(0, data[2])
            e5.insert(0, data[3])
        else:
            messagebox.showinfo("Hi", "No recordfound")
    def close():
        t.destroy()
    head=Label(t,text='CURRENT STATUS',bg='yellow',fg='green',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='Custid',bg='yellow',font=('segoe UI',12,'bold'))
    a.place(x=100,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(101,131))
    e1.place(x=300,y=100)
    b=Label(t,text='Name',bg='yellow',font=('segoe UI',12,'bold'))
    b.place(x=100,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=150)
    d=Label(t,text='Address',bg='yellow',font=('segoe UI',12,'bold'))
    d.place(x=100,y=200)
    e3=Entry(t,width=30)
    e3.place(x=300,y=200)
    f=Label(t,text='Email',bg='yellow',font=('segoe UI',12,'bold'))
    f.place(x=100,y=250)
    e4=Entry(t,width=30)
    e4.place(x=300,y=250)
    g=Label(t,text='Phone',bg='yellow',font=('segoe UI',12,'bold'))
    g.place(x=100,y=300)
    e5=Entry(t,width=30)
    e5.place(x=300, y=300)
    btn1=Button(t, text='Find',command=finddata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=400, y=380)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=500,y=380)
    t.mainloop()