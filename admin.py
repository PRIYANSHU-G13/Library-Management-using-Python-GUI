from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import webbrowser

mypass = "XXXX" #use your own password
mydatabase="library" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

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

labelFrame = Frame(admin,bg='black')
labelFrame.place(relx=0.04,rely=0.25,relwidth=0.92,relheight=0.6)


# Manage Students

lb1 = Menu(menubar,tearoff=0,bg='black', fg='white')
menubar.add_cascade(label='Manage Students',menu=lb1)
lb1.add_command(label='Add Student',command=None)
lb1.add_command(label='View Students',command=None)


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
