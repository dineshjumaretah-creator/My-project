import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def showcusinsert():
    t=tkinter.Tk()
    t.geometry('1000x1000')
    t.config(bg='#35344e')
    def savedata():
        if (len(e1.get()) == 0 or len(e2.get()) == 0 
            or len(e3.get()) == 0 or len(e4.get()) == 0 
            or len(e5.get()) == 0):
            messagebox.showerror('Error', 'Please fill all data')
            return
    
        phone = e5.get()
        if not phone.isdigit():
            messagebox.showerror('Error', 'Phone number must contain only digits')
            return
        if len(phone) != 10:
            messagebox.showerror('Error', 'Phone number must be exactly 10 digits')
            return
    
        try:
            db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
            cur = db.cursor()
            xa = int(e1.get())
            xb = e2.get()
            xc = e3.get()
            xd = e4.get()  # <-- Email address from Entry
            xe = phone
    
            sql = "INSERT INTO customerdata VALUES('%s','%s','%s','%s','%s')" % (xa, xb, xc, xd, xe)
            cur.execute(sql)
            db.commit()
    
            # === Email Sending Block ===
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
    
            from_address = "dineshjumaretah@gmail.com"
            to_address = xd  # <-- use email from e4
    
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Welcome to Courier System"
            msg['From'] = from_address
            msg['To'] = to_address
    
            html = f"""<html>
                <body>
                    <h3>Dear {xb},</h3>
                    <p>Your registration with customer ID {xa} has been saved successfully.</p>
                    <p>Thanks,<br>Courier Management System</p>
                </body>
            </html>"""
            part1 = MIMEText(html, 'html')
            msg.attach(part1)
    
            username = 'dineshjumaretah@gmail.com'
            password = 'dlqnwrntmubftusu'  # Your app-specific Gmail password
    
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()
    
            messagebox.showinfo("Success", "Data Saved & Email Sent")
    
        except Exception as err:
            messagebox.showerror("Error", str(err))
        finally:
            db.close()
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)

    head=Label(t,text='CUSTOMERDATA SAVE',bg='#494862',font=('arial',15))
    head.place(x=400,y=20)
    a=Label(t,text="custid",width=10,height=1,font=('arial',11))
    a.place(x=380,y=70)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(501,550))
    e1.place(x=500,y=70)
    b=Label(t,text="cname",width=10,height=1,font=('arial',11))
    b.place(x=380,y=120)
    e2=Entry(t,width=20,font=('arial',13))
    e2.place(x=500,y=120)
    c=Label(t,text="address",width=10,height=1,font=('arial',11))
    c.place(x=380,y=170)
    e3=Entry(t,width=20,font=('arial',13))
    e3.place(x=500,y=170)
    d=Label(t,text="email",width=10,height=1,font=('arial',11))
    d.place(x=380,y=220)
    e4=Entry(t,width=20,font=('arial',13))
    e4.place(x=500,y=220)
    f=Label(t,text="phone",width=10,height=1,font=('arial',11))
    f.place(x=380,y=270)
    e5=Entry(t,width=20,font=('arial',13))
    e5.place(x=500,y=270)
    bt1=Button(t,text="save",command=savedata,bg='green',width=10,height=1,font=('arial',15))
    bt1.place(x=400,y=320)
    bt2=Button(t,text="close",command=savedata,bg='red',width=10,height=1,font=('arial',15))
    bt2.place(x=550,y=320)
    t.mainloop()