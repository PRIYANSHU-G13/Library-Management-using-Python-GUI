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

header_admin= Label(admin,text='ADMIN',fg='black',bg='#7d7d7d')
header_admin.place(relx=0.65,rely=0.02,relwidth=0.1,relheight=0.05)

header_username=Button(admin,text='USERNSME',fg='black')
header_username.place(relx=0.76,rely=0.02,relwidth=0.2,relheight=0.05)

headingFrame1 = Frame(admin,bg="#FFBB00",bd=2)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.08)

headingLabel = Label(headingFrame1, text="Welcome ADMIN", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Search Students
sr1 = Button(admin,text="Search Students",bg='#7d7d7d',fg='black')
sr1.place(relx=0.11,rely=0.3, relwidth=0.35, relheight=0.08)

# Search books
sr2 = Button(admin,text="Search Books",bg='#7d7d7d',fg='black')
sr2.place(relx=0.53,rely=0.3, relwidth=0.35, relheight=0.08)

labelFrame = Frame(admin,bg='black')
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

# Manage Students
def manage_students():
    admin.destroy()
    win1=Tk()
    win1.title('Manage Students')
    win1.geometry('400x350')

    Canvas1 = Canvas(win1)
    Canvas1.config(bg='#7d7d7d')
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame = Frame(win1,bg="#FFBB00",bd=2)
    headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.08)

    headingLabel = Label(headingFrame, text="Manage Students", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(win1,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.5)

    ms1=Button(labelFrame,text="View students",bg='black',fg='white')
    ms1.place(relx=0.1,rely=0.1,relwidth=0.35,relheight=0.15)

    ms2=Button(labelFrame,text="Add Books",bg='black',fg='white')
    ms2.place(relx=0.55,rely=0.1,relwidth=0.35,relheight=0.15)
    quitBtn = Button(win1,text="Quit",bg='#f7f1e3', fg='black', command=win1.destroy)
    quitBtn.place(relx=0.12,rely=0.9, relwidth=0.88,relheight=0.08)
    
lb1 = Button(labelFrame,text="Manage Students", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.25, relwidth=0.4, relheight=0.2)

# Manage Books
def manage():
    admin.destroy()
    root=Tk()
    root.title('Manage Books')
    root.geometry('600x450')

    Canvas1 = Canvas(root)
    Canvas1.config(bg='#7d7d7d')
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame = Frame(root,bg="#FFBB00",bd=2)
    headingFrame.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.08)

    headingLabel = Label(headingFrame, text="Manage Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)

    mb1=Button(labelFrame,text="View Library",bg='black',fg='white')
    mb1.place(relx=0.1,rely=0.1,relwidth=0.35,relheight=0.15)

    mb2=Button(labelFrame,text="Issued Books",bg='black',fg='white')
    mb2.place(relx=0.55,rely=0.1,relwidth=0.35,relheight=0.15)

    mb3=Button(labelFrame,text="Add Existing Book",bg='black',fg='white')
    mb3.place(relx=0.1,rely=0.35,relwidth=0.35,relheight=0.15)

    mb4=Button(labelFrame,text="Add New Book",bg='black',fg='white')
    mb4.place(relx=0.55,rely=0.35,relwidth=0.35,relheight=0.15)

    mb5=Button(labelFrame,text="Add Book-Details",bg='black',fg='white')
    mb5.place(relx=0.1,rely=0.6,relwidth=0.35,relheight=0.15)

    mb6=Button(labelFrame,text='Delete Book',bg='black',fg='white')
    mb6.place(relx=0.55,rely=0.6,relwidth=0.35,relheight=0.15)

    back=Button(root,text="Go to start_page",bg='#f7f1e3',fg="black")
    back.place(relx=0.55,rely=0.85,relwidth=0.25,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.2,rely=0.85, relwidth=0.18,relheight=0.08)



lb2 = Button(labelFrame,text="Manage books", bg='black', fg='white',command=manage)
lb2.place(relx=0.55,rely=0.25, relwidth=0.4, relheight=0.2)


# Pending files
lb3 = Button(labelFrame,text="Pending Files", bg='black', fg='white')
lb3.place(relx=0.05,rely=0.65, relwidth=0.4, relheight=0.2)

# Query/Feedback
def view():
    admin.destroy()
    booktable="emp_2019bcs0032"
    root1=Tk()
    root1.title('Query/Feedback')
    root1.geometry('500x480')

    Canvas1 = Canvas(root1)
    Canvas1.config(bg='#7d7d7d')
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame = Frame(root1,bg="#FFBB00",bd=2)
    headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.08)

    headingLabel = Label(headingFrame, text="Query/Feedback", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.6)

    back=Button(root1,text="Go to start_page",bg='#f7f1e3',fg="black")
    back.place(relx=0.55,rely=0.9,relwidth=0.25,relheight=0.08)

    quitBtn = Button(root1,text="Quit",bg='#f7f1e3', fg='black', command=root1.destroy)
    quitBtn.place(relx=0.2,rely=0.9, relwidth=0.18,relheight=0.08)

lb4 = Button(labelFrame,text="Query/Feedback", bg='black', fg='white',command=view)
lb4.place(relx=0.55,rely=0.65, relwidth=0.4, relheight=0.2)

quitBtn = Button(admin,text="Quit",bg='#f7f1e3', fg='black', command=admin.destroy)
quitBtn.place(relx=0.12,rely=0.88, relwidth=0.18,relheight=0.08)

admin.mainloop()
