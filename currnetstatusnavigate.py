import pymysql
from tkinter import *
import tkinter
from tkinter import messagebox
def showcurnavigate():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title("CustomerData")
    t.configure(bg='cyan')
    xa = []
    xb = []
    xc = []
    xd = []
    i = 0
    def filldata():
        xa.clear()
        xb.clear()
        xc.clear()
        xd.clear()
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        sql = "select * from customerdata"
        cur.execute(sql)
        data = cur.fetchall()
        for row in data:
            xa.append(str(row[0]))
            xb.append(row[1])
            xc.append(row[2])
            xd.append(row[3])
        db.close()
    def showdata(index):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
    
        e1.insert(0, xa[index])
        e2.insert(0, xb[index])
        e3.insert(0, xc[index])
        e4.insert(0, xd[index])
    def firstdata():
        global i
        filldata()
        if xa:
            i = 0
            showdata(i)
    def nextdata():
        global i
        if i < len(xa) - 1:
            i += 1
            showdata(i)
        else:
            messagebox.showinfo("Hi", "Last RecordReached")
    def previousdata():
        global i
        if i > 0:
            i -= 1
            showdata(i)
        else:
            messagebox.showinfo("Start", "First Record Reached")
    def lastdata():
        global i
        filldata()
        if xa:
            i = len(xa) - 1
            showdata(i)
    def close():
        t.destroy()
    head=Label(t,text='Currentstatus STATUS',bg='yellow',fg='green',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='Parcelno',bg='yellow',font=('segoe UI',12,'bold'))
    a.place(x=50,y=50)
    e1=Entry(t,width=30)
    e1.place(x=300,y=50)
    b=Label(t,text='custid',bg='yellow',font=('segoe UI',12,'bold'))
    b.place(x=50,y=100)
    e2=Entry(t,width=30)
    e2.place(x=300,y=100)
    d =Label(t,text='catid',bg='yellow',font=('segoe UI',12,'bold'))
    d.place(x=50,y=150)
    e3=Entry(t,width=30)
    e3.place(x=300,y=150)
    f=Label(t,text='Curentstatus',bg='yellow',font=('segoe UI',12,'bold'))
    f.place(x=50,y=200)
    e4=Entry(t,width=30)
    e4.place(x=300,y=200)
    btn1=Button(t,text='First',command=firstdata,bg='#2e7d32',fg='#ffffff',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=90,y=320)
    btn2=Button(t, text='Next',command=nextdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=180,y=320)
    btn3=Button(t,text='Previous',command=previousdata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn3.place(x=270,y=320)
    btn4=Button(t,text='Last',command=lastdata,bg='#512da8',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn4.place(x=360,y=320)
    btn5=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn5.place(x=460,y=320)
    t.mainloop()