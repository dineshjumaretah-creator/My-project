import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def showcofinsert():
    t=tkinter.Tk()
    t.geometry('1000x1000')
    t.config(bg='#35344e')
    def closedata():
        t.destroy()
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
            messagebox.showerror('Error','Please fill all data')
        else:
            try:
                db = pymysql.connect(host="localhost", user='root', password='root', database='cms')
                cur = db.cursor()
                xa = int(e1.get())
                xb = e2.get()
                xc = e3.get()
                xd = e4.get()  # email
                xe = e5.get()
    
                sql = "INSERT INTO coffice VALUES('%s','%s','%s','%s','%s')" % (xa, xb, xc, xd, xe)
                cur.execute(sql)
                db.commit()
    
                # === Email Sending Block ===
                import smtplib
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
        
                from_address = "dineshjumaretah@gmail.com"
                to_address = xd  
        
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Welcome to Courier System"
                msg['From'] = from_address
                msg['To'] = to_address
        
                html = f"""<html>
                    <body>
                        <h3>Dear {xb},</h3>
                        <p>Your registration with customer ID {xa}.</p>
                        <p>Your registration with Address ID {xc}.</p>
                        <p>Your registration with Email ID {xd}.</p>
                        <p>Your registration with Phone no ID {xe}.</p>
                        <p>Thanks,<br>Courier Management System</p>
                    </body>
                </html>"""
                part1 = MIMEText(html, 'html')
                msg.attach(part1)
        
                username = 'dineshjumaretah@gmail.com'
                password = 'ecfasydasefvhyhi'  # Your app-specific Gmail password
        
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(username, password)
                server.sendmail(from_address, to_address, msg.as_string())
                server.quit()
        
                messagebox.showinfo("Success", "Data Saved & Email Sent")
    
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                db.close()
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)

    head=Label(t,text='COFFICE SAVE',bg='#494862',font=('arial',15))
    head.place(x=470,y=20)
    a=Label(t,text="officeid",width=10,height=1,font=('arial',11))
    a.place(x=400,y=70)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(101,150))
    e1.place(x=500,y=70)
    b=Label(t,text="Name",width=10,height=1,font=('arial',11))
    b.place(x=400,y=120)
    e2=Entry(t,width=20,font=('arial',13))
    e2.place(x=500,y=120)
    c=Label(t,text="address",width=10,height=1,font=('arial',11))
    c.place(x=400,y=170)
    e3=Entry(t,width=20,font=('arial',13))
    e3.place(x=500,y=170)
    d=Label(t,text="email",width=10,height=1,font=('arial',11))
    d.place(x=400,y=220)
    e4=Entry(t,width=20,font=('arial',13))
    e4.place(x=500,y=220)
    f=Label(t,text="regno",width=10,height=1,font=('arial',11))
    f.place(x=400,y=270)
    e5=ttk.Combobox(t,width=27)
    e5['values']=list(range(1001,1050))
    e5.place(x=500,y=270)
    bt1=Button(t,text="save",command=savedata,bg='green',fg='white',width=10,height=1,font=('arial',14))
    bt1.place(x=450,y=320)
    bt2=Button(t,text='Close',command=closedata,bg='red',fg='white',width=10,height=1,font=('arial',14))
    bt2.place(x=580,y=320)
    t.mainloop()