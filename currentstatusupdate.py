import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showcurupdate():
    t = Tk()
    t.geometry('700x700')
    t.title("CurrentStatusUpdate")
    t.configure(bg='yellow')
    
    def updatedata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        xa = int(e1.get())
        xb = int(e2.get())
        xc = int(e3.get())
        xd = e4.get()
        sql = "update currentstatusdataa set custid=%s, catid=%s, currentstate=%s where parcelno=%s"
        cur.execute(sql, (xb, xc, xd, xa))
        db.commit()
        db.close()
        messagebox.showinfo("Hi", "Updated Successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
    def finddata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        xa = int(e1.get())
        sql = "select * from currentstatusdataa where parcelno=%s"
        cur.execute(sql, (xa,))
        data = cur.fetchone()
        if data:
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e2.insert(0, data[1])
            e3.insert(0, data[2])
            e4.insert(0, data[3])
        else:
            messagebox.showinfo("Hi", "Data Not Found")
        db.close()
    def close():
        t.destroy()
    head=Label(t,text='CURRENTSTATUSDATA',bg='yellow',font=('segoe UI',18,'bold'))
    head.place(x=200,y=10)
    
    a=Label(t,text='ParcelNo', bg='yellow',font=('segoe UI',12,'bold'))
    a.place(x=80,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(301,331))
    e1.place(x=300,y=100)
    
    b=Label(t,text='CustID',bg='yellow',font=('segoe UI',12,'bold'))
    b.place(x=80,y=150)
    e2=ttk.Combobox(t,width=27)
    e2['values']=list(range(101,121))
    e2.place(x=300,y=150)
    
    c=Label(t,text='CatID',bg='yellow',font=('segoe UI',12,'bold'))
    c.place(x=80,y=200)
    e3=ttk.Combobox(t,width=27)
    e3['values']=list(range(501,531))
    e3.place(x=300,y=200)
    
    d=Label(t,text='CurrentStatus',bg='yellow',font=('segoe UI',12,'bold'))
    d.place(x=80,y=250)
    e4=ttk.Combobox(t,width=27)
    e4['values']=('Mumbai','Agra','Delhi','Noida','Mainpuri')
    e4.place(x=300,y=250)
    btn1=Button(t,text='Update',command=updatedata,bg='blue',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=150,y=320)
    btn2=Button(t,text='Find',command=finddata,bg='orange',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=250,y=320)
    btn3=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn3.place(x=350,y=320)
    
    t.mainloop()