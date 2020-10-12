from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
'''
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
'''
def Login():
    global username, password 
    user = str(username.get())
    password1 = str(password.get())
    command1 = "select * from admin where id=%s AND password=%s"
    var=[user,password1]
    command2 = "select * from student where id=%s AND password=%s"
    try:
        # Add your own database name and password here to reflect in the code
        # before running this program create a databse python_pro
        #Create tables admin and student in database python_pro  
        mypass = "your_MySQL_password"
        mydatabase="python_pro"
        con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
        cur = con.cursor()
        cur.execute(command1,var)
        var1=cur.fetchall()
        cur.execute(command2,var)
        var2=cur.fetchall()
        
        if (len(var1)+len(var2))<1:
          messagebox.showinfo('_','Invalid user name or password') 
        else: 
          for i in var1:
            if i[0]==user and i[1]==password1:
              messagebox.showinfo('sucess','Login Success as Admin')
          for i in var2:
            if i[0]==user and i[1]==password1:
              messagebox.showinfo('sucess','Login Success as Student')               
    except:
        messagebox.showinfo("Error","Can't find data into Database")



root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")


    
Canvas1 = Canvas(root)
Canvas1.config(bg="pink")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Team Rolex Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

labelFrame = Frame(root,bg='black')
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

# User name
lb1 = Label(labelFrame,text="User name : ", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.3, relheight=0.1)
        
username = Entry(labelFrame)
username.place(relx=0.3,rely=0.3, relwidth=0.5, relheight=0.1)

# Password
lb2 = Label(labelFrame,text="Password : ", bg='black', fg='white')
lb2.place(relx=0.05,rely=0.5, relheight=0.1)
        
password = Entry(labelFrame)
password.place(relx=0.3,rely=0.5, relwidth=0.5, relheight=0.1)
password.config(show="*")

#Submit Button
SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=Login)
SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)


root.mainloop()