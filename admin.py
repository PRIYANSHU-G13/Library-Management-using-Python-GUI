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
header_admin.place(relx=0.65,rely=0.02,relwidth=0.1,relheight=0.05)

header_username=Button(admin,text='USERNSME',fg='black')
header_username.place(relx=0.76,rely=0.02,relwidth=0.2,relheight=0.05)

headingFrame1 = Frame(admin,bg="#FFBB00",bd=2)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.08)

headingLabel = Label(headingFrame1, text="Welcome ADMIN", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# search entry
search_entry=Entry(admin)
search_entry.insert(0,'Search Students/Books')
search_entry.place(relx=0.11,rely=0.3, relwidth=0.45, relheight=0.08)

# Search Students
sr1 = Button(admin,text="Search Students",bg='#7d7d7d',fg='black')#,command=SearchStudents)
sr1.place(relx=0.57,rely=0.3, relwidth=0.16, relheight=0.08)

# Search books
sr2 = Button(admin,text="Search Books",bg='#7d7d7d',fg='black')#,command=SearchBooks)
sr2.place(relx=0.74,rely=0.3, relwidth=0.16, relheight=0.08)

labelFrame = Frame(admin,bg='black')
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

quitBtn = Button(admin,text="Quit",bg='#f7f1e3', fg='black', command=admin.destroy)
quitBtn.place(relx=0.12,rely=0.88, relwidth=0.18,relheight=0.08)

admin.mainloop()
