import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
def showcitydelete():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title("CityData")
    t.configure(bg='grey')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from citydata where cityid=%s"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','DataDeleted')
    def close():
        t.destroy()
    head=Label(t,text='CITY DATA',bg='#f2ede7',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='cityid',bg='#f2ede7',font=('segoe UI',12,'bold'))
    a.place(x=100,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(201,221))
    e1.place(x=300,y=100)
    btn1=Button(t,text='Delete',command=deletedata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=100,y=180)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=200,y=180)
    t.mainloop()