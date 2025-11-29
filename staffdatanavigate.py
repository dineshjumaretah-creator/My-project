import pymysql
from tkinter import*
from tkinter import messagebox
def showstnavigate():
    t=Tk()
    t.geometry('700x700')
    t.title("StaffData")
    t.configure(bg='royalblue')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    i=0
    def filldata():
        xa.clear()
        xb.clear()
        xc.clear()
        xd.clear()
        xe.clear()
        db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
        cur=db.cursor()
        cur.execute("select * from staffdata")
        data=cur.fetchall()
        for res in data:
         xa.append(str(res[0]))
         xb.append(res[1])
         xc.append(res[2])
         xd.append(res[3])
         xe.append(str(res[4]))
        db.close()
    def showdata(index):
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.insert(0,xa[index])
        e2.insert(0,xb[index])
        e3.insert(0,xc[index])
        e4.insert(0,xd[index])
        e5.insert(0,xe[index])
    def firstdata():
        global i
        filldata()
        i=0
        showdata(i)
    def lastdata():
        global i
        filldata()
        i=len(xa)-1
        showdata(i)
    def nextdata():
        global i
        if i<len(xa)-1:
         i+=1
         showdata(i)
        else:
         messagebox.showinfo("Info","Last record")
    def previousdata():
        global i
        if i>0:
         i-=1
         showdata(i)
        else:
         messagebox.showinfo("Info","First record")
    def close():
        t.destroy()
    head=Label(t,text='STAFF DATA',bg='royalblue',fg='black',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='staffid',bg='royalblue',font=('segoe UI',18,'bold'))
    a.place(x=100,y=100)
    e1=Entry(t,width=30)
    e1.place(x=300,y=110)
    b=Label(t,text='sname',bg='royalblue',font=('segoe UI',18,'bold'))
    b.place(x=100,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=160)
    c=Label(t,text='address',bg='royalblue',font=('segoe UI',18,'bold'))
    c.place(x=100,y=200)
    e3=Entry(t,width=30)
    e3.place(x=300,y=210)
    d=Label(t,text='email',bg='royalblue',font=('segoe UI',18,'bold'))
    d.place(x=100,y=250)
    e4=Entry(t,width=30)
    e4.place(x=300,y=260)
    e=Label(t,text='phone',bg='royalblue',font=('segoe UI',18,'bold'))
    e.place(x=100,y=300)
    e5=Entry(t,width=30)
    e5.place(x=300,y=310)
    btn1=Button(t,text='First',command=firstdata,bg='#2e7d32',fg='#ffffff',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=90,y=350)
    btn2=Button(t,text='Next',command=nextdata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=180,y=350)
    btn3=Button(t,text='Previous',command=previousdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn3.place(x=270,y=350)
    btn4=Button(t,text='Last',command=lastdata,bg='#512da8',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn4.place(x=360,y=350)
    btn5=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn5.place(x=460,y=350)
    t.mainloop()