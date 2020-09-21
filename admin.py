from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox



admin = Tk()
admin.title("Admin")
admin.minsize(width=400,height=400)
admin.geometry("800x600")



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
lb2 = Button(labelFrame,text="Manage books", bg='black', fg='white')
lb2.place(relx=0.55,rely=0.25, relwidth=0.4, relheight=0.2)

# Pending files
lb3 = Button(labelFrame,text="Pending Files", bg='black', fg='white')
lb3.place(relx=0.05,rely=0.65, relwidth=0.4, relheight=0.2)

# Query/Feedback
lb4 = Button(labelFrame,text="Query/Feedback", bg='black', fg='white')
lb4.place(relx=0.55,rely=0.65, relwidth=0.4, relheight=0.2)

quitBtn = Button(admin,text="Quit",bg='#f7f1e3', fg='black', command=admin.destroy)
quitBtn.place(relx=0.12,rely=0.88, relwidth=0.18,relheight=0.08)

admin.mainloop()
