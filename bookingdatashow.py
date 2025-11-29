import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
def showbookshow():
    t = tkinter.Tk()
    t.geometry('1000x1000')
    t.title("BookingData")
    t.configure(bg='#93C572')
    def filldata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        sql = "select * from bookingdataa"
        msg = ""
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            msg = msg + str(res[0]) + "\t"
            msg = msg + str(res[1]) + "\t"   
            msg = msg + str(res[2]) + "\t"   
            msg = msg + str(res[3]) + "\t"   
            msg = msg + str(res[4]) + "\n"   
        db.close()
        a.delete(1.0, END)
        a.insert(END, msg)
    def close():
        t.destroy()
    head=Label(t,text='BOOKING DATA',bg='#f2ede7',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Text(t,height=20,width=80,bg='#f2ede7',font=('segoe UI',12,'bold'))
    a.place(x=10,y=10)
    btn1=Button(t,text="Show Booking Data",command=filldata,bg='#1565c0',fg='yellow',font=('calibri',11,'bold'),width=15,height=1)
    btn1.place(x=10,y=450)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=140,y=450)
    t.mainloop()