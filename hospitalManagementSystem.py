from tkinter import*
import mysql.connector as pymy
import tkinter.messagebox as msgbox

                                #establishing db connection
mycon=pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
mycur=mycon.cursor()
                    #creating db
mycur.execute("CREATE DATABASE if not exists HOSPITAL")
mycur.execute("USE HOSPITAL")
    
                                                    #creating tables
mycur.execute("""CREATE TABLE if not exists PATIENT(PId int(10) primary key,Name varchar(30) not null,DOB Date,Gender varchar(15),
              Age int(3),Address varchar(50),Phone_Number varchar(10),Department varchar(20) not null,Doctor varchar(30) not null)""")
mycur.execute("""CREATE TABLE if not exists STAFF(SId int(10) primary key,Name varchar(30) not null,DOB Date,
Designation char(20) not null,Department varchar(20) not null,Address varchar(50),Phone_Number varchar(10),Monthly_Salary int(10))""")
                                #table for user id and passwd of the user
mycur.execute("CREATE TABLE if not exists user(username varchar(30) primary key,password varchar(15) not null)")
mycon.close()

#ROOT WINDOW REFERENCE
root=Tk()
root.geometry("480x250")
space="  "
root.title(20*space+"WELCOME TO MEDICARE HOSPITAL")
root.configure(bg='deep sky blue')

#login option
signin= Label(root,text='SIGN IN', font=("italics",17))  #creating label
signin.place(x=206,y=10)   #margin frm left nd top                     #putting the variables on screen
uname=Label(root,text='Username', font=("italics",14))   
uname.place(x=205,y=60)
un=Entry(justify="center")                          #accepting username input frm user
un.place(x=189,y=100)
upass=Label(root,text='Password', font=("italics",14))
upass.place(x=205,y=130)
up=Entry(show="*",justify="center")          #accepting pswd frm user
up.place(x=189,y=170)


def sw(window):               #to show hidden window
    window.deiconify()
def hw(window):               #to hide a window
    window.withdraw()         
#Verifying
def ok():
    UN=un.get()
    UP=up.get()
    if (UN =="" or UP=="") :
        msgbox.showwarning("Current Status ","Username and Password is required!")
    else:       
        mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
        mycur = mycon.cursor()
        mycur.execute("Select * from user where username='"+ UN +"'")
        rows= mycur.fetchall()

        for row in rows:
            a,b=row
            if b==UP:
                sw(home)
                mycon.close()
                hw(root)
                break
            else:
                msgbox.showwarning("Current Status ","Permission Denied\nInvalid Password")
        else:
            msgbox.showwarning("Current Status ","Permission Denied\nInvalid Username")
        
ok =Button(root,text="OK",font=("italics",10),command=ok)    #function by name of ok already created above
ok.place(x=235,y=210)

#Child Window
home=Toplevel(root)
home.geometry("600x300")
home.title(43*space+"HOME PAGE")
home.configure(bg='spring green')
hw(home)
    
#HOME WINDOW - Options
def Quit(window):
    window.destroy()
    import sys
    sys.exit()
