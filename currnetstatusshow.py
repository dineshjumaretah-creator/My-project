import pymysql
from tkinter import messagebox
import tkinter
from tkinter import *
def showcurshow():
    t=tkinter.Tk()
    t.geometry('900x700')
    t.title("CurrentStatusDataa")
    t.configure(bg='#93C572')
    def showdata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        sql = "SELECT * FROM currentstatusdataa"
        cur.execute(sql)
        data = cur.fetchall()
        msg = ""
        for row in data:
            msg += str(row[0]) + "\t"
            msg += str(row[1]) + "\t"
            msg += str(row[2]) + "\t"
            msg += row[3] + "\n"
        db.close()
        a.delete(1.0, END)
        a.insert(END, msg)
    def close():
        t.destroy()
    head=Label(t,text='CITY DATA',bg='yellow',fg='green',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Text(t, height=25,width=100,bg='yellow',font=('segoe UI',12,'bold'))
    a.place(x=50,y=50)
    btn1=Button(t, text='Show',command=showdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=400,y=600)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=500,y=600)
    t.mainloop()