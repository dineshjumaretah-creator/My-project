import pymysql
from tkinter import messagebox
import tkinter
from tkinter import*
from tkinter import ttk
def showbookdelete():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title("BookingData")
    t.configure(bg='#93C572')
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from bookingdataa where custid=%s"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','DataDeleted')
    def close():
        t.destroy()
    head=Label(t,text='BOOKING DATA',bg='#f2ede7',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='customerid',bg='#f2ede7',font=('segoe UI',12,'bold'))
    a.place(x=100,y=150)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(101,120))
    e1.place(x=300,y=150)
    btn1=Button(t,text='Delete',command=deletedata,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=130,y=230)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=230,y=230)
    t.mainloop()