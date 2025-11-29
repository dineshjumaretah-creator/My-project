import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
def showpadelete():
    t=Tk()
    t.geometry('700x700')
    t.title("ParcelCategory")
    t.configure(bg='magenta')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from parcelcategory where catid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo("Hi","Deleted")
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
    def close():
        t.destroy()
    head=Label(t,text='PARCELCATEGORY',bg='yellow',fg='black',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='catid',bg='magenta',font=('segoe UI',18,'bold'))
    a.place(x=100,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(501,521))
    e1.place(x=300,y=100)
    btn1=Button(t,text='Delete',command=deletedata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=180,y=300)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=280,y=300)
    t.mainloop()