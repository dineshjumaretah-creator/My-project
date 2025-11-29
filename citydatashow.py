import pymysql
import tkinter
from tkinter import *
def showcityshow():
    t = tkinter.Tk()
    t.geometry('800x600')
    t.title("CityData")
    t.configure(bg='#93C572')
    def showdata():
        a.delete('1.0', END)
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        sql = "SELECT * FROM citydata"
        cur.execute(sql)
        data = cur.fetchall()
        msg = "CityID\tCityName\tState\tPincode\n"
        msg += "-" * 50 + "\n"
        for res in data:
            msg += str(res[0]) + "\t" + res[1] + "\t" + res[2] + "\t" + str(res[3]) + "\n"
        db.close()
        a.insert(END, msg)
    def close():
        t.destroy()
    head=Label(t,text='CITY DATA',bg='#f2ede7',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a = Text(t, height=20, width=80,bg='#f2ede7',font=('segoe UI',12,'bold'))
    a.place(x=50, y=70)
    btn1 = Button(t, text='Show', command=showdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=15,height=1)
    btn1.place(x=350,y=500)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=450,y=500)
    t.mainloop()