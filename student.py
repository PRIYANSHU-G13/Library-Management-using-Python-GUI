import tkinter
from tkinter import font as tkFont
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import *
from tkinter.ttk import *
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import *
from tkinter.ttk import *
from PIL import Image

# Making the window -------------------------------------
win = Tk()
win.title('Welcome [Username_here]')
win.geometry('1150x680')
win.config(bg='White')
win.resizable(False, False)


# Frames ------------------------------
global topF, leftF, rightF

topF = tkinter.Frame(win, width=1150, borderwidth=-1, height=150, bg='black')
topF.grid(column=0, row=0, columnspan=2)

leftF = tkinter.Frame(win, width=850,
                      relief=SUNKEN, height=450, bg="white")
leftF.grid(column=0, row=2)

rightF = tkinter.Frame(win, borderwidth=1, relief=SUNKEN,
                       width=300, height=450, bg="white")
rightF.grid(column=1, row=2, rowspan=1)

tabF = tkinter.Frame(win, width=850, height=80, relief=SUNKEN, bg="white")
tabF.grid(column=0, row=1)

finesF = tkinter.Frame(win, borderwidth=1, relief=SUNKEN,
                       width=300, height=80, bg="white")
finesF.grid(column=1, row=1, rowspan=1)


def library():
    # Entry labels ----------------------------------------------
    for widget in leftF.winfo_children():
        widget.destroy()

    titleFont = tkFont.Font(family='product sans', size=13)
    keywordsL = tkinter.Label(leftF, text='Keywords : ', bg="white", width=12,
                              borderwidth=0, font=titleFont, anchor='e').place(relx=0.01923076*2, rely=0.11-0.06)
    titleL = tkinter.Label(leftF, text='Selected ISBN : ', bg="white", borderwidth=0,
                           width=12, font=titleFont, anchor='e').place(relx=0.01923076*2, rely=0.2+0.05-0.11)

    # Entry fields ----------------------------------------------
    entryFont = tkFont.Font(family='product sans', size=14)
    titleE = tkinter.Entry(leftF, width=38, highlightthickness=3, font=entryFont, selectborderwidth=3,
                           relief='flat', bg="#f7f7f7", selectbackground="white").place(relx=0.21153846, rely=0.11+0.05-0.11)
    isbnE = tkinter.Entry(leftF, width=38, highlightthickness=3, font=entryFont, selectborderwidth=3,
                          relief='flat', bg="#f7f7f7", selectbackground="white").place(relx=0.21153846, rely=0.2+0.05-0.11)

    # Buttons ------------------------------------
    buttonsFont = tkFont.Font(family='product sans', size=12)

    searchBt = tkinter.Button(leftF, text="Search", bg="#F4B400", activebackground="#FFD666",
                              font=buttonsFont, anchor='c', width=13, relief="flat").place(relx=0.78886153, rely=0.11+0.05-0.11)
    requestBt = tkinter.Button(leftF, text="Request", bg="#F4B400", activebackground="#FFD666",
                               font=buttonsFont, anchor='c', width=13, relief="flat").place(relx=0.78886153, rely=0.2+0.05-0.11)

    # Label ---------------------------------------
    titleFont = tkFont.Font(family='courier new', size=10)
    column_list = "ISBN--------------------------TITLE-----------------------------AVAILABILITY---------------------PAGES"
    keywordsL = tkinter.Label(leftF, text=column_list, bg="White", width=100,
                              borderwidth=0, font=titleFont).place(relx=0.01923076, rely=0.2+0.05+0.1-0.11)

    # List ---------------------------------------
    listFont = tkFont.Font(family='times new roman', size=12)
    # scrollY = tkinter.Scrollbar(leftF).place(relx=0.78886153, rely=0.2+0.05+0.1+0.05-0.11)
    ls = tkinter.Listbox(leftF, font=listFont, bg="#f7f7f7",
                         width=100, relief="sunken")

    ls.place(relx=0.01923076, rely=0.2+0.05+0.1+0.05-0.11)
    # scrollY.configure(command=ls.yview)

    for i in range(20):
        s = str(i)+"--------------------------"+"wrgorngrwn" + \
            "--------------------------"+"Yes" + \
            "--------------------------"+str(214)
        s = str(s)
        ls.insert(i, s)

    return


def tabs():
    # Functional buttons ----------------------------------------------
    btFont = tkFont.Font(family='product sans', size=15, weight=tkFont.BOLD)
    library_bt = tkinter.Button(tabF, highlightthickness=0, justify="center", activebackground='#356AC3', activeforeground="white", relief='flat', cursor='hand2',
                                text='LibraryG', width=10, foreground='white', background='#4285F4', font=btFont, command=library).place(relx=0.01923076, rely=0.1)

    fines_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", relief='flat', cursor='hand2',
                              text='Fines', width=10, foreground='white', background='#4285F4', font=btFont).place(relx=0.21153846, rely=0.1)

    history_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", relief='flat', cursor='hand2',
                                text='History', width=10, foreground='white', background='#4285F4', font=btFont).place(relx=0.40384615, rely=0.1)

    request_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", relief='flat', cursor='hand2',
                                text='Requests', width=10, foreground='white', background='#4285F4', font=btFont).place(relx=0.59615384, rely=0.1)

    mybooks_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", relief='flat', cursor='hand2',
                                text='My Books', width=10, foreground='white', background='#4285F4', font=btFont).place(relx=0.78846153, rely=0.1)


tabs()


win.mainloop()
