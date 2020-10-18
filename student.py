#this code will be used as module to import into login.py file so, here variables have been declared as global
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import mysql.connector
from tkinter import font as tkFont
from tkcalendar import Calendar, DateEntry #pip install tkcalendar
from tkinter import ttk
from time import time 

#conneting MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="XXXX",#Replace XXXX with your MySQL password
    database="Library")
cur = con.cursor()

Regno=""

def start_student(reg,password): 
    global cur,Regno,win,topF,bottomF,tabF
    #initialize Regno of the student to argument passed from module login.py into start() function after login 
    Regno=reg
    
    #start
    #fetching data of user after login
    command="select Sname, Fine from student where Regno=%s and Password=%s"
    var=[reg, password]
    cur.execute(command,var)
    user_details=cur.fetchall()
    #end

    # Making the window -------------------------------------
    win = Tk()
    win.title(str("Hii, "+user_details[0][0])+"  |   Welcome to IIIT Kottayam Library   |   Student Section")
    win.geometry('1150x630+50+5')
    win.config(bg='White')
    win.resizable(False, False)


    # Frames ----------------------------------------------------------------------------------------------------
    
    #start
    topF = Frame(win, borderwidth=-1, bg='black')
    topF.place(relx=0, rely=0, relwidth=1, relheight=0.2206)

    tabF = Frame(win, relief=SUNKEN, bg="red")
    tabF.place(relx=0, rely=0.2206, relwidth=1, relheight=0.1176)

    bottomF = Frame(win, relief=SUNKEN, bg="yellow")
    bottomF.place(relx=0, rely=0.2206+0.1176, relwidth=1, relheight=1-0.2206-0.1176)
    #end
    
    #start of Fine
    #creting listbox1 to insert fine into this listbox
    listbox1 = Listbox(topF,relief="sunken",font=("courier",15),bg='black')
    listbox1.place(relx=0.8, rely=0,relwidth=1,relheight=1)

    #function to display message of PayFine button
    def message():
        messagebox.showinfo("Sorry, This option is not available!\n","Kindly contact to your Admin")

    fineFont = tkFont.Font(size=12)
    user = Label(listbox1, text='User : ' + str(user_details[0][0]), fg="green", font=fineFont)   
    user.place(relx=0, rely=0)
    Fine = Label(listbox1, text='Fine  : ' + str(user_details[0][1]), fg="red", font=fineFont)   
    Fine.place(relx=0, rely=0.25)
    pay_fine=Button(listbox1,text='Pay Fine',bg='green',fg='white', activeforeground='black', command="", bd='3',cursor='hand2', font=fineFont)
    pay_fine.place(relx=0.125, rely=0.23)
    #end of Fine
        
    #calling tab() function from start() function to display tabs
    tabs()
    win.mainloop()
#end  of start() function
 

# Library --------------------------------------------------------------------------------------------------------------

def library():
    global cur,win,topF,bottomF,tabF
    dic={
        'CSE':['DS','Algorithms','AI','ML','DL','NNP'],
        'ECE':['Basic electronics','Digital electronics'],
        'IT':['Web development','IT Workshop 1','IT Workshop 2'],
        'Maths':['Disrete Mathematics','Linear Algebra','Differrential equation','Graph theory']
        }
    def dropdown_fun(event):
        #if strem.get()=="CSE":
        catogery = ttk.Combobox(listbox,width=30,state="readonly")
        catogery['values'] = dic[strem.get()]
        catogery.place(relx=0.22+0.25, rely=0.5)
        catogery.current(0)
            
    # Entry labels ----------------------------------------------
    for widget in bottomF.winfo_children():
        widget.destroy()

        

    listbox = Listbox(bottomF,relief="sunken",font=("courier",15),fg="white",bg='light yellow')
    listbox.place(relx=0.04, rely=0,relwidth=0.92,relheight=0.9)

    label3 = Label(listbox,text="SEARCH BOOK",bg='#525b59', fg='white', font='BOLD')
    label3.place(relx=0.35,rely=0.11,relwidth=0.3,relheight=0.1)

    titleFont = tkFont.Font(family='product sans', size=13)
    strem1 = Label(listbox, text='Select stream : ', bg="light yellow", width=15,
                              borderwidth=0, font=titleFont, anchor='e').place(relx=0.04+0.25, rely=0.4)
    catogery1 = Label(listbox, text='Select catogery : ', bg="light yellow", borderwidth=0,
                           width=15, font=titleFont, anchor='e').place(relx=0.04+0.25, rely=0.5)
    #creating select box
    strem = ttk.Combobox(listbox,width=30,state="readonly")
    strem['values']=('CSE','ECE','IT','Maths')
    strem.current(0)
    strem.bind("<<ComboboxSelected>>", dropdown_fun)
    strem.place(relx=0.22+0.25, rely=0.4)

    catogery = ttk.Combobox(listbox,width=30)
    catogery['values']=dic['CSE']
    catogery.place(relx=0.22+0.25, rely=0.5)
    catogery.current(1)

    submit_btn = Button(listbox,text="SUBMIT",bd=5, bg='green', fg='white', font='BOLD', cursor='hand2', command="")
    submit_btn.place(relx=0.425,rely=0.65,relwidth=0.15,relheight=0.1)
    #start
    #the given code will prevent user to directly access to this file
    '''
    if __name__ == "__main__":
        messagebox.showinfo("Error!", "Kindly login before accessing It!")
        win.destroy()
    '''    
    #end



