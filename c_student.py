from io import BytesIO
import tkinter
from tkinter import font as tkFont
from tkinter.font import families
from PIL import ImageTk, Image
import os
from tkinter import messagebox
from tkinter import ttk
#from tkinter import *
from tkinter.ttk import *
#from tkinter import *
#from tkinter.ttk import *
import tkinter.font as font
#from PIL import ImageTk, Image
#from tkinter import *
#from tkinter.ttk import *
#from PIL import Image
from tkinter import *
import mysql.connector


# Making the window -------------------------------------
win = Tk()
win.title('Welcome [Username_here]')
win.geometry('1150x680')
win.config(bg='White')
win.resizable(False, False)


# Frames ----------------------------------------------------------------------------------------------------
# global topF, leftF, rightF

topF = tkinter.Frame(win, width=1150, borderwidth=-1, height=150, bg='black')
topF.grid(column=0, row=0, columnspan=2)

leftF = tkinter.Frame(win, width=850,
                      relief=SUNKEN, height=450, bg="gray")
leftF.grid(column=0, row=2)

rightF = tkinter.Frame(win, borderwidth=1, relief=SUNKEN,
                       width=300, height=450, bg="pink")
rightF.grid(column=1, row=2, rowspan=1)

tabF = tkinter.Frame(win, width=850, height=80, relief=SUNKEN, bg="gray")
tabF.grid(column=0, row=1)

finesF = tkinter.Frame(win, borderwidth=1, relief=SUNKEN,
                       width=300, height=80, bg="white")
finesF.grid(column=1, row=1, rowspan=1)

#start of Fine frame
def message():
    messagebox.showinfo("Sorry, This option is not available!","Kindly contact to your Admin")

fineFont = tkFont.Font(family='product sans',size=12)
user = tkinter.Label(finesF, text='User : Shivam kumar', fg="green", bg="white", font=fineFont)   
user.place(relx=0, rely=0)
Fine = tkinter.Label(finesF, text='Fine  : 325.50', bg="white", fg="red", font=fineFont)   
Fine.place(relx=0, rely=0.33)
pay_fine=Button(finesF,text='Pay Fine',bg='green',fg='white', activeforeground='black', command=message, bd='3',cursor='hand2',font=fineFont)
pay_fine.place(relx=0.7, rely=0.5)
#end of Fine frame

# Library --------------------------------------------------------------------------------------------------------------

def library():
    dic={
        'CSE':['DS','Algorithms','AI','ML','DL','NNP'],
        'ECE':['Basic electronics','Digital electronics'],
        'IT':['Web development','IT Workshop 1','IT Workshop 2'],
        'Maths':['Disrete Mathematics','Linear Algebra','Differrential equation','Graph theory']
        }
    def dropdown_fun(event):
        #if strem.get()=="CSE":
        catogery = ttk.Combobox(listbox,width=30)
        catogery['values'] = dic[strem.get()]
        catogery.place(relx=0.22+0.25, rely=0.5)
        catogery.current(0)
            
    # Entry labels ----------------------------------------------
    for widget in leftF.winfo_children():
        widget.destroy()

        

    listbox = Listbox(leftF,relief="sunken",font=("courier",15),fg="white",bg='light yellow')
    listbox.place(relx=0.04, rely=0,relwidth=0.92,relheight=0.9)

    label3 = tkinter.Label(listbox,text="SEARCH BOOK",bg='#525b59', fg='white', font='BOLD')
    label3.place(relx=0.35,rely=0.11,relwidth=0.3,relheight=0.1)

    titleFont = tkFont.Font(family='product sans', size=13)
    strem1 = tkinter.Label(listbox, text='Select stream : ', bg="light yellow", width=15,
                              borderwidth=0, font=titleFont, anchor='e').place(relx=0.04+0.25, rely=0.4)
    catogery1 = tkinter.Label(listbox, text='Select catogery : ', bg="light yellow", borderwidth=0,
                           width=15, font=titleFont, anchor='e').place(relx=0.04+0.25, rely=0.5)
    #creating select box
    strem = ttk.Combobox(listbox,width=30)
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



