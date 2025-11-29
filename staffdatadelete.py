import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
def showstdelete():
    t=Tk()
    t.geometry('700x700')
    t.title("StaffData")
    t.configure(bg='royalblue')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from staffdata where staffid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo("Hi","Deleted")
        e1.delete(0,100)
    def close():
        t.destroy()
    head=Label(t,text='STAFF DATA',bg='royalblue',fg='black',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='staffid',bg='royalblue',font=('segoe UI',18,'bold'))
    a.place(x=100,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(3001,3021))
    e1.place(x=300,y=100)
    btn1=Button(t,text='Delete',command=deletedata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=100,y=280)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=200,y=280)
    t.mainloop()