def reuqests():
    global cur,win,topF,bottomF,tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    numOfRequest = 20

    #start
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0.5, rely=0.43,relwidth=0.92,relheight=0.85, anchor=CENTER)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=0.9, anchor=S, relwidth=0.92)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=0.98, rely=0.43, anchor=E, relheight=0.92)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
    #end
    for i in range(numOfRequest):
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox,text='Requested_Book_Name : ' + str(i), bg="pink",width=60, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        dateFont = tkFont.Font(family='product sans', size=13)
        date = Label(listbox, text='issueDate_returnDate', bg="blue", width=40, borderwidth=0, font=dateFont, anchor='c')
        t.window_create(END,window=date)

        statusFont = tkFont.Font(family='product sans', size=13)
        status = Label(listbox, text='status', bg="light yellow", fg='black',width=13, borderwidth=0, font=statusFont, anchor='c') 
        t.window_create(END,window=status)

        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16,cursor='hand2') 
        t.window_create(END,window=cancel)
        t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  

def mybooks():
    global cur,win,topF,bottomF,tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    numOfRequest = 20

    #start
    #command='select '
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0.5, rely=0.43,relwidth=0.92,relheight=0.85, anchor=CENTER)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=0.9, anchor=S, relwidth=0.92)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=0.98, rely=0.43, anchor=E, relheight=0.92)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)  
    #end
    for i in range(numOfRequest):
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox,text='Requested_Book_Name : ' + str(i), bg="green",width=60, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        dateFont = tkFont.Font(family='product sans', size=13)
        date = Label(listbox, text='issueDate_returnDate', bg="blue", width=40, borderwidth=0, font=dateFont, anchor='c')
        t.window_create(END,window=date)

        statusFont = tkFont.Font(family='product sans', size=13)
        status = Label(listbox, text='status', bg="white", width=13, borderwidth=0, font=statusFont, anchor='c') 
        t.window_create(END,window=status)

        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
        t.window_create(END,window=cancel)
        t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  