def reuqests():
    for widget in leftF.winfo_children():
        widget.destroy()

    numOfRequest = 20

    #start
    listbox = Listbox(leftF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0.5, rely=0.43,relwidth=0.92,relheight=0.85, anchor=CENTER)
    h = Scrollbar(leftF, orient='horizontal')
    h.place(relx=0.5, rely=0.92, anchor=S, relwidth=0.92)
    v = Scrollbar(leftF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.43, anchor=E, relheight=0.92)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
    #end
    for i in range(numOfRequest):
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = tkinter.Label(listbox,text='Requested_Book_Name', bg="pink",width=60, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        dateFont = tkFont.Font(family='product sans', size=13)
        date = tkinter.Label(listbox, text='issueDate_returnDate', bg="blue", width=20, borderwidth=0, font=dateFont, anchor='c')
        t.window_create(END,window=date)

        statusFont = tkFont.Font(family='product sans', size=13)
        status = tkinter.Label(listbox, text='status', bg="light yellow", fg='black',width=13, borderwidth=0, font=statusFont, anchor='c') 
        t.window_create(END,window=status)

        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16,cursor='hand2') 
        t.window_create(END,window=cancel)
        t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  

def mybooks():
    for widget in leftF.winfo_children():
        widget.destroy()

    numOfRequest = 20

    #start
    listbox = Listbox(leftF, relief="sunken", font=("courier", 15), fg="white")
    listbox.place(relx=0.5, rely=0.43,relwidth=0.92,relheight=0.85, anchor=CENTER)
    h = Scrollbar(leftF, orient='horizontal')
    h.place(relx=0.5, rely=0.92, anchor=S, relwidth=0.92)
    v = Scrollbar(leftF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.43, anchor=E, relheight=0.92)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)  
    #end
    for i in range(numOfRequest):
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = tkinter.Label(listbox,text='MyBook_Name', bg="green",width=60, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        dateFont = tkFont.Font(family='product sans', size=13)
        date = tkinter.Label(listbox, text='issueDate_returnDate', bg="blue", width=20, borderwidth=0, font=dateFont, anchor='c')
        t.window_create(END,window=date)

        statusFont = tkFont.Font(family='product sans', size=13)
        status = tkinter.Label(listbox, text='status', bg="white", width=13, borderwidth=0, font=statusFont, anchor='c') 
        t.window_create(END,window=status)

        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
        t.window_create(END,window=cancel)
        t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  

def history():
    for widget in leftF.winfo_children():
        widget.destroy()

    numOfRequest = 20

    #start
    listbox = Listbox(leftF, relief="sunken", font=("courier", 15), fg="white")
    listbox.place(relx=0.5, rely=0.43,relwidth=0.92,relheight=0.85, anchor=CENTER)
    h = Scrollbar(leftF, orient='horizontal')
    h.place(relx=0.5, rely=0.92, anchor=S, relwidth=0.92)
    v = Scrollbar(leftF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.43, anchor=E, relheight=0.92)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)  
    #end
    for i in range(numOfRequest):
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = tkinter.Label(listbox,text='approved_book_name', bg="gray",width=60, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        dateFont = tkFont.Font(family='product sans', size=13)
        date = tkinter.Label(listbox, text='rating', bg="blue", width=18, borderwidth=0, font=dateFont, anchor='w')
        t.window_create(END,window=date)

        statusFont = tkFont.Font(family='product sans', size=13)
        status = tkinter.Label(listbox, text='status', bg="yellow", width=13, borderwidth=0, font=statusFont, anchor='c') 
        t.window_create(END,window=status)

        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
        t.window_create(END,window=cancel)
        t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  

def fine():
    for widget in leftF.winfo_children():
        widget.destroy()

    numOfRequest = 20

    #start
    listbox = Listbox(leftF, relief="sunken", font=("courier", 15), fg="white")
    listbox.place(relx=0.5, rely=0.43,relwidth=0.92,relheight=0.85, anchor=CENTER)
    h = Scrollbar(leftF, orient='horizontal')
    h.place(relx=0.5, rely=0.92, anchor=S, relwidth=0.92)
    v = Scrollbar(leftF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.43, anchor=E, relheight=0.92)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set) 
    #end
    for i in range(numOfRequest):
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = tkinter.Label(listbox,text='approved_book_name', bg="black", fg="white", width=40, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        dateFont = tkFont.Font(family='product sans', size=13)
        date = tkinter.Label(listbox, text='issue_date', bg="blue", width=18, borderwidth=0, font=dateFont, anchor='c')
        t.window_create(END,window=date)

        statusFont = tkFont.Font(family='product sans', size=13)
        status = tkinter.Label(listbox, text='fine', bg="red", width=13, borderwidth=0, font=statusFont, anchor='c') 
        t.window_create(END,window=status)

        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
        t.window_create(END,window=cancel)
        t.insert(END,"\n")
    #start   
    t.configure(state="disabled") 
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)  
    #end  



