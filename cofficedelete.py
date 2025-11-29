import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showcoffdelete():
    t=Tk()
    t.geometry('700x550')
    t.title("CofficeDelete")
    t.configure(bg='yellow')
    def deletedata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        xo = int(e1.get())
        sql = "delete from coffice where officeid=%d" %(xo)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo("Hi", " Deleted Successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
    def close():
        t.destroy()
    head=Label(t,text='CITY DATA',bg='yellow',fg='green',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t, text='Officeid', bg='yellow',font=('segoe UI',18,'bold'))
    a.place(x=100, y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(1001,1021))
    e1.place(x=300,y=100)
    btn1 = Button(t, text='Delete', command=deletedata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=100, y=250)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=200,y=250)
    t.mainloop()