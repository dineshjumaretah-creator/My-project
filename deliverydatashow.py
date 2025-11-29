import pymysql
import tkinter
from tkinter import *
def showdelshow():
    t=Tk()
    t.geometry('800x600')
    t.title("DeliverData Show")
    t.configure(bg='#93C572')
    def showdata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        sql = "select * from deliverdata"
        cur.execute(sql)
        data = cur.fetchall()
        db.close()
        msg = "ParcelNo\tCustID\tCatID\tCityID\tDateOfDelivery\n"
        msg += "-" * 60 + "\n"
        for row in data:
            msg += f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\n"
        text_box.delete("1.0", END)
        text_box.insert(END, msg)
    def close():
        t.destroy()
    head=Label(t,text='DELIVER DATA',bg='orange',fg='cyan',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    text_box=Text(t,height=25,width=90,bg='yellow',font=('segoe UI',12,'bold'))
    text_box.place(x=20,y=50)
    btn_show=Button(t,text="Show",command=showdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn_show.place(x=150,y=20)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=250,y=20)
    t.mainloop()