def history():
    global Regno,cur,win,topF,bottomF,tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    #start
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0.5, rely=0.43,relwidth=0.92,relheight=0.85, anchor=CENTER)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=0.9, anchor=S, relwidth=0.92)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=0.98, rely=0.43, anchor=E, relheight=0.92)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set) 
    #end
    command='select DISTINCT Book.Bname,Book.Author,Return_book.Approved_date,Return_book.Return_date,Book.Bid,SubBook.Sub_bid,Return_book.Borrow_ID from Book,Student,SubBook,Return_book WHERE Book.Bid=SubBook.Bid and SubBook.Sub_bid=Return_book.Sub_bid and Return_book.Student_regno=%s'
    var=[Regno]
    cur.execute(command,var)
    rows=cur.fetchall()

    bookNameFont = tkFont.Font(family='product sans', size=13)
    bookName = Label(listbox,text='Book Name', bg="pink",width=40, borderwidth=0,font=bookNameFont, anchor='c')
    t.window_create(END,window=bookName)

    authorFont = tkFont.Font(family='product sans', size=13)
    author = Label(listbox, text='Author', bg="pink", width=40, borderwidth=0, font=authorFont, anchor='c')
    t.window_create(END,window=author)

    approveddateFont = tkFont.Font(family='product sans', size=13)
    approveddate = Label(listbox, text='Approved Date', bg="pink", width=13, borderwidth=0, font=approveddateFont, anchor='c') 
    t.window_create(END,window=approveddate)

    returndateFont = tkFont.Font(family='product sans', size=13)
    returndate = Label(listbox, text='Return date', bg="pink", width=13, borderwidth=0, font=returndateFont, anchor='c') 
    t.window_create(END,window=returndate)

    bidFont = tkFont.Font(family='product sans', size=13)
    bid = Label(listbox, text='Book ID', bg="pink", width=13, borderwidth=0, font=bidFont, anchor='c') 
    t.window_create(END,window=bid)

    subbidFont = tkFont.Font(family='product sans', size=13)
    subbid = Label(listbox, text='Sub Book ID', bg="pink", width=13, borderwidth=0, font=subbidFont, anchor='c') 
    t.window_create(END,window=subbid)

    borrowidFont = tkFont.Font(family='product sans', size=13)
    borrowid = Label(listbox, text='Borrow ID', bg="pink", width=13, borderwidth=0, font=borrowidFont, anchor='c') 
    t.window_create(END,window=borrowid)
    t.insert(END,"\n")
    #t.insert(END,"\n")

    for a in rows:
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox,text=str(a[0]), bg="gray",width=40, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        authorFont = tkFont.Font(family='product sans', size=13)
        author = Label(listbox, text=str(a[1]), bg="green", width=40, borderwidth=0, font=authorFont, anchor='w')
        t.window_create(END,window=author)

        approveddateFont = tkFont.Font(family='product sans', size=13)
        approveddate = Label(listbox, text=str(a[2]), bg="yellow", width=13, borderwidth=0, font=approveddateFont, anchor='c') 
        t.window_create(END,window=approveddate)

        returndateFont = tkFont.Font(family='product sans', size=13)
        returndate = Label(listbox, text=str(a[3]), bg="gray", width=13, borderwidth=0, font=returndateFont, anchor='c') 
        t.window_create(END,window=returndate)

        bidFont = tkFont.Font(family='product sans', size=13)
        bid = Label(listbox, text=str(a[4]), bg="green", width=13, borderwidth=0, font=bidFont, anchor='c') 
        t.window_create(END,window=bid)

        subbidFont = tkFont.Font(family='product sans', size=13)
        subbid = Label(listbox, text=str(a[5]), bg="yellow", width=13, borderwidth=0, font=subbidFont, anchor='c') 
        t.window_create(END,window=subbid)

        borrowidFont = tkFont.Font(family='product sans', size=13)
        borrowid = Label(listbox, text=str(a[6]), bg="gray", width=13, borderwidth=0, font=borrowidFont, anchor='c') 
        t.window_create(END,window=borrowid)

        '''
        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
        t.window_create(END,window=cancel)
        '''
        t.insert(END,"\n")
        #t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  

