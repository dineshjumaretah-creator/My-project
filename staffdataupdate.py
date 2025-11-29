import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
def showstupdate():
    t=Tk()
    t.geometry('700x700')
    t.title("StaffData")
    t.configure(bg='royalblue')
    def updatedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
            messagebox.showinfo('Hi','please fill 10 digit number')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
            cur=db.cursor()
            xa=int(e1.get())
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            sql="update staffdata set sname='%s',address='%s',email='%s',phone='%s' where staffid=%d"%(xb,xc,xd,xe,xa)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo("Hi","Updated")
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
    def finddata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
            messagebox.showinfo('Hi','please fill 10 digit number')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
            cur=db.cursor()
            xa=int(e1.get())
            sql="select sname,address,email,phone from staffdata where staffid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data:
             
             e2.delete(0,100)
             e3.delete(0,100)
             e4.delete(0,100)
             e5.delete(0,100)
        
             e2.insert(0,data[0])
             e3.insert(0,data[1])
             e4.insert(0,data[2])
             e5.insert(0,data[3])
            else:
             messagebox.showinfo("Not Found","Record not found")
            db.close()
    def close():
        t.destroy()
    head=Label(t,text='STAFF DATA',bg='royalblue',fg='black',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='staffid',bg='royalblue',font=('segoe UI',18,'bold'))
    a.place(x=100,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(3001,3021))
    e1.place(x=300,y=100)
    b=Label(t,text='sname',bg='royalblue',font=('segoe UI',18,'bold'))
    b.place(x=100,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=160)
    c=Label(t,text='address',bg='royalblue',font=('segoe UI',18,'bold'))
    c.place(x=100,y=200)
    e3=Entry(t,width=30)
    e3.place(x=300,y=200)
    d=Label(t,text='email',bg='royalblue',font=('segoe UI',18,'bold'))
    d.place(x=100,y=250)
    e4=Entry(t,width=30)
    e4.place(x=300,y=260)
    f=Label(t,text='phone',bg='royalblue',font=('segoe UI',18,'bold'))
    f.place(x=100,y=300)
    e5=Entry(t,width=30)
    e5.place(x=300,y=310)
    btn1=Button(t,text='Update',command=updatedata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=120,y=380)
    btn2=Button(t,text='Find',command=finddata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=220,y=380)
    btn3=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn3.place(x=330,y=380)
    t.mainloop()