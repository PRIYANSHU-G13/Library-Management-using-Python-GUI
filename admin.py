from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import webbrowser
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@0035",
    database="Library"
)

db = mydb.cursor()

admin = Tk()
admin.title("Admin")
admin.minsize(width=400,height=400)
admin.geometry("1000x800")
#creating menubar
menubar = Menu(admin)



Canvas1 = Canvas(admin)
Canvas1.config(bg="pink")
Canvas1.pack(expand=True,fill=BOTH)

'''def SearchStudents():
    global search_entry
    search = str(search_entry.get())'''

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
        con=str(contact1.get())
        age=str(age1.get())
        batch=str(batch1.get())
        course=str(course1.get())
        if(fname=='' or usern=="" or mail=="" or con==None or age==None or batch=="" or course=="" or passwrd==""):
            messagebox.showinfo("Can't ADD","All feilds are required!")
        if(mail.endswith('@iiitkottayam.ac.in')):
            pass
        else:
            messagebox.showinfo("Invalid Email","Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
        if(con.isnumeric() and len(con)==10):
            pass
        else:
            messagebox.showinfo("Invalid Contact Number","Enter a valid Contact Number(Length 10)!")
        if(age.isnumeric()):
            pass
        else:
            messagebox.showinfo("Invalid Age","Age should be Number!")
        if(batch.isnumeric()):
            pass
        else:
            messagebox.showinfo("Invalid Batch","Batch should be number and in format '20XX' !")
        if(usern.isalnum()):
            pass
        else:
            messagebox.showinfo("Invalid Username","Username should be Alphanumeric!")

        db=mydb.cursor()
        addformula="INSERT INTO students (Fullname, Username, Email, Password, Contact, Age, Batch, Course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        add_student=(fname,usern,mail,passwrd,int(con),int(age),int(batch),course)
        db.execute(addformula, add_student)
        mydb.commit()
        messagebox.showinfo("Student Added","Student is added successfully!")



    details=Label(labelFrame,text="Add Details:",bg='white',fg='black').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
    fullname=Label(labelFrame,text="Full name",bg='black',fg='white').place(relx=0.1,rely=0.18,relwidth=0.25,relheight=0.08)
    username=Label(labelFrame,text="Username",bg='black',fg='white').place(relx=0.1,rely=0.28,relwidth=0.25,relheight=0.08)
    email=Label(labelFrame,text="Email Id",bg='black',fg='white').place(relx=0.1,rely=0.38,relwidth=0.25,relheight=0.08)
    password=Label(labelFrame,text="Password",bg='black',fg='white').place(relx=0.1,rely=0.48,relwidth=0.25,relheight=0.08)
    contact=Label(labelFrame,text="Contact no.",bg='black',fg='white').place(relx=0.1,rely=0.58,relwidth=0.25,relheight=0.08)
    age=Label(labelFrame,text="Age",bg='black',fg='white').place(relx=0.1,rely=0.68,relwidth=0.25,relheight=0.08)
    batch=Label(labelFrame,text="Batch",bg='black',fg='white').place(relx=0.1,rely=0.78,relwidth=0.25,relheight=0.08)
    course=Label(labelFrame,text="Course",bg='black',fg='white').place(relx=0.1,rely=0.88,relwidth=0.25,relheight=0.08)

    fullname1 = Entry(labelFrame)
    fullname1.place(relx=0.5,rely=0.18,relwidth=0.3,relheight=0.08)
    #print('fullname1',fullname1)
    username1 = Entry(labelFrame)
    username1.place(relx=0.5,rely=0.28,relwidth=0.3,relheight=0.08)
    email1 = Entry(labelFrame)
    email1.place(relx=0.5,rely=0.38,relwidth=0.3,relheight=0.08)
    password1 = Entry(labelFrame)
    password1.place(relx=0.5,rely=0.48,relwidth=0.3,relheight=0.08)
    contact1 = Entry(labelFrame)
    contact1.place(relx=0.5,rely=0.58,relwidth=0.3,relheight=0.08)
    age1 = Entry(labelFrame)
    age1.place(relx=0.5,rely=0.68,relwidth=0.3,relheight=0.08)
    batch1 = Entry(labelFrame)
    batch1.place(relx=0.5,rely=0.78,relwidth=0.3,relheight=0.08)
    course1 = Entry(labelFrame)
    course1.place(relx=0.5,rely=0.88,relwidth=0.3,relheight=0.08)

    add=Button(labelFrame,text='Add',bg='#7d7d7d',fg='black',command=add_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


# View all the students from the database
def views():
    for widget in labelFrame.winfo_children():
        widget.destroy()

    view=Button(labelFrame,text='View',bg='#7d7d7d',fg='black').place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)


# Deleting Student from the Database
def deletes():
    for widget in labelFrame.winfo_children():
        widget.destroy()

    # Verufy and delete
    def del_stu():
        delst=str(dusername.get())
        dfname=str(dfullname.get())
        dmail=str(demail.get())
        if(delst=='' or dfname=='' or dmail==''):
            messagebox.showinfo("Can't Delete","All feilds are required!")
        db=mydb.cursor()
        db.execute("DELETE FROM Students WHERE Username='"+ delst +"'")
        mydb.commit()
        messagebox.showinfo("Student Deleted","Student is Deleted successfully!")
        

    details=Label(labelFrame,text="Enter Details:",bg='white',fg='black').place(relx=0.08,rely=0.06,relwidth=0.3,relheight=0.1)
    username=Label(labelFrame,text="Username",bg='black',fg='white').place(relx=0.1,rely=0.28,relwidth=0.25,relheight=0.08)
    fullname=Label(labelFrame,text="Full name",bg='black',fg='white').place(relx=0.1,rely=0.38,relwidth=0.25,relheight=0.08)
    email=Label(labelFrame,text="Email Id",bg='black',fg='white').place(relx=0.1,rely=0.48,relwidth=0.25,relheight=0.08)
    dfullname = Entry(labelFrame)
    dfullname.place(relx=0.5,rely=0.38,relwidth=0.3,relheight=0.08)
    dusername = Entry(labelFrame)
    dusername.place(relx=0.5,rely=0.28,relwidth=0.3,relheight=0.08)
    demail = Entry(labelFrame)
    demail.place(relx=0.5,rely=0.48,relwidth=0.3,relheight=0.08)
    delete=Button(labelFrame,text='Delete',bg='#7d7d7d',fg='black',command=del_stu).place(relx=0.7,rely=0.06,relwidth=0.25,relheight=0.1)



header_admin= Label(admin,text='ADMIN',fg='black',bg='#7d7d7d')
header_admin.place(relx=0.65,rely=0.09,relwidth=0.1,relheight=0.05)

header_username=Button(admin,text='USERNAME',fg='black')
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
sr1 = Button(admin,text="Search Students",bg='#7d7d7d',fg='black')#,command=SearchStudents)
sr1.place(relx=0.63,rely=0.15, relwidth=0.155, relheight=0.06)

# Search books
sr2 = Button(admin,text="Search Books",bg='#7d7d7d',fg='black')#,command=SearchBooks)
sr2.place(relx=0.80,rely=0.15, relwidth=0.155, relheight=0.06)

labelFrame = Frame(admin,bg='black')
labelFrame.place(relx=0.04,rely=0.25,relwidth=0.92,relheight=0.6)

# Manage Students

lb1 = Menu(menubar,tearoff=0,bg='black', fg='white')
menubar.add_cascade(label='Manage Students',menu=lb1)
lb1.add_command(label='Add Student',command=adds)
lb1.add_command(label='View Students',command=views)
lb1.add_separator()
lb1.add_command(label='Delete Student',command=deletes)
lb1.add_command(label='Restrict Student',command=None)




# Manage Books

lb2 = Menu(menubar,tearoff=0,bg='black', fg='white')
menubar.add_cascade(label='Manage Books',menu=lb2)
lb2.add_command(label='View Library',command=None)
lb2.add_command(label='Issued Books',command=None)
lb2.add_separator()
lb2.add_command(label='Add Existing Book',command=None)
lb2.add_command(label='Add New Book',command=None)
lb2.add_command(label='Add Book Details',command=None)
lb2.add_command(label='Delete Book',command=None)


# Pending files
lb3 = Menu(menubar,tearoff=0,bg='black', fg='white')
menubar.add_cascade(label='Pending Files',menu=lb3)
lb3.add_command(label='Pending Requests',command=None)
lb3.add_command(label='Pending Books',command=None)


# Query/Feedback

lb4 = Menu(menubar,tearoff=0,bg='black', fg='white')
menubar.add_cascade(label='Qwery/Feedback',menu=lb4)
lb4.add_command(label='Feedback',command=None)
lb4.add_command(label='Query',command=None)


quitBtn = Button(admin,text="Quit",bg='#f7f1e3', fg='black', command=admin.destroy)
quitBtn.place(relx=0.12,rely=0.9, relwidth=0.18,relheight=0.06)

admin.config(menu=menubar)
admin.mainloop()
