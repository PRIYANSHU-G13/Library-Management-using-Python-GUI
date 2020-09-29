from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="XXXX",#Replace XXXX with your MySQL password
    database="Library")
        '''Create this database(Library) and add the student table as:
           create table Students(Fullname varchar(30) NOT NULL,Username varchar(15) NOT NULL,
           Email varchar(50) NOT NULL,Password varchar(20) NOT NULL,Contact int(10) NOT NULL,
           Age int(3) NOT NULL,Batch int(4) NOT NULL,Course varchar(20) NOT NULL,PRIMARY KEY (Username));'''

        '''books table as:
           create table books(B_ID VARCHAR(10) NOT NULL, B_NAME VARCHAR(20) NOT NULL, AUTHOR VARCHAR(30) NOT NULL,
           S_ID VARCHAR(10) NOT NULL, S_NAME VARCHAR(20) NOT NULL, C_NAME VARCHAR(20) NOT NULL,
           PRIMARY KEY (B_ID));'''

cur = mydb.cursor()

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

labelFrame = Frame(admin,bg="black")
labelFrame.place(relx=0.04,rely=0.25,relwidth=0.92,relheight=0.6)



# Manage Students

lb1 = Menu(menubar,tearoff=0,bg='black', fg='white')
menubar.add_cascade(label='Manage Students',menu=lb1)
lb1.add_command(label='Add Student',command=None)
lb1.add_command(label='View Students',command=None)




#FUNCTION TO VIEW LIBRARY

def view():
    for widget in labelFrame.winfo_children():
        widget.destroy()
    ls = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
    ls.place(relx=0.04, rely=0.3,relwidth=0.92,relheight=0.65)

    b_id = Label(labelFrame,text="BOOK_ID",bg="white",fg="black")
    b_id.place(relx=0.04,rely=0.2,relwidth=0.08,relheight=0.06)

    b_name = Label(labelFrame,text="BOOK_NAME",bg="white",fg="black")
    b_name.place(relx=0.16,rely=0.2,relwidth=0.1,relheight=0.06)

    author= Label(labelFrame,text="AUTHOR",bg="white",fg="black")
    author.place(relx=0.35,rely=0.2,relwidth=0.1,relheight=0.06)

    s_id = Label(labelFrame,text="STREAM_ID",bg="white",fg="black")
    s_id.place(relx=0.518,rely=0.2,relwidth=0.1,relheight=0.06)

    s_name = Label(labelFrame,text="STREAM_NAME",bg="white",fg="black")
    s_name.place(relx=0.68,rely=0.2,relwidth=0.1,relheight=0.06)

    c_name = Label(labelFrame,text="CATEGORY_NAME",bg="white",fg="black")
    c_name.place(relx=0.82,rely=0.2,relwidth=0.14,relheight=0.06)

    def show():
        cur.execute("select * from books")
        rows=cur.fetchall()

        for row in rows:
            insertdata = "%-10s%-15s%-15s%-10s%-12.5s%-12.5s"%(row[0],row[1],row[2],row[3],row[4],row[5])
            ls.insert(ls.size()+1, insertdata)

    display = Button(labelFrame,text="CLICK TO VIEW",bg="pink",fg="black",command=show)
    display.place(relx=0.35,rely=0.05,relwidth=0.3,relheight=0.1)


#FUNCTION FOR ADDING EXISTING BOOK

def add_existing():
    print()

#FUNCTION FOR ADDING NEW BOOK

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
            cur.execute("insert into books values('"+ B_ID +"','"+ B_NAME +"','"+ AUTHOR +"','"+ S_ID +"','"+ S_NAME +"','"+ C_NAME +"')")
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
            cur.execute("delete from books where B_ID='"+ e_b_id.get() +"'")
            cur.execute("commit")

        e_b_id.delete(0, 'end')
        e_b_name.delete(0, 'end')

        messagebox.showinfo("Delete Status","Successfully deleted from database")

    DELETE = Button(labelFrame,text="DELETE BOOK",fg="black",bg="#7d7d7d",command=remove)
    DELETE.place(relx=0.62,rely=0.85,relwidth=0.2,relheight=0.08)

# Manage Books

lb2 = Menu(menubar,tearoff=0,bg='black', fg='white')
menubar.add_cascade(label='Manage Books',menu=lb2)
lb2.add_command(label='View Library',command=view)
lb2.add_command(label='Issued Books',command=None)
lb2.add_separator()
lb2.add_command(label='Add Existing Book',command=add_existing)
lb2.add_command(label='Add New Book',command=add_new)
lb2.add_command(label='Add Book Details',command=None)
lb2.add_command(label='Delete Book',command=delete)


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