def patient():
    pdetail=Toplevel()
    pdetail.geometry("585x420")
    pdetail.title(35*space+"PATIENT DETAILS")
    pdetail.configure(bg="orange")
    hw(home)
    #patient details pg
    pid = Label(pdetail,text='Patient ID', font=(13))    
    pid.place(x=20, y=20)
    e_pid =Entry(pdetail,justify="center")
    e_pid.place(x=300,y=20)
    name = Label(pdetail,text='Name', font=(13))  
    name.place(x=20, y=50)
    e_name =Entry(pdetail,justify="center")
    e_name.place(x=300,y=50)
    dob = Label(pdetail,text='D.O.B.', font=(13))  
    dob.place(x=20, y=95)
    dd = Label(pdetail,text='DD', font=(10))
    dd.place(x=210, y=80)
    mm = Label(pdetail,text='MM', font=(10))
    mm.place(x=350, y=80)
    yyyy = Label(pdetail,text='YYYY', font=(10))
    yyyy.place(x=486, y=80)
    e_dat =Entry(pdetail,justify="center")
    e_dat.place(x=160,y=110)
    e_mon =Entry(pdetail,justify="center")
    e_mon.place(x=300,y=110)
    e_yr =Entry(pdetail,justify="center")
    e_yr.place(x=440,y=110)
    gndr = Label(pdetail,text='Gender', font=(13))  
    gndr.place(x=20, y=140)
    e_gndr =Entry(pdetail,justify="center")
    e_gndr.place(x=300,y=140)
    age = Label(pdetail,text='Age', font=(13))  
    age.place(x=20, y=170)
    e_age =Entry(pdetail,justify="center")
    e_age.place(x=300,y=170)
    add = Label(pdetail,text='Address', font=(13))  
    add.place(x=20, y=200)
    e_add =Entry(pdetail,justify="center")
    e_add.place(x=300,y=200)
    phn = Label(pdetail,text='Phone Number', font=(13))  
    phn.place(x=20, y=230)
    e_phn =Entry(pdetail,justify="center")
    e_phn.place(x=300,y=230)
    dep = Label(pdetail,text='Department', font=(13))  
    dep.place(x=20, y=260)
    e_dep =Entry(pdetail,justify="center")
    e_dep.place(x=300,y=260)
    doc = Label(pdetail,text='Doctor', font=(13))  
    doc.place(x=20, y=290)
    e_doc =Entry(pdetail,justify="center")
    e_doc.place(x=300,y=290)

    def Quit(window):
        sw(home)
        
    def clear():
        e_pid.delete(0, 'end')               #deleting char in given range of textbox
        e_name.delete(0, 'end')
        e_dat.delete(0, 'end')
        e_mon.delete(0, 'end')
        e_yr.delete(0, 'end')
        e_gndr.delete(0, 'end')
        e_age.delete(0, 'end')
        e_add.delete(0, 'end')
        e_phn.delete(0, 'end')
        e_dep.delete(0, 'end')
        e_doc.delete(0, 'end')
    
    def insert():
        g_pid =e_pid.get()
        g_name =e_name.get()
        g_dob=e_yr.get()+'-'+e_mon.get()+'-'+e_dat.get()
        g_gndr =e_gndr.get()
        g_age =e_age.get()
        g_add =e_add.get()
        g_phn =e_phn.get()
        g_dep =e_dep.get()
        g_doc =e_doc.get()
    
        if(g_pid=="" or g_name=="" or g_dob=="" or  g_gndr=="" or g_age=="" or g_add=="" or g_phn=="" or g_dep=="" or g_doc=="") :
            msgbox.showinfo("Insert Status", "All Fields are required")
        elif str(g_pid).isdigit()==False or str(g_age).isdigit()==False or str(g_phn).isdigit()==False:
            msgbox.showinfo("Insert Status", "Invalid Entry")
        else:
            mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
            mycur =mycon.cursor()
            mycur.execute("Insert into patient values('"+ g_pid + "','"+ g_name +"','"+ g_dob +"','"+ g_gndr +"','"+ g_age +"','"+ g_add +"','"+ g_phn +"','"+ g_dep +"','"+ g_doc +"') ")
            mycon.commit()
            clear()        
            msgbox.showinfo("Insert Status","Inserted Successfully") #1st one is title of msg box 2nd is msg
            mycon.close()
    def delete():
        if e_pid.get()=="":
            msgbox.showinfo("Delete Status ","Patient ID is compulsory for deletion")
        else:
            mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
            mycur = mycon.cursor()
            mycur.execute("Delete from patient where PId='"+ e_pid.get() +"'")
            mycon.commit()
            clear()
            msgbox.showinfo("Delete Status","Deleted Successfully") 
            mycon.close()
    def update():
        g_pid =e_pid.get()
        g_name =e_name.get()
        g_dob=e_yr.get()+'-'+e_mon.get()+'-'+e_dat.get()
        g_gndr =e_gndr.get()
        g_age =e_age.get()
        g_add =e_add.get()
        g_phn =e_phn.get()
        g_dep =e_dep.get()
        g_doc =e_doc.get()
    
        if(g_pid=="" or g_name=="" or g_dob=="" or  g_gndr=="" or g_age=="" or g_add=="" or g_phn=="" or g_dep=="" or g_doc=="") :
            msgbox.showinfo("Update Status", "All Fields are required")
        elif str(g_pid).isdigit()==False or str(g_age).isdigit()==False or str(g_phn).isdigit()==False:
            msgbox.showinfo("Update Status", "Invalid Entry")
        else:
            mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
            mycur =mycon.cursor()
            mycur.execute("Update patient set Name='"+ g_name +"',DOB='"+ g_dob +"',Gender='"+ g_gndr +"',Age='"+ g_age +"',Address='"+ g_add +"',Phone_Number='"+ g_phn +"',Department='"+ g_dep +"',Doctor='"+ g_doc +"' where PId='"+ g_pid +"' ")
            mycon.commit()
            clear()
            msgbox.showinfo("Update Status","Updated Successfully") 
            mycon.close()
    def display():
        if (e_pid.get() ==""):
            msgbox.showinfo("Fetch Status ","ID is compulsory for fetching")
        else:
            mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
            mycur = mycon.cursor()
            mycur.execute(" Select * from patient where PId='"+ e_pid.get() +"' ")
            rows= mycur.fetchall()
        
            for row in rows:
                e_name.insert(0, row[1])
                r=str(row[2])
                yr,mon,dat=r.split('-')
                e_dat.insert(0, dat)
                e_mon.insert(0, mon)
                e_yr.insert(0, yr)
                e_gndr.insert(0, row[3])
                e_age.insert(0, row[4])
                e_add.insert(0, row[5])
                e_phn.insert(0, row[6])
                e_dep.insert(0, row[7])
                e_doc.insert(0, row[8])

            mycon.close()

    insert=Button(pdetail,text="INSERT",font=("italics",13),command=insert)
    insert.place(x=20,y=360)
    update=Button(pdetail,text="UPDATE",font=("italics",13),command=update)
    update.place(x=137,y=360)
    delete=Button(pdetail,text="DELETE",font=("italics",13),command=delete)
    delete.place(x=258,y=360)
    display=Button(pdetail,text="DISPLAY",font=("italics",13),command=display)
    display.place(x=382,y=360)
    Qt=Button(pdetail,text="QUIT",font=("italics",13),command=lambda: Quit(root))
    Qt.place(x=514,y=360)
