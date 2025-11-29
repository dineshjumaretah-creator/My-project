import pymysql
import tkinter
from tkinter import*
def showpashow():
    t=Tk()
    t.geometry('800x600')
    t.title("ParcelCategory")
    t.configure(bg='magenta')
    head=Label(t,text='PARCELCATEGORY',bg='yellow',fg='black',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='cms')
        cur=db.cursor()
        sql="select * from parcelcategory"
        cur.execute(sql)
        data=cur.fetchall()
        msg=""
        for res in data:
         msg+=str(res[0])+"\t"+res[1]+"\t"+str(res[2])+"\t"+str(res[3])+"\n"
        txt.insert(END,msg)
        db.close()
    def close():
        t.destroy()
    txt=Text(t,height=10,width=50,bg='grey',font=('segoe UI',18,'bold'))
    txt.place(x=50,y=50)
    btn=Button(t,text='Show',command=showdata,bg='#1565c0',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn.place(x=350,y=400)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=430,y=400)
    t.mainloop()