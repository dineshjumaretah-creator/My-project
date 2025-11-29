import pymysql
from tkinter import messagebox
import datetime
import tkinter
from tkinter import *
def showbooknavigate():
    t = tkinter.Tk()
    t.geometry('700x700')
    t.title("BookingData")
    t.configure(bg='#93C572')
    xa = []
    xb = []
    xc = []
    xd = []
    xe = []
    i = 0
    def filldata():
        xa.clear()
        xb.clear()
        xc.clear()
        xd.clear()
        xe.clear()
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        sql = "select * from bookingdataa"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(str(res[1]))
            xc.append(str(res[2]))
            xd.append(str(res[3]))
            xe.append(str(res[4]))
        db.close()
    def showdata(index):
        if len(xa) == 0:
            messagebox.showinfo("Hi", "No data found in table.")
            return
    
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
    
        e1.insert(0, xa[index])
        e2.insert(0, xb[index])
        e3.insert(0, xc[index])
        e4.insert(0, xd[index])
        e5.insert(0, xe[index])
    def firstdata():
        global i
        filldata()
        if len(xa) > 0:
            i = 0
            showdata(i)
    def lastdata():
        global i
        filldata()
        if len(xa) > 0:
            i = len(xa) - 1
            showdata(i)
    def nextdata():
        global i
        if len(xa) == 0:
            filldata()
        if i < len(xa) - 1:
            i += 1
            showdata(i)
        else:
            messagebox.showinfo("Info", "Last record reached")
    def previousdata():
        global i
        if len(xa) == 0:
            filldata()
        if i > 0:
            i -= 1
            showdata(i)
        else:
            messagebox.showinfo("Info", "First record reached")
    def close():
        t.destroy()
    head=Label(t,text='BOOKING DATA',bg='#f2ede7',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='customerid',bg='#f2ede7',font=('segoe UI',12,'bold'))
    a.place(x=80,y=100)
    e1=Entry(t,width=30)
    e1.place(x=300,y=100)
    b=Label(t,text='parcelno',bg='#f2ede7',font=('segoe UI',12,'bold'))
    b.place(x=80,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=150)
    d=Label(t,text='catid',bg='#f2ede7',font=('segoe UI',12,'bold'))
    d.place(x=80,y=200)
    e3=Entry(t,width=30)
    e3.place(x=300,y=200)
    f=Label(t,text='cityid',bg='#f2ede7',font=('segoe UI',12,'bold'))
    f.place(x=80,y=250)
    e4=Entry(t,width=30)
    e4.place(x=300,y=250)
    g=Label(t,text='dateofbooking',bg='#f2ede7',font=('segoe UI',12,'bold'))
    g.place(x=80,y=300)
    e5=Entry(t,width=30)
    e5.place(x=300,y=300)
    today=datetime.date.today()
    e5.insert(0,str(today))
    btn1=Button(t,text='First',command=firstdata,bg='#2e7d32',fg='#ffffff',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=100,y=380)
    btn2=Button(t,text='Next',command=nextdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=180,y=380)
    btn3=Button(t,text='Last',command=lastdata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn3.place(x=260,y=380)
    btn4=Button(t,text='Previous',command=previousdata,bg='#512da8',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn4.place(x=340,y=380)
    btn5=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn5.place(x=440,y=380)
    t.mainloop()