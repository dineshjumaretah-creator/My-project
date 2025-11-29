import pymysql
from tkinter import *
from tkinter import messagebox
def showcusshow():
    t=Tk()
    t.geometry("800x600")
    t.title("CustomerData")
    t.configure(bg='cyan')
    def showdata():
        db = pymysql.connect(host="localhost", user="root", password="root", database="cms")
        cur = db.cursor()
        sql = "select * from customerdata"
        cur.execute(sql)
        data = cur.fetchall()
        db.close()
        a.delete(1.0, END)
        msg = "CustID\tName\tAddress\tEmail\tPhone\n"
        msg += "-"*80 + "\n"
        for row in data:
            msg += f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\n"
        a.insert(END, msg)
    def close():
        t.destroy()
    head=Label(t,text='CURRENT STATUS',bg='yellow',fg='green',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Text(t,width=90,height=25,bg='yellow',font=('segoe UI',12,'bold'))
    a.place(x=20, y=50)
    btn1=Button(t,text='Show',command=showdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=350,y=500)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=450,y=500)
    t.mainloop()