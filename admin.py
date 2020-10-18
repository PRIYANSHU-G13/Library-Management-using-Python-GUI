from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import mysql.connector
from tkinter import font as tkFont
from tkcalendar import Calendar, DateEntry #pip install tkcalendar
#from ad_student import *

def start_admin(user,password):
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@0035",#Replace XXXX with your MySQL password
        database="Library")
    cur = con.cursor()
            #'''Create this database(Library) and add the student table as:
             #  create table Students(Fullname varchar(30) NOT NULL,Username varchar(15) NOT NULL,
              # Email varchar(50) NOT NULL,Password varchar(20) NOT NULL,Contact int(10) NOT NULL,
               #Age int(3) NOT NULL,Batch int(4) NOT NULL,Course varchar(20) NOT NULL,PRIMARY KEY (Username));'''

            #'''add books table as:
             #  create table books(B_ID VARCHAR(10) NOT NULL, B_NAME VARCHAR(20) NOT NULL, AUTHOR VARCHAR(30) NOT NULL,
              # S_ID VARCHAR(10) NOT NULL, S_NAME VARCHAR(20) NOT NULL, C_NAME VARCHAR(20) NOT NULL,
               #PRIMARY KEY (B_ID));'''

    Regno=user

    #start
    #fetching data of user after login
    command="select Aname,Aid,Email from admin where Aid=%s and password=%s"
    var=[user, password]
    cur.execute(command,var)
    user_details=cur.fetchall()

    admin = Tk()
    admin.title(str("Hii, "+user_details[0][0])+"  |   Welcome to IIIT Kottayam Library")
    #admin.minsize(width=400,height=400)
    admin.geometry("1150x680+150+50")
    admin.resizable(False,False)
    #creating menubar
    menubar = Menu(admin)



    Canvas1 = Canvas(admin)
    Canvas1.config(bg="#B8DBE6")
    Canvas1.pack(expand=True,fill=BOTH)

    '''def SearchStudents():
        global search_entry
        search = str(search_entry.get())'''


    header_admin= Label(admin,text='ADMIN',bg='#525b59', fg='white')
    header_admin.place(relx=0.65,rely=0.09,relwidth=0.1,relheight=0.05)

    header_username=Button(admin,text=user_details[0][0],fg='black')
    header_username.place(relx=0.76,rely=0.09,relwidth=0.2,relheight=0.05)

    headingFrame1 = Frame(admin,bg="#FFBB00",bd=2)
    headingFrame1.place(relx=0,rely=0.0,relwidth=1,relheight=0.08)

    headingLabel = Label(headingFrame1, text="Welcome ADMIN", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    # search entry
    search_entry=Entry(admin)
    search_entry.insert(0,'Search Students/Books')
    search_entry.place(relx=0.04,rely=0.15, relwidth=0.57, relheight=0.06)

    # Search Students
    sr1 = Button(admin,text="Search Students",bg='#525b59', fg='white')#,command=SearchStudents)
    sr1.place(relx=0.63,rely=0.15, relwidth=0.155, relheight=0.06)

    # Search books
    sr2 = Button(admin,text="Search Books",bg='#525b59', fg='white')#,command=SearchBooks)
    sr2.place(relx=0.80,rely=0.15, relwidth=0.155, relheight=0.06)

    labelFrame = Frame(admin,bg="black")
    labelFrame.place(relx=0.04,rely=0.25,relwidth=0.92,relheight=0.71)

    # Adding student to the Database
    def adds():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        # Validating and add
        def add_stu():
            fname=str(fullname1.get())
            usern=str(username1.get())
            mail=str(email1.get())
            passwrd=str(password1.get())
            cont=str(contact1.get())
            dob=str(dob1.get())
            batch=str(batch1.get())
            course=str(course1.get())
            rest='no'
            if(res.get()==1):
                rest='yes'
            bir=dob.split('/')
            dob=''
            if len(bir[2])==4:
                dob=bir[2]+'-'+bir[1]+'-'+bir[0]
            else:
                dob='20'+bir[2]+'-'+bir[1]+'-'+bir[0]
            fine='0'
            if(fname=='' or usern=="" or mail=="" or cont==None or dob==None or batch=="" or course=="" or passwrd=="")!=False:
                messagebox.showinfo("Can't ADD","All feilds are required!")
            elif(mail.endswith('@iiitkottayam.ac.in'))!=True:
                messagebox.showinfo("Invalid Email","Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
            elif(cont.isnumeric() and len(cont)==10)!=True:
                messagebox.showinfo("Invalid Contact Number","Enter a valid Contact Number(Length 10)!")
            elif (batch.isnumeric())!=True:
                messagebox.showinfo("Invalid Batch","Batch should be number and in format '20XX' !")
            elif(usern.isalnum())!=True:
                messagebox.showinfo("Invalid Username","Username should be Alphanumeric!")
            else:
                try:
                    addformula="INSERT INTO Student (Sname, Regno, Password, Phone, Email, Batch, DOB, Fine, Course, is_restricted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    add_student=(fname,usern,passwrd,cont,mail,batch,dob,fine,course,rest)
                    cur.execute(addformula, add_student)
                    con.commit()
                    fullname1.delete(0,'end')
                    username1.delete(0,'end')
                    email1.delete(0,'end')
                    password1.delete(0,'end')
                    contact1.delete(0,'end')
                    dob1.delete(0,'end')
                    batch1.delete(0,'end')
                    course1.delete(0,'end')
                    messagebox.showinfo("Student Added","Student is added successfully!")
                except(mysql.connector.errors.IntegrityError):
                    messagebox.showinfo("Can't add Student","Oops!!\nUsername already exist!!")


        details=Label(labelFrame,text="Add Details:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        fullname=Label(labelFrame,text="Full name",bg='black',fg='white').place(relx=0.1,rely=0.18,relwidth=0.25,relheight=0.07)
        username=Label(labelFrame,text="Username",bg='black',fg='white').place(relx=0.1,rely=0.27,relwidth=0.25,relheight=0.07)
        email=Label(labelFrame,text="Email Id",bg='black',fg='white').place(relx=0.1,rely=0.36,relwidth=0.25,relheight=0.07)
        password=Label(labelFrame,text="Password",bg='black',fg='white').place(relx=0.1,rely=0.45,relwidth=0.25,relheight=0.07)
        contact=Label(labelFrame,text="Contact no.",bg='black',fg='white').place(relx=0.1,rely=0.54,relwidth=0.25,relheight=0.07)
        dob=Label(labelFrame,text="Date Of Birth",bg='black',fg='white').place(relx=0.1,rely=0.63,relwidth=0.25,relheight=0.07)
        batch=Label(labelFrame,text="Batch",bg='black',fg='white').place(relx=0.1,rely=0.72,relwidth=0.25,relheight=0.07)
        course=Label(labelFrame,text="Course",bg='black',fg='white').place(relx=0.1,rely=0.81,relwidth=0.25,relheight=0.07)
        restrict=Label(labelFrame,text="Is Restricted?",bg='black',fg='white').place(relx=0.1,rely=0.90,relwidth=0.25,relheight=0.07)

        res=IntVar()
        res.set(2)

        fullname1 = Entry(labelFrame)
        fullname1.place(relx=0.5,rely=0.18,relwidth=0.3,relheight=0.06)
        #print('fullname1',fullname1)
        username1 = Entry(labelFrame)
        username1.place(relx=0.5,rely=0.27,relwidth=0.3,relheight=0.06)
        email1 = Entry(labelFrame)
        email1.place(relx=0.5,rely=0.36,relwidth=0.3,relheight=0.06)
        password1 = Entry(labelFrame)
        password1.place(relx=0.5,rely=0.45,relwidth=0.3,relheight=0.06)
        contact1 = Entry(labelFrame)
        contact1.place(relx=0.5,rely=0.54,relwidth=0.3,relheight=0.06)
        dob1 = DateEntry(labelFrame, date_pattern='dd/mm/yyyy',state="readonly")
        dob1.place(relx=0.5,rely=0.63,relwidth=0.15,relheight=0.06)
        batch1 = Entry(labelFrame)
        batch1.place(relx=0.5,rely=0.72,relwidth=0.3,relheight=0.06)
        course1 = Entry(labelFrame)
        course1.place(relx=0.5,rely=0.81,relwidth=0.3,relheight=0.06)
        re1= Radiobutton(labelFrame, text="Yes")
        re1.place(relx=0.5,rely=0.90,relwidth=0.12,relheight=0.06)
        re1.config(variable=res, val=1)
        re2= Radiobutton(labelFrame, text="No")
        re2.place(relx=0.65,rely=0.90,relwidth=0.12,relheight=0.06)
        re2.config(variable=res, val=2)

        add=Button(labelFrame,text='Add',bg='#7d7d7d',fg='black',command=add_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


    # View all the students from the database
    def views():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        lboxs.place(relx=0.04, rely=0.04,relwidth=0.92,relheight=0.92)

        #print_his()
        '''def print_his():
            reg_no=str(reg.get())
            print(reg_no)'''

        #def show():
        lboxs.delete(0,'end')
        #start
        h = Scrollbar(lboxs, orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(lboxs)
        v.pack(side = RIGHT, fill = Y)
        t = Text(lboxs, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
        #end
        cur.execute("select Regno, Sname, Email, Phone, Batch, Course, Fine from student order by Regno")
        rows=list(cur.fetchall())

        reg=Label(lboxs,text='Reg.No.',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='w')
        t.window_create(END,window=reg)
        s_name=Label(lboxs,text='Name',bg='#97cee3',fg='white',width=15,font='BOLD', anchor='w')
        t.window_create(END,window=s_name)
        s_mail=Label(lboxs,text='Email',bg='#97cee3',fg='white',width=25,font='BOLD', anchor='c')
        t.window_create(END,window=s_mail)
        s_phone=Label(lboxs,text='Contact',bg='#97cee3',fg='white',width=10,font='BOLD', anchor='c')
        t.window_create(END,window=s_phone)
        s_batch=Label(lboxs,text='Batch',bg='#97cee3',fg='white',font='BOLD',width=10, anchor='c')
        t.window_create(END,window=s_batch)
        s_course=Label(lboxs,text='Course',bg='#97cee3',fg='white',width=9,font='BOLD', anchor='c')
        t.window_create(END,window=s_course)
        s_fine=Label(lboxs,text='Fine',bg='#97cee3',fg='white',width=11,font='BOLD', anchor='c')
        t.window_create(END,window=s_fine)
        s_history=Label(lboxs,text='History',bg='#97cee3',fg='white', font='BOLD',width=10 , anchor='c')
        t.window_create(END,window=s_history)
        t.insert(END,"\n")

        for row in rows:
            reg=Label(lboxs,text=row[0],bg='yellow',fg='black',width=13, anchor='w')
            t.window_create(END,window=reg)
            s_name=Label(lboxs,text=row[1],bg='yellow',fg='black',width=22, anchor='w')
            t.window_create(END,window=s_name)
            s_mail=Label(lboxs,text=row[2],bg='yellow',fg='black',width=30, anchor='w')
            t.window_create(END,window=s_mail)
            s_phone=Label(lboxs,text=row[3],bg='yellow',fg='black',width=13, anchor='c')
            t.window_create(END,window=s_phone)
            s_batch=Label(lboxs,text=row[4],bg='yellow',fg='black',width=12, anchor='c')
            t.window_create(END,window=s_batch)
            s_course=Label(lboxs,text=row[5],bg='yellow',fg='black',width=12, anchor='c')
            t.window_create(END,window=s_course)
            s_fine=Label(lboxs,text=row[6],bg='yellow',fg='black',width=12, anchor='c')
            t.window_create(END,window=s_fine)
            s_history=Button(lboxs,text='History',bg='grey',fg='black',command= None,width=14, anchor='c')
            t.window_create(END,window=s_history)
            t.insert(END,"\n")
                #insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                #lboxs.insert(lboxs.size()+1, insertdata)
                #t.insert(END,insertdata)
            #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
            #end

        #display = Button(labelFrame,text="CLICK TO VIEW",bg='#525b59', fg='white',command=show)
        #display.place(relx=0.35,rely=0.05,relwidth=0.3,relheight=0.1)

    # Deleting Student from the Database
    def deletes():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        # Verufy and delete
        def del_stu():
            delst=str(dusername.get())
            if(delst==''):
                messagebox.showinfo("Can't Delete","Enter Student's Registration Number!")
            cur.execute("DELETE FROM Student WHERE Regno='"+ delst +"'")
            con.commit()
            dusername.delete(0,'end')
            messagebox.showinfo("Student Deleted","Student is Deleted successfully!")

        details=Label(labelFrame,text="Enter Details:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        username=Label(labelFrame,text="Registration ID",bg='black',fg='white').place(relx=0.1,rely=0.28,relwidth=0.25,relheight=0.08)
        dusername = Entry(labelFrame)
        dusername.place(relx=0.5,rely=0.28,relwidth=0.3,relheight=0.08)
        delete=Button(labelFrame,text='Delete',bg='#7d7d7d',fg='black',command=del_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)

    # Update student details
    def updates():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        def up_stu():
            regi=str(st_reg.get())
            for widget in labelFrame.winfo_children():
                widget.destroy()

            cur.execute("select * from student where Regno='"+ regi +"'")
            rows=list(cur.fetchall())

            def update_stu():
                fname=str(fullname1.get())
                fine=str(fine1.get())
                mail=str(email1.get())
                passwrd=str(password1.get())
                cont=str(contact1.get())
                dob=str(dob1.get())
                batch=str(batch1.get())
                course=str(course1.get())
                rest='no'
                if(res.get()==1):
                    rest='yes'
                bir=dob.split('/')
                dob=''
                if len(bir[2])==4:
                    dob=bir[2]+'-'+bir[1]+'-'+bir[0]
                else:
                    dob='20'+bir[2]+'-'+bir[1]+'-'+bir[0]

                if(fname=='' or fine=="" or mail=="" or cont==None or dob==None or batch=="" or course=="" or passwrd=="")!=False:
                    messagebox.showinfo("Can't ADD","All feilds are required!")
                elif(mail.endswith('@iiitkottayam.ac.in'))!=True:
                    messagebox.showinfo("Invalid Email","Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
                elif(cont.isnumeric() and len(cont)==10)!=True:
                    messagebox.showinfo("Invalid Contact Number","Enter a valid Contact Number(Length 10)!")
                elif (batch.isnumeric())!=True:
                    messagebox.showinfo("Invalid Batch","Batch should be number and in format '20XX' !")
                else:
                    try:
                        #addformula="INSERT INTO Student (Sname, Regno, Password, Phone, Email, Batch, DOB, Fine, Stream_id, is_restricted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        #add_student=(fname,usern,passwrd,cont,mail,batch,dob,fine,course,rest)
                        #cur.execute(addformula, add_student)
                        cur.execute("UPDATE Student SET Sname='"+ fname +"',Password='"+ passwrd +"',Phone='"+ cont +"',Email='"+ mail +"',Batch='"+ batch +"',DOB='"+ dob +"',Fine='"+ fine +"',Course='"+ course +"',is_restricted='"+ rest +"' WHERE Regno='"+ regi +"'")
                        con.commit()
                        fullname1.delete(0,'end')
                        fine1.delete(0,'end')
                        email1.delete(0,'end')
                        password1.delete(0,'end')
                        contact1.delete(0,'end')
                        dob1.delete(0,'end')
                        batch1.delete(0,'end')
                        course1.delete(0,'end')
                        messagebox.showinfo("Student Updated","Student Details are updated successfully!")
                        updates()
                    except:
                        messagebox.showinfo("Can't Update Student","Oops!!\nSomething went wrong!!")


            details=Label(labelFrame,text="Enter Details to Update:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
            fullname=Label(labelFrame,text="Full name",bg='black',fg='white').place(relx=0.1,rely=0.18,relwidth=0.25,relheight=0.07)
            fine=Label(labelFrame,text="Fine",bg='black',fg='white').place(relx=0.1,rely=0.27,relwidth=0.25,relheight=0.07)
            email=Label(labelFrame,text="Email Id",bg='black',fg='white').place(relx=0.1,rely=0.36,relwidth=0.25,relheight=0.07)
            password=Label(labelFrame,text="Password",bg='black',fg='white').place(relx=0.1,rely=0.45,relwidth=0.25,relheight=0.07)
            contact=Label(labelFrame,text="Contact no.",bg='black',fg='white').place(relx=0.1,rely=0.54,relwidth=0.25,relheight=0.07)
            dob=Label(labelFrame,text="Date Of Birth",bg='black',fg='white').place(relx=0.1,rely=0.63,relwidth=0.25,relheight=0.07)
            batch=Label(labelFrame,text="Batch",bg='black',fg='white').place(relx=0.1,rely=0.72,relwidth=0.25,relheight=0.07)
            course=Label(labelFrame,text="Course",bg='black',fg='white').place(relx=0.1,rely=0.81,relwidth=0.25,relheight=0.07)
            restrict=Label(labelFrame,text="Is Restricted?",bg='black',fg='white').place(relx=0.1,rely=0.90,relwidth=0.25,relheight=0.07)

            res=IntVar()
            restricted=rows[0][9].lower()
            if restricted=='no':
                res.set(2)
            else:
                res.set(1)

            st_birth=str(rows[0][6])
            stu_bir=st_birth.split('-')
            st_birth=''
            st_birth=stu_bir[2]+'/'+stu_bir[1]+'/'+stu_bir[0]

            fullname1 = Entry(labelFrame)
            fullname1.insert(0,str(rows[0][0]))
            fullname1.place(relx=0.5,rely=0.18,relwidth=0.3,relheight=0.06)
            fine1 = Entry(labelFrame)
            fine1.insert(0,str(rows[0][7]))
            fine1.place(relx=0.5,rely=0.27,relwidth=0.3,relheight=0.06)
            email1 = Entry(labelFrame)
            email1.insert(0,str(rows[0][4]))
            email1.place(relx=0.5,rely=0.36,relwidth=0.3,relheight=0.06)
            password1 = Entry(labelFrame)
            password1.insert(0,str(rows[0][2]))
            password1.place(relx=0.5,rely=0.45,relwidth=0.3,relheight=0.06)
            contact1 = Entry(labelFrame)
            contact1.insert(0,str(rows[0][3]))
            contact1.place(relx=0.5,rely=0.54,relwidth=0.3,relheight=0.06)
            dob1 = DateEntry(labelFrame, date_pattern='dd/mm/yyyy')
            dob1.delete(0,'end')
            dob1.insert(0,st_birth)
            dob1.place(relx=0.5,rely=0.63,relwidth=0.15,relheight=0.06)
            batch1 = Entry(labelFrame)
            batch1.insert(0,str(rows[0][5]))
            batch1.place(relx=0.5,rely=0.72,relwidth=0.3,relheight=0.06)
            course1 = Entry(labelFrame)
            course1.insert(0,str(rows[0][8]))
            course1.place(relx=0.5,rely=0.81,relwidth=0.3,relheight=0.06)
            re1= Radiobutton(labelFrame, text="Yes")
            re1.place(relx=0.5,rely=0.90,relwidth=0.12,relheight=0.06)
            re1.config(variable=res, val=1)
            re2= Radiobutton(labelFrame, text="No")
            re2.place(relx=0.65,rely=0.90,relwidth=0.12,relheight=0.06)
            re2.config(variable=res, val=2)

            update=Button(labelFrame,text='Update',bg='#7d7d7d',fg='black',command=update_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


        details=Label(labelFrame,text="Update Student Details:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        user=Label(labelFrame,text="Registration Number",bg='black',fg='white').place(relx=0.1,rely=0.28,relwidth=0.25,relheight=0.08)
        st_reg = Entry(labelFrame)
        st_reg.place(relx=0.5,rely=0.28,relwidth=0.3,relheight=0.08)
        delete=Button(labelFrame,text='Proceed',bg='#7d7d7d',fg='black',command=up_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


    #restrict student
    def restricts():
        for widget in labelFrame.winfo_children():
             widget.destroy()


        def rest_stu():
            st_res=str(st_rest.get())
            y='Yes'
            cur.execute("UPDATE Student SET is_restricted='"+ 'Yes' +"' WHERE Regno='"+ st_res +"'")
            con.commit()
            st_rest.delete(0,'end')
            messagebox.showinfo("Student Restricted","Student is Restricted successfully!")

        details=Label(labelFrame,text="Restrict Student:",bg='white',fg='black',font='BOLD').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
        st_res=Label(labelFrame,text="Registration Number",bg='black',fg='white').place(relx=0.1,rely=0.28,relwidth=0.25,relheight=0.08)
        st_rest = Entry(labelFrame)
        st_rest.place(relx=0.5,rely=0.28,relwidth=0.3,relheight=0.08)
        delete=Button(labelFrame,text='Restrict',bg='#7d7d7d',fg='black',command=rest_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)



    # Manage Students

    lb1 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Manage Students',menu=lb1)
    lb1.add_command(label='Add Student',command=adds)
    lb1.add_command(label='Update Details',command=updates)
    lb1.add_command(label='View Students',command=views)
    lb1.add_separator()
    lb1.add_command(label='Delete Student',command=deletes)
    lb1.add_command(label='Restrict Student',command=restricts)




    #FUNCTION TO VIEW LIBRARY

    def view():
        for widget in labelFrame.winfo_children():
            widget.destroy()
        ls = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        ls.place(relx=0.04, rely=0.3,relwidth=0.92,relheight=0.65)

        b_id = Label(labelFrame,text="BOOK_ID",bg="white",fg="black")
        b_id.place(relx=0.04,rely=0.2,relwidth=0.08,relheight=0.06)

        b_name = Label(labelFrame,text="BOOK_NAME",bg="white",fg="black")
        b_name.place(relx=0.16,rely=0.2,relwidth=0.11,relheight=0.06)

        author= Label(labelFrame,text="AUTHOR",bg="white",fg="black")
        author.place(relx=0.32,rely=0.2,relwidth=0.11,relheight=0.06)

        s_id = Label(labelFrame,text="STREAM_ID",bg="white",fg="black")
        s_id.place(relx=0.48,rely=0.2,relwidth=0.11,relheight=0.06)

        s_name = Label(labelFrame,text="STREAM_NAME",bg="white",fg="black")
        s_name.place(relx=0.63,rely=0.2,relwidth=0.13,relheight=0.06)

        c_name = Label(labelFrame,text="CATEGORY_NAME",bg="white",fg="black")
        c_name.place(relx=0.80,rely=0.2,relwidth=0.14,relheight=0.06)

        def show():
            '''ls.delete(0,'end')

            cur.execute("select * from books")
            rows=cur.fetchall()

            for row in rows:
                insertdata = "%-10s%-15s%-15s%-10s%-12.5s%-12.5s"%(row[0],row[1],row[2],row[3],row[4],row[5])
                ls.insert(ls.size()+1, insertdata)'''
            ls.delete(0,'end')
            #start
            h = Scrollbar(ls, orient = 'horizontal')
            h.pack(side = BOTTOM, fill = X)
            v = Scrollbar(ls)
            v.pack(side = RIGHT, fill = Y)
            t = Text(ls, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
            #end

            cur.execute("select * from book")
            rows=cur.fetchall()

            for row in rows:
                insertdata = "%-10s%-15s%-15s%-10s%-12.5s%-12.5s"%(row[0],row[1],row[2],row[3],row[4],row[5])
                #ls.insert(ls.size()+1, insertdata)
                t.insert(END,insertdata)

            #start
            t.configure(state="disabled")
            t.pack(side=TOP, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)
            #end

        display = Button(labelFrame,text="CLICK TO VIEW",bg='#525b59', fg='white',command=show)
        display.place(relx=0.35,rely=0.05,relwidth=0.3,relheight=0.1)


    #FUNCTION FOR ADDING BOOKs

    def add_new():
        for widget in labelFrame.winfo_children():
            widget.destroy()
        B_ID = Label(labelFrame,text="BOOK_ID",fg="black",bg="white")
        B_ID.place(relx=0.02,rely=0.12,relwidth=0.3,relheight=0.08)

        B_NAME = Label(labelFrame,text="BOOK_NAME",fg="black",bg="white")
        B_NAME.place(relx=0.02,rely=0.22,relwidth=0.3,relheight=0.08)

        AUTHOR = Label(labelFrame,text="AUTHOR",fg="black",bg="white")
        AUTHOR.place(relx=0.02,rely=0.32,relwidth=0.3,relheight=0.08)

        S_ID = Label(labelFrame,text="STREAM_ID",fg="black",bg="white")
        S_ID.place(relx=0.02,rely=0.42,relwidth=0.3,relheight=0.08)

        S_NAME = Label(labelFrame,text="STREAM_NAME",fg="black",bg="white")
        S_NAME.place(relx=0.02,rely=0.52,relwidth=0.3,relheight=0.08)

        C_NAME = Label(labelFrame,text="CATEGORY",fg="black",bg="white")
        C_NAME.place(relx=0.02,rely=0.62,relwidth=0.3,relheight=0.08)

        e_b_id = Entry(labelFrame)
        e_b_id.place(relx=0.42,rely=0.12,relwidth=0.3,relheight=0.08)

        e_b_name = Entry(labelFrame)
        e_b_name.place(relx=0.42,rely=0.22,relwidth=0.3,relheight=0.08)

        e_author = Entry(labelFrame)
        e_author.place(relx=0.42,rely=0.32,relwidth=0.3,relheight=0.08)

        e_s_id = Entry(labelFrame)
        e_s_id.place(relx=0.42,rely=0.42,relwidth=0.3,relheight=0.08)

        e_s_name = Entry(labelFrame)
        e_s_name.place(relx=0.42,rely=0.52,relwidth=0.3,relheight=0.08)

        e_c_name = Entry(labelFrame)
        e_c_name.place(relx=0.42,rely=0.62,relwidth=0.3,relheight=0.08)


        def add():
            B_ID = e_b_id.get()
            B_NAME = e_b_name.get()
            AUTHOR = e_author.get()
            S_ID = e_s_id.get()
            S_NAME = e_s_name.get()
            C_NAME = e_c_name.get()

            if(B_ID=="" or B_NAME=="" or AUTHOR=="" or S_ID=="" or S_NAME=="" or C_NAME==""):
                messagebox.showinfo("Insert Status", "All fields are required!")
            else:
                cur.execute("insert into book values('"+ B_ID +"','"+ B_NAME +"','"+ AUTHOR +"','"+ S_ID +"','"+ S_NAME +"','"+ C_NAME +"')")
                cur.execute("commit")

                e_b_id.delete(0, 'end')
                e_b_name.delete(0, 'end')
                e_author.delete(0, 'end')
                e_s_id.delete(0, 'end')
                e_s_name.delete(0, 'end')
                e_c_name.delete(0, 'end')

                messagebox.showinfo("Insert Status","Successfully inserted into database")

        ADD = Button(labelFrame,text="ADD BOOK",fg="black",bg="#7d7d7d",command=add)
        ADD.place(relx=0.62,rely=0.85,relwidth=0.2,relheight=0.08)

    #FUNCTION FOR DELETING BOOK

    def delete():
        for widget in labelFrame.winfo_children():
            widget.destroy()
        B_ID = Label(labelFrame,text="BOOK_ID",fg="black",bg="white")
        B_ID.place(relx=0.02,rely=0.12,relwidth=0.3,relheight=0.08)

        B_NAME = Label(labelFrame,text="BOOK_NAME",fg="black",bg="white")
        B_NAME.place(relx=0.02,rely=0.22,relwidth=0.3,relheight=0.08)

        e_b_id = Entry(labelFrame)
        e_b_id.place(relx=0.42,rely=0.12,relwidth=0.3,relheight=0.08)

        e_b_name = Entry(labelFrame)
        e_b_name.place(relx=0.42,rely=0.22,relwidth=0.3,relheight=0.08)

        def remove():
            B_ID = e_b_id.get()
            B_NAME = e_b_name.get()

            if(B_ID=="" or B_NAME==""):
                messagebox.showinfo("Insert Status", "All fields are required!")

            else:
                cur.execute("delete from book where B_ID='"+ e_b_id.get() +"'")
                cur.execute("commit")

            e_b_id.delete(0, 'end')
            e_b_name.delete(0, 'end')

            messagebox.showinfo("Delete Status","Successfully deleted from database")

        DELETE = Button(labelFrame,text="DELETE BOOK",fg="black",bg="#7d7d7d",command=remove)
        DELETE.place(relx=0.62,rely=0.85,relwidth=0.2,relheight=0.08)

    # Manage Books

    lb2 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Manage Books',menu=lb2)
    lb2.add_command(label='View Library',command=view)
    lb2.add_command(label='Issued Books',command=None)
    lb2.add_separator()
    lb2.add_command(label='Add Books',command=add_new)
    #lb2.add_command(label='Add Book Details',command=None)
    lb2.add_command(label='Delete Book',command=delete)


    # Pending files
    def view_pf():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        view=Button(labelFrame,text='View',bg='#7d7d7d',fg='black').place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)

    def requests():
        for widget in labelFrame.winfo_children():
            widget.destroy()
        ls = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
        ls.place(relx=0.04, rely=0.3,relwidth=0.92,relheight=0.65)

        numOfRequest = 20

        #start
        h = Scrollbar(ls, orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(ls)
        v.pack(side = RIGHT, fill = Y)
        t = Text(ls, width = 30, height = 30, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set)
        #end
        for i in range(numOfRequest):
            regnoFont = tkFont.Font(family='product sans', size=13)
            regno = Label(ls,text='reg no : ', bg="pink",width=15, borderwidth=0,font=regnoFont, anchor='w')
            t.window_create(END,window=regno)
            nameFont = tkFont.Font(family='product sans', size=13)
            name = Label(ls,text='Student Name : ', bg="pink",width=20, borderwidth=0,font=nameFont, anchor='w')
            t.window_create(END,window=name)

            bookidFont = tkFont.Font(family='product sans', size=13)
            bookid = Label(ls, text='book id ', bg="pink", width=10, borderwidth=0, font=bookidFont, anchor='c')
            t.window_create(END,window=bookid)

            subidFont = tkFont.Font(family='product sans', size=13)
            subid = Label(ls, text='sub book id', bg="pink", fg='black',width=13, borderwidth=0, font=subidFont, anchor='c')
            t.window_create(END,window=subid)
            borrowdateFont = tkFont.Font(family='product sans', size=13)
            borrowdate = Label(ls, text='borrow date', bg="pink", fg='black',width=13, borderwidth=0, font=borrowdateFont, anchor='c')
            t.window_create(END,window=borrowdate)
            borrowidFont = tkFont.Font(family='product sans', size=13)
            borrowid = Label(ls, text='borrowid', bg="pink", fg='black',width=13, borderwidth=0, font=borrowidFont, anchor='c')
            t.window_create(END,window=borrowid)

            buttonsFont = tkFont.Font(family='product sans', size=12)
            receivebook = Button(ls, text="receive book", font=buttonsFont, bg="white", activebackground="#7d7d7d", anchor='c', width=16,cursor='hand2')
            t.window_create(END,window=receivebook)
            t.insert(END,"\n")
        #start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        #end

    #pending files
    lb3 = Menu(menubar,tearoff=0,bg='black', fg='white')
    menubar.add_cascade(label='Pending Files',menu=lb3)
    lb3.add_command(label='Pending Requests',command=requests)
    lb3.add_command(label='Pending Books',command=view_pf)



    # Query/Feedback

    lb4 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Qwery/Feedback',menu=lb4)
    lb4.add_command(label='Feedback',command=None)
    lb4.add_command(label='Query',command=None)


    #quitBtn = Button(admin,text="Quit",bg='#f7f1e3', fg='black', command=admin.destroy)
    #quitBtn.place(relx=0.05,rely=0.92, relwidth=0.18,relheight=0.05)

    admin.config(menu=menubar)
    admin.mainloop()

if __name__ == "__main__":
    start_admin('admin_user','admin_password') #change admin_user and admin_passowrd by adding a new admin in admin table.Or use the one which already exists in the table.
