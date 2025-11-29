import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox
import tkinter
from tkinter import*
from maindashboard import *
from userdashboard import *
t=tkinter.Tk()
t.geometry('700x400')
t.title("CofficeSave")
t.configure(bg='grey')
def login():
    x=c1.get()
    y=e1.get()
    z=e2.get()
    if x=='Admin':
        if y=='admin' and z=='123':
            messagebox.showinfo('Hi','login ok')
            logindata()
        else:
            messagebox.showinfo('Error','failed')
    elif x=='User':
        if y=='user' and z=='456':
            messagebox.showinfo('Hi','Login ok')
            userlogin()
        else:
            messagebox.showinfo('Hi','login failed')
    
def clear():
    e1.delete(0,100)
    e2.delete(0,100)
head=Label(t,text='Login Panel',bg='grey',font=('segoe UI',16,'bold'))
head.place(x=200,y=40)
d=Label(t,text='for login',bg='grey',font=('segoe UI',12))
d.place(x=100,y=100)
c1=ttk.Combobox(t,width=27)
c1['values']=('Admin','User')
c1.place(x=300,y=100)
a=Label(t,text='Login',bg='grey',font=('segoe UI',12))
a.place(x=100,y=150)
e1=Entry(t,width=30)
e1.place(x=300,y=150)
b=Label(t,text='Password',bg='grey',font=('segoe UI',12))
b.place(x=100,y=200)
e2=Entry(t,width=30,show='*')
e2.place(x=300,y=200)
btn1=Button(t,text='Login',command=login,width=10,bg='green',fg='white')
btn1.place(x=100,y=250)
btn2=Button(t,text='Clear',command=clear,width=10,bg='red',fg='white')
btn2.place(x=200,y=250)

t.mainloop()