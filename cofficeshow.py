import pymysql
from tkinter import *
def showcoffshow():
    t=Tk()
    t.geometry('800x700')
    t.title("Coffice - Show Records")
    t.configure(bg='#93C572')
    def showdata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        sql = "select * from coffice"
        cur.execute(sql)
        data = cur.fetchall()
        msg = ""
        for res in data:
            msg += str(res[0]) + "\t"
            msg += res[1] + "\t"
            msg += res[2] + "\t"
            msg += res[3] + "\t"
            msg += str(res[4]) + "\n"
        db.close()
        a.delete('1.0', END)
        a.insert(END, msg)
    def close():
        t.destroy()
    head=Label(t,text='CITY DATA',bg='yellow',fg='green',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Text(t, height=20, width=90,bg='yellow',font=('segoe UI',12,'bold'))
    a.place(x=50, y=50)
    btn1 = Button(t, text='Show', command=showdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=100, y=500)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=200,y=500)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=300,y=500)
    t.mainloop()