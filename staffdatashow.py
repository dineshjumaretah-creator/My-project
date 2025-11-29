import pymysql
from tkinter import messagebox
import tkinter
from tkinter import *
def showstshow():
    t=tkinter.Tk()
    t.geometry('800x700')
    t.title("StaffData")
    t.configure(bg='#93C572')
    def showdata():
        a.delete('1.0', END)
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        sql = "select * from staffdata"
        cur.execute(sql)
        data = cur.fetchall()
        msg = ""
        for res in data:
            msg += str(res[0]) + "\t" + res[1] + "\t" + res[2] + "\t" + res[3] + "\t" + res[4] + "\n"
        db.close()
        a.insert(END, msg)
    def close():
        t.destroy()
    a=Text(t,height=20,width=80)
    a.place(x=30,y=50)
    btn1=Button(t,text="Show",command=showdata)
    btn1.place(x=100,y=400)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=230,y=400)
    t.mainloop()