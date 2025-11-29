import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
def showcurdelete():
    t = Tk()
    t.geometry('700x700')
    t.title("CurrentStatusDelete")
    t.configure(bg='yellow')
    def deletedata():
        db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
        cur = db.cursor()
        xa = int(e1.get())
        sql = "delete from currentstatusdataa where parcelno=%s"
        cur.execute(sql, (xa,))
        db.commit()
        db.close()
        messagebox.showinfo("Hi", "Deleted Successfully")
        e1.delete(0, END)
    def close():
        t.destroy()
    head=Label(t,text='CURRENTSTATUSDATA',bg='yellow',font=('segoe UI',18,'bold'))
    head.place(x=200,y=10)
    
    a=Label(t,text='ParcelNo', bg='yellow',font=('segoe UI',12,'bold'))
    a.place(x=80,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(301,331))
    e1.place(x=300,y=100)
    
    btn1=Button(t,text='Delete',command=deletedata,bg='red',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn1.place(x=150,y=160)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=250,y=160)
    
    t.mainloop()