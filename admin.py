from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
'''from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *'''

mypass = "Kathyu@0508" #use your own password
mydatabase="inst" #The database name
con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor

admin = Tk()
admin.title("Admin")
admin.minsize(width=400,height=400)
admin.geometry("1000x800")

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
lb1 = Button(labelFrame,text="Manage Students", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.25, relwidth=0.4, relheight=0.2)

# Manage Books
def manage():
    admin=Tk()
    admin.title('Manage Books')
    admin.geometry('400x350')

    Canvas1 = Canvas(admin)
    Canvas1.config(bg='#7d7d7d')
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame = Frame(admin,bg="#FFBB00",bd=2)
    headingFrame.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.08)

    headingLabel = Label(headingFrame, text="Manage Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(admin,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.5)

    mb1=Button(labelFrame1,text="View Library",bg='black',fg='white')
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


lb2 = Button(labelFrame,text="Manage books", bg='black', fg='white',command=manage)
lb2.place(relx=0.55,rely=0.25, relwidth=0.4, relheight=0.2)


# Pending files
lb3 = Button(labelFrame,text="Pending Files", bg='black', fg='white')
lb3.place(relx=0.05,rely=0.65, relwidth=0.4, relheight=0.2)

# Query/Feedback
def view():
    booktable="emp_2019bcs0032"
    admin=Tk()
    admin.title('Query/Feedback')
    admin.geometry('500x480')

    Canvas1 = Canvas(admin)
    Canvas1.config(bg='#7d7d7d')
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame = Frame(admin,bg="#FFBB00",bd=2)
    headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.08)

    headingLabel = Label(headingFrame, text="Query/Feedback", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(admin,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.6)

    Label(labelFrame, text="%-10s%-30s%-40s%-20s"%('SID','S_Name','Messages',''),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            Label(labelFrame,text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")


lb4 = Button(labelFrame,text="Query/Feedback", bg='black', fg='white',command=view)
lb4.place(relx=0.55,rely=0.65, relwidth=0.4, relheight=0.2)

quitBtn = Button(admin,text="Quit",bg='#f7f1e3', fg='black', command=admin.destroy)
quitBtn.place(relx=0.12,rely=0.88, relwidth=0.18,relheight=0.08)


admin.mainloop()
