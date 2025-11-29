import pymysql
from tkinter import messagebox
from tkinter import ttk
import tkinter
import datetime
from tkinter import *
def showdeldelete():
    t=Tk()
    t.geometry('700x700')
    t.title("DeliveryData")
    t.configure(bg='orange')
    def deletedata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        xa = int(e1.get())
        sql = "delete from deliverdata where parcelno = %d" % xa
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo("Hi","deleted successfully")
        e1.delete(0, END)
    def close():
        t.destroy()
    head=Label(t,text='DELIVER DATA',bg='orange',fg='cyan',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='Parcelno',bg='orange',font=('segoe UI',12,'bold'))
    a.place(x=100,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(101,131))
    e1.place(x=300,y=100)
    btn1=Button(t,text='Delete',command=deletedata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=200, y=200)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=300,y=200)
    t.mainloop()