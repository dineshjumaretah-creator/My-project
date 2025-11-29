import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
def showpardelete():
    t=Tk()
    t.geometry('700x700')
    t.title("ParcelCharge")
    t.configure(bg='crimson')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
        cur=db.cursor()
        xa=int(c1.get())
        sql="delete from parcelcharge where catid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo("Hi","Deleted")
        c1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
    def close():
        t.destroy()
    head=Label(t,text='PARCEL CHARGE',bg='yellow',fg='black',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='catid',bg='crimson',font=('segoe UI',18,'bold'))
    a.place(x=100,y=100)
    c1=ttk.Combobox(t,width=27)
    c1['values']=list(range(501,521))
    c1.place(x=300,y=100)
    btn=Button(t,text='Delete',command=deletedata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn.place(x=200,y=360)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=300,y=360)
    t.mainloop()