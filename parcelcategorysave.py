import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def showpainsert():
    t = Tk()
    t.geometry('700x500')
    t.title("ParcelCategory")
    t.configure(bg='lightblue')

    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            messagebox.showerror('Error', 'Please fill all fields')
        else:
            db = pymysql.connect(host='localhost', user='root', password='root', database='cms')
            cur = db.cursor()

            xa = int(e1.get())   # catid
            xb = e2.get()        # catname
            xc = e3.get()        # mincharges
            xd = e4.get()        # distancecharges

            sql = "INSERT INTO parcelcategory (catid, catname, minweight, maxweight) VALUES ('%s','%s','%s','%s')" % (xa, xb, xc, xd)
            cur.execute(sql)
            db.commit()
            db.close()

            from_address = "dineshjumaretah@gmail.com"
            to_address = "receiver@gmail.com"   # <- yaha apna ya customer email daalein

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Parcel Category Saved"
            msg['From'] = from_address
            msg['To'] = to_address

            html = f"""<html>
                <body>
                    <h3>New Parcel Category Saved:</h3>
                    <p><b>Catid:</b> {xa}</p>
                    <p><b>catname:</b> {xb}</p>
                    <p><b>Minweight:</b> {xc}</p>
                    <p><b>maxweight:</b> {xd}</p>
                    <p>Thanks,<br>Courier Management System</p>
                </body>
            </html>"""

            part = MIMEText(html, 'html')
            msg.attach(part)

            username = "dineshjumaretah@gmail.com"
            password = "dlqnwrntmubftusu"  # Gmail app password

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()

            messagebox.showinfo("Success", "Data Saved & Email Sent")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
    def close():
        t.destroy()
    head=Label(t,text='PARCELCATEGORY',bg='lightblue',fg='black',font=('segoe UI',18,'bold'))
    head.place(x=280,y=10)
    a=Label(t,text='catid',bg='lightblue',font=('segoe UI',12,'bold'))
    a.place(x=100,y=100)
    e1=ttk.Combobox(t,width=27)
    e1['values']=list(range(501,521))
    e1.place(x=300,y=100)
    b=Label(t,text='catname',bg='lightblue',font=('segoe UI',12,'bold'))
    b.place(x=100,y=150)
    e2=Entry(t,width=30)
    e2.place(x=300,y=150)
    c=Label(t,text='minweight',bg='lightblue',font=('segoe UI',12,'bold'))
    c.place(x=100,y=200)
    e3=ttk.Combobox(t,width=27)
    e3['values']=list(range(50,500))
    e3.place(x=300,y=200)
    d=Label(t,text='maxweight',bg='lightblue',font=('segoe UI',12,'bold'))
    d.place(x=100,y=250)
    e4=ttk.Combobox(t,width=27)
    e4['values']=list(range(500,1000))
    e4.place(x=300,y=250)
    btn=Button(t,text='Save',command=savedata,bg='#2e7d32',fg='#ffffff',font=('calibri',11,'bold'),width=10,height=1)
    btn.place(x=100,y=350)
    btn2=Button(t,text='Close',command=close,bg='#e53935',fg='white',font=('calibri',11,'bold'),width=10,height=1)
    btn2.place(x=200,y=350)

    t.mainloop()