def staff():
    sdetail=Toplevel()
    sdetail.geometry("585x420")
    sdetail.title(35*space+"STAFF DETAILS")
    sdetail.configure(bg="orange")
    hw(home)
    #staff details pg
    sid = Label(sdetail,text='Staff ID', font=(13))  
    sid.place(x=20, y=20)
    e_sid =Entry(sdetail,justify="center")
    e_sid.place(x=300,y=20)
    name = Label(sdetail,text='Name', font=(13))  
    name.place(x=20, y=50)
    e_name =Entry(sdetail,justify="center")
    e_name.place(x=300,y=50)
    dob = Label(sdetail,text='D.O.B.', font=(13))  
    dob.place(x=20, y=95)
    dd = Label(sdetail,text='DD', font=(10))
    dd.place(x=210, y=80)
    mm = Label(sdetail,text='MM', font=(10))
    mm.place(x=350, y=80)
    yyyy = Label(sdetail,text='YYYY', font=(10))
    yyyy.place(x=486, y=80)
    e_dat =Entry(sdetail,justify="center")
    e_dat.place(x=160,y=110)
    e_mon =Entry(sdetail,justify="center")
    e_mon.place(x=300,y=110)
    e_yr =Entry(sdetail,justify="center")
    e_yr.place(x=440,y=110)
    dsg = Label(sdetail,text='Designation', font=(13))  
    dsg.place(x=20, y=140)
    e_dsg =Entry(sdetail,justify="center")
    e_dsg.place(x=300,y=140)
    dep = Label(sdetail,text='Department', font=(13))  
    dep.place(x=20, y=170)
    e_dep =Entry(sdetail,justify="center")
    e_dep.place(x=300,y=170)
    add = Label(sdetail,text='Address', font=(13))  
    add.place(x=20, y=200)
    e_add =Entry(sdetail,justify="center")
    e_add.place(x=300,y=200)
    phn = Label(sdetail,text='Phone Number', font=(13))  
    phn.place(x=20, y=230)
    e_phn =Entry(sdetail,justify="center")
    e_phn.place(x=300,y=230)
    sal = Label(sdetail,text='Monthly Salary', font=('bold', 13))  
    sal.place(x=20, y=260)
    e_sal =Entry(sdetail,justify="center")
    e_sal.place(x=300,y=260)

    def Quit(window):
        sw(home)

    def clear():
        e_sid.delete(0, 'end')              
        e_name.delete(0, 'end')
        e_dat.delete(0, 'end')
        e_mon.delete(0, 'end')
        e_yr.delete(0, 'end')
        e_dsg.delete(0, 'end')
        e_dep.delete(0, 'end')
        e_add.delete(0, 'end')
        e_phn.delete(0, 'end')
        e_sal.delete(0, 'end')

    def insert():
        g_sid =e_sid.get()
        g_name =e_name.get()
        g_dob=e_yr.get()+'-'+e_mon.get()+'-'+e_dat.get()
        g_dsg =e_dsg.get()
        g_dep =e_dep.get()
        g_add =e_add.get()
        g_phn =e_phn.get()
        g_sal =e_sal.get()
    
        if(g_sid=="" or g_name=="" or g_dob=="" or  g_dsg=="" or g_dep=="" or g_add=="" or g_phn=="" or g_sal=="") :
            msgbox.showinfo("Insert Status", "All Fields are required")
        elif str(g_sid).isdigit()==False or str(g_sal).isdigit()==False or str(g_phn).isdigit()==False:
            msgbox.showinfo("Insert Status", "Invalid Entry")
        else:
            mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
            mycur =mycon.cursor()
            mycur.execute("Insert into staff values('"+ g_sid + "','"+ g_name +"','"+ g_dob +"','"+ g_dsg +"','"+ g_dep +"','"+ g_add +"','"+ g_phn +"','"+ g_sal +"') ")
            mycon.commit()
            clear()
            msgbox.showinfo("Insert Status","Inserted Successfully") #1st one is title of msg box 2nd is msg
            mycon.close()
    def delete():
        if e_sid.get()=="":
            msgbox.showinfo("Delete Status ","Staff ID is compulsory for deletion")
        else:
            mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
            mycur = mycon.cursor()
            mycur.execute("Delete from staff where SId='"+ e_sid.get() +"'")
            mycon.commit()
            clear()
            msgbox.showinfo("Delete Status","Deleted Successfully") 
            mycon.close()
    def update():
        g_sid =e_sid.get()
        g_name =e_name.get()
        g_dob=e_yr.get()+'-'+e_mon.get()+'-'+e_dat.get()
        g_dsg =e_dsg.get()
        g_dep =e_dep.get()
        g_add =e_add.get()
        g_phn =e_phn.get()
        g_sal =e_sal.get()
    
        if(g_sid=="" or g_name=="" or g_dob=="" or  g_dsg=="" or g_dep=="" or g_add=="" or g_phn=="" or g_sal=="") :
            msgbox.showinfo("Update Status", "All Fields are required")
        elif str(g_sid).isdigit()==False or str(g_sal).isdigit()==False or str(g_phn).isdigit()==False:
            msgbox.showinfo("Update Status", "Invalid Entry")
        else:
            mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
            mycur =mycon.cursor()
            mycur.execute("Update staff set Name='"+ g_name +"',DOB='"+ g_dob +"',Designation='"+ g_dsg +"',Department='"+ g_dep +"',Address='"+ g_add +"',Phone_Number='"+ g_phn +"',Monthly_Salary='"+ g_sal +"' where SId='"+ g_sid +"' ")
            mycon.commit()
            clear()   
            msgbox.showinfo("Update Status","Updated Successfully") 
            mycon.close()
    def display():
        if (e_sid.get() ==""):
            msgbox.showinfo("Fetch Status ","Id is compulsory for fetching")
        else:
            mycon =pymy.connect(host="localhost",user="root",passwd="tiger",database="hospital",charset="utf8")
            mycur = mycon.cursor()
            mycur.execute(" Select * from staff where SId='"+ e_sid.get() +"' ")
            rows= mycur.fetchall()
        
            for row in rows:
                e_name.insert(0, row[1])
                r=str(row[2])
                yr,mon,dat=r.split('-')
                e_dat.insert(0, dat)
                e_mon.insert(0, mon)
                e_yr.insert(0, yr)
                e_dsg.insert(0, row[3])
                e_dep.insert(0, row[4])
                e_add.insert(0, row[5])
                e_phn.insert(0, row[6])
                e_sal.insert(0, row[7])

            mycon.close()
    
    insert=Button(sdetail,text="INSERT",font=(13),command=insert)
    insert.place(x=20,y=360)
    delete=Button(sdetail,text="DELETE",font=(13),command=delete)
    delete.place(x=137,y=360)
    update=Button(sdetail,text="UPDATE",font=(13),command=update)
    update.place(x=258,y=360)
    display=Button(sdetail,text="DISPLAY",font=(13),command=display)
    display.place(x=382,y=360)
    Qt=Button(sdetail,text="QUIT",font=(13),command=lambda: Quit(root))
    Qt.place(x=514,y=360)
patient=Button(home,bg="royal blue",text="PATIENT",font=("italics",20),command=patient)
patient.place(x=248,y=40)

staff=Button(home,bg="firebrick1",text="STAFF",font=("italics",20),command=staff)
staff.place(x=259,y=120)

Qt=Button(home,bg="yellow2",text="QUIT",font=("italics",20),command=lambda: Quit(root))   
Qt.place(x=270,y=200)

root.mainloop()