def tabs():
    # Functional buttons ----------------------------------------------
    btFont = tkFont.Font(family='product sans', size=15, weight=tkFont.BOLD)
    library_bt = tkinter.Button(tabF,highlightthickness=0, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='Search Book', width=10, foreground='white', background='#4285F4', font=btFont, command=library).place(relx=0.01923076, rely=0.1)

    fines_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", cursor='hand2',
                              text='Fines', width=10, foreground='white', background='#4285F4', font=btFont,command=fine).place(relx=0.21153846, rely=0.1)

    history_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='History', width=10, foreground='white', background='#4285F4', font=btFont,command=history).place(relx=0.40384615, rely=0.1)

    request_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='Requests', width=10, foreground='white', background='#4285F4', font=btFont, command=reuqests).place(relx=0.59615384, rely=0.1)

    mybooks_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2, cursor='hand2',
                                text='My Books', width=10, foreground='white', background='#4285F4', font=btFont,command=mybooks).place(relx=0.78846153, rely=0.1)


tabs()
library()

# -----------------------------------------------------------
# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#     return binaryData


# connector = mysql.connector.Connect(
#     host="localhost",
#     user="root",
#     password="sohamsql",  # Replace XXXX with your MySQL password
#     database="library")
# cursor = connector.cursor()

# # img = ImageTk.PhotoImage(Image.open("C:\Users\Admin\Downloads\peng.jpg"))
# bin_file = convertToBinaryData(r"C:\Users\\Admin\\Downloads\\peng.jpg")
# sql_insert_blob_query = """INSERT INTO testimg(img) VALUES (%s)"""
# insert_blob_tuple = (bin_file,)

# result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)

# connector.commit()

# sql_fetch_blob_query = """SELECT * from testimg;"""
# cursor.execute(sql_fetch_blob_query)

# record = cursor.fetchone()


# def write_file(data, filename):
#     # Convert binary data to proper format and write it on Hard Disk
#     with open(filename, 'wb') as file:
#         file.write(data)


# # for i in record:
# file = record[0]
# # write_file(file, r"C:\Users\\Admin\\Downloads\\peng_result.jpg")


# img = Image.open(BytesIO(file))
# phimg = ImageTk.PhotoImage(img)

# panel = tkinter.Label(leftF, image=phimg)
# panel.grid(row=0, rowspan=5, columnspan=2)
# # panel = Tkinter.Label(window, image=phimg)
# --------------------------------------------------

# for i in range(5):
#     tmpL = tkinter.Label(leftF, text="HI----this is button number : "+str(i)).grid(column=2, row=i)

# for i in range(5):

# soham = tkinter.Frame(leftF, width=800, relief=SUNKEN,
#                       height=200, bg="red", borderwidth=1).grid(column=1, row=2)

# book_name = tkinter.Label(leftF, text="book_name : ",
#   bg='Yellow',  borderwidth=1).place(x=0, y=4)

# place(relx=0.0, rely=0.5)
# keywordsL = tkinter.Label(leftF, text=column_list, bg="White", width=100,
#   borderwidth=0, font=titleFont).place(relx=0.01923076, rely=0.2+0.05+0.1-0.11)

# tmp.grid(column=0, row=2)

win.mainloop()