def fine():
    global Regno,cur,win,topF,bottomF,tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    #start
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0.5, rely=0.43,relwidth=0.92,relheight=0.85, anchor=CENTER)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=0.9, anchor=S, relwidth=0.92)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=0.98, rely=0.43, anchor=E, relheight=0.92)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set) 
    #end
    command='select Book.Bname,Book.Author,Borrow.Approved_date,ADDDATE(Borrow.Approved_date, 14),(CURDATE()-ADDDATE(Borrow.Approved_date, 14))*5 from Borrow, SubBook, Book where Student_regno=%s and Borrow.sub_bid=SubBook.sub_bid and SubBook.bid=Book.bid and (CURDATE()-ADDDATE(Borrow.Approved_date, 14))*5 > 0'
    #bookname-0,author-1,approved_date-2,expexted_return_date-3,fine-4
    var=[Regno]
    cur.execute(command,var)
    rows=cur.fetchall()

    Font0 = tkFont.Font(family='product sans', size=13)
    Bname = Label(listbox,text='Book Name', bg="pink",width=40, borderwidth=0,font=Font0, anchor='c')
    t.window_create(END,window=Bname)

    Font1 = tkFont.Font(family='product sans', size=13)
    author = Label(listbox, text='Author', bg="pink", width=40, borderwidth=0, font=Font1, anchor='c')
    t.window_create(END,window=author)

    Font2 = tkFont.Font(family='product sans', size=13)
    approveddate = Label(listbox, text='Approved Date', bg="pink", width=13, borderwidth=0, font=Font2, anchor='c') 
    t.window_create(END,window=approveddate)

    Font3 = tkFont.Font(family='product sans', size=13)
    returndate = Label(listbox, text='Expected Return date', bg="pink", width=23, borderwidth=0, font=Font3, anchor='c') 
    t.window_create(END,window=returndate)

    Font4 = tkFont.Font(family='product sans', size=13)
    bid = Label(listbox, text='Fine', bg="pink", width=13, borderwidth=0, font=Font4, anchor='c') 
    t.window_create(END,window=bid)

    Font4 = tkFont.Font(family='product sans', size=13)
    bid = Label(listbox, text='Return Button', bg="pink", width=17, borderwidth=0, font=Font4, anchor='c') 
    t.window_create(END,window=bid)
    t.insert(END,"\n")
    #t.insert(END,"\n")

    for a in rows:
        #bookname-0,author-1,approved_date-2,expexted_return_date-3,fine-4
        Font0 = tkFont.Font(family='product sans', size=13)
        Bname = Label(listbox,text=a[0], bg="gray",width=40, borderwidth=0,font=Font0, anchor='w')
        t.window_create(END,window=Bname)

        Font1 = tkFont.Font(family='product sans', size=13)
        author = Label(listbox, text=a[1], bg="green", width=40, borderwidth=0, font=Font1, anchor='w')
        t.window_create(END,window=author)

        Font2 = tkFont.Font(family='product sans', size=13)
        approveddate = Label(listbox, text=a[2], bg="yellow", width=13, borderwidth=0, font=Font2, anchor='c') 
        t.window_create(END,window=approveddate)

        Font3 = tkFont.Font(family='product sans', size=13)
        returndate = Label(listbox, text=a[3], bg="gray", width=23, borderwidth=0, font=Font3, anchor='c') 
        t.window_create(END,window=returndate)

        Font4 = tkFont.Font(family='product sans', size=13)
        bid = Label(listbox, text=a[4], bg="green", width=13, borderwidth=0, font=Font4, anchor='c') 
        t.window_create(END,window=bid)

        Font5 = tkFont.Font(family='product sans', size=12)
        return_btn = Button(listbox, text="Return",command="", font=Font5, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16,cursor='hand2') 
        t.window_create(END,window=return_btn)
        t.insert(END,"\n")
        #t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  



def tabs():
    global cur,win,topF,bottomF,tabF
    # Functional buttons ----------------------------------------------
    btFont = tkFont.Font(family='product sans', size=15, weight=tkFont.BOLD)
    library_bt = Button(tabF,highlightthickness=0, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='Search Book', width=10, foreground='white', background='#4285F4', font=btFont, command=library).place(relx=0.01923076, rely=0.1)

    fines_bt = Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", cursor='hand2',
                              text='Fines', width=10, foreground='white', background='#4285F4', font=btFont,command=fine).place(relx=0.21153846, rely=0.1)

    history_bt = Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='History', width=10, foreground='white', background='#4285F4', font=btFont,command=history).place(relx=0.40384615, rely=0.1)

    request_bt = Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='Requests', width=10, foreground='white', background='#4285F4', font=btFont, command=reuqests).place(relx=0.59615384, rely=0.1)

    mybooks_bt = Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='My Books', width=10, foreground='white', background='#4285F4', font=btFont,command=mybooks).place(relx=0.78846153, rely=0.1)

    library() 
    #win.mainloop()                           

if __name__ == "__main__":
    
    start_student('2019BCS0034','shiva') #comment out this this line if you don't want to run this program as a main program
    #if you directely use this code before login, it will show  a message box with "Error!, Kindly login before accessing It!" and 
    #after clicking on the ok button the whole window will be destroyed.
    #start
    '''
    write this code into the end of library function(the last called function)
    if __name__ == "__main__":
        messagebox.showinfo("Error!", "Kindly login before accessing It!")
        win.destroy()
    ''' 
    #end


