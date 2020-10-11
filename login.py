from io import BytesIO
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
import mysql.connector


win = Tk()
win.title('Library Management System')
win.geometry('1150x680')
win.config(bg='White')
win.resizable(False, False)


# focusBorderImageData = '''
#     R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
#     rOzq7JyanNza3Ly6vPz6/ISChMTGxKSmpOTm5JSWlNTW1LS2tPT29IyOjMzO
#     zKyurOzu7JyenNze3Ly+vPz+/OkAKOUA5IEAEnwAAACuQACUAAFBAAB+AFYd
#     QAC0AABBAAB+AIjMAuEEABINAAAAAHMgAQAAAAAAAAAAAKjSxOIEJBIIpQAA
#     sRgBMO4AAJAAAHwCAHAAAAUAAJEAAHwAAP+eEP8CZ/8Aif8AAG0BDAUAAJEA
#     AHwAAIXYAOfxAIESAHwAAABAMQAbMBZGMAAAIEggJQMAIAAAAAAAfqgaXESI
#     5BdBEgB+AGgALGEAABYAAAAAAACsNwAEAAAMLwAAAH61MQBIAABCM8B+AAAU
#     AAAAAAAApQAAsf8Brv8AlP8AQf8Afv8AzP8A1P8AQf8AfgAArAAABAAADAAA
#     AACQDADjAAASAAAAAACAAADVABZBAAB+ALjMwOIEhxINUAAAANIgAOYAAIEA
#     AHwAAGjSAGEEABYIAAAAAEoBB+MAAIEAAHwCACABAJsAAFAAAAAAAGjJAGGL
#     AAFBFgB+AGmIAAAQAABHAAB+APQoAOE/ABIAAAAAAADQAADjAAASAAAAAPiF
#     APcrABKDAAB8ABgAGO4AAJAAqXwAAHAAAAUAAJEAAHwAAP8AAP8AAP8AAP8A
#     AG0pIwW3AJGSAHx8AEocI/QAAICpAHwAAAA0SABk6xaDEgB8AAD//wD//wD/
#     /wD//2gAAGEAABYAAAAAAAC0/AHj5AASEgAAAAA01gBkWACDTAB8AFf43PT3
#     5IASEnwAAOAYd+PuMBKQTwB8AGgAEGG35RaSEgB8AOj/NOL/ZBL/gwD/fMkc
#     q4sA5UGpEn4AAIg02xBk/0eD/358fx/4iADk5QASEgAAAALnHABkAACDqQB8
#     AMyINARkZA2DgwB8fBABHL0AAEUAqQAAAIAxKOMAPxIwAAAAAIScAOPxABIS
#     AAAAAIIAnQwA/0IAR3cAACwAAAAAQABAAAAI/wA/CBxIsKDBgwgTKlzIsKFD
#     gxceNnxAsaLFixgzUrzAsWPFCw8kDgy5EeQDkBxPolypsmXKlx1hXnS48UEH
#     CwooMCDAgIJOCjx99gz6k+jQnkWR9lRgYYDJkAk/DlAgIMICZlizat3KtatX
#     rAsiCNDgtCJClQkoFMgqsu3ArBkoZDgA8uDJAwk4bGDmtm9BZgcYzK078m4D
#     Cgf4+l0skNkGCg3oUhR4d4GCDIoZM2ZWQMECyZQvLMggIbPmzQIyfCZ5YcME
#     AwFMn/bLLIKBCRtMHljQQcDV2ZqZTRDQYfWFAwMqUJANvC8zBhUWbDi5YUAB
#     Bsybt2VGoUKH3AcmdP+Im127xOcJih+oXsEDdvOLuQfIMGBD9QwBlsOnzcBD
#     hfrsuVfefgzJR599A+CnH4Hb9fcfgu29x6BIBgKYYH4DTojQc/5ZGGGGGhpU
#     IYIKghgiQRw+GKCEJxZIwXwWlthiQyl6KOCMLsJIIoY4LlQjhDf2mNCI9/Eo
#     5IYO2sjikX+9eGCRCzL5V5JALillY07GaOSVb1G5ookzEnlhlFx+8OOXZb6V
#     5Y5kcnlmckGmKaaMaZrpJZxWXjnnlmW++WGdZq5ZXQEetKmnlxPgl6eUYhJq
#     KKOI0imnoNbF2ScFHQJJwW99TsBAAAVYWEAAHEQAZoi1cQDqAAeEV0EACpT/
#     JqcACgRQAW6uNWCbYKcyyEwGDBgQwa2tTlBBAhYIQMFejC5AgQAWJNDABK3y
#     loEDEjCgV6/aOcYBAwp4kIF6rVkXgAEc8IQZVifCBRQHGqya23HGIpsTBgSU
#     OsFX/PbrVVjpYsCABA4kQCxHu11ogAQUIOAwATpBLDFQFE9sccUYS0wAxD5h
#     4DACFEggbAHk3jVBA/gtTIHHEADg8sswxyzzzDQDAAEECGAQsgHiTisZResN
#     gLIHBijwLQEYePzx0kw37fTSSjuMr7ZMzfcgYZUZi58DGsTKwbdgayt22GSP
#     bXbYY3MggQIaONDzAJ8R9kFlQheQQAAOWGCAARrwdt23Bn8H7vfggBMueOEG
#     WOBBAAkU0EB9oBGUdXIFZJBABAEEsPjmmnfO+eeeh/55BBEk0Ph/E8Q9meQq
#     bbDABAN00EADFRRQ++2254777rr3jrvjFTTQwQCpz7u6QRut5/oEzA/g/PPQ
#     Ry/99NIz//oGrZpUUEAAOw==
# '''

# borderImageData = '''
#     R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
#     rOzq7JyanNza3Ly6vPz6/ISChMTGxKSmpOTm5JSWlNTW1LS2tPT29IyOjMzO
#     zKyurOzu7JyenNze3Ly+vPz+/OkAKOUA5IEAEnwAAACuQACUAAFBAAB+AFYd
#     QAC0AABBAAB+AIjMAuEEABINAAAAAHMgAQAAAAAAAAAAAKjSxOIEJBIIpQAA
#     sRgBMO4AAJAAAHwCAHAAAAUAAJEAAHwAAP+eEP8CZ/8Aif8AAG0BDAUAAJEA
#     AHwAAIXYAOfxAIESAHwAAABAMQAbMBZGMAAAIEggJQMAIAAAAAAAfqgaXESI
#     5BdBEgB+AGgALGEAABYAAAAAAACsNwAEAAAMLwAAAH61MQBIAABCM8B+AAAU
#     AAAAAAAApQAAsf8Brv8AlP8AQf8Afv8AzP8A1P8AQf8AfgAArAAABAAADAAA
#     AACQDADjAAASAAAAAACAAADVABZBAAB+ALjMwOIEhxINUAAAANIgAOYAAIEA
#     AHwAAGjSAGEEABYIAAAAAEoBB+MAAIEAAHwCACABAJsAAFAAAAAAAGjJAGGL
#     AAFBFgB+AGmIAAAQAABHAAB+APQoAOE/ABIAAAAAAADQAADjAAASAAAAAPiF
#     APcrABKDAAB8ABgAGO4AAJAAqXwAAHAAAAUAAJEAAHwAAP8AAP8AAP8AAP8A
#     AG0pIwW3AJGSAHx8AEocI/QAAICpAHwAAAA0SABk6xaDEgB8AAD//wD//wD/
#     /wD//2gAAGEAABYAAAAAAAC0/AHj5AASEgAAAAA01gBkWACDTAB8AFf43PT3
#     5IASEnwAAOAYd+PuMBKQTwB8AGgAEGG35RaSEgB8AOj/NOL/ZBL/gwD/fMkc
#     q4sA5UGpEn4AAIg02xBk/0eD/358fx/4iADk5QASEgAAAALnHABkAACDqQB8
#     AMyINARkZA2DgwB8fBABHL0AAEUAqQAAAIAxKOMAPxIwAAAAAIScAOPxABIS
#     AAAAAIIAnQwA/0IAR3cAACwAAAAAQABAAAAI/wA/CBxIsKDBgwgTKlzIsKFD
#     gxceNnxAsaLFixgzUrzAsWPFCw8kDgy5EeQDkBxPolypsmXKlx1hXnS48UEH
#     CwooMCDAgIJOCjx99gz6k+jQnkWR9lRgYYDJkAk/DlAgIMICkVgHLoggQIPT
#     ighVJqBQIKvZghkoZDgA8uDJAwk4bDhLd+ABBmvbjnzbgMKBuoA/bKDQgC1F
#     gW8XKMgQOHABBQsMI76wIIOExo0FZIhM8sKGCQYCYA4cwcCEDSYPLOgg4Oro
#     uhMEdOB84cCAChReB2ZQYcGGkxsGFGCgGzCFCh1QH5jQIW3xugwSzD4QvIIH
#     4s/PUgiQYcCG4BkC5P/ObpaBhwreq18nb3Z79+8Dwo9nL9I8evjWsdOX6D59
#     fPH71Xeef/kFyB93/sln4EP2Ebjegg31B5+CEDLUIH4PVqiQhOABqKFCF6qn
#     34cHcfjffCQaFOJtGaZYkIkUuljQigXK+CKCE3po40A0trgjjDru+EGPI/6I
#     Y4co7kikkAMBmaSNSzL5gZNSDjkghkXaaGIBHjwpY4gThJeljFt2WSWYMQpZ
#     5pguUnClehS4tuMEDARQgH8FBMBBBExGwIGdAxywXAUBKHCZkAIoEEAFp33W
#     QGl47ZgBAwZEwKigE1SQgAUCUDCXiwtQIIAFCTQwgaCrZeCABAzIleIGHDD/
#     oIAHGUznmXABGMABT4xpmBYBHGgAKGq1ZbppThgAG8EEAW61KwYMSOBAApdy
#     pNp/BkhAAQLcEqCTt+ACJW645I5rLrgEeOsTBtwiQIEElRZg61sTNBBethSw
#     CwEA/Pbr778ABywwABBAgAAG7xpAq6mGUUTdAPZ6YIACsRKAAbvtZqzxxhxn
#     jDG3ybbKFHf36ZVYpuE5oIGhHMTqcqswvyxzzDS/HDMHEiiggQMLDxCZXh8k
#     BnEBCQTggAUGGKCB0ktr0PTTTEfttNRQT22ABR4EkEABDXgnGUEn31ZABglE
#     EEAAWaeN9tpqt832221HEEECW6M3wc+Hga3SBgtMODBABw00UEEBgxdO+OGG
#     J4744oZzXUEDHQxwN7F5G7QRdXxPoPkAnHfu+eeghw665n1vIKhJBQUEADs=
# '''
# ignore the above two datas

buttonsFont = tkFont.Font(family='product sans', size=15)

login = tkinter.Button(win, text="Next", bg="#4285F4", activebackground="#356AC3", activeforeground="white",
                       font=buttonsFont, anchor='c', width=13, relief="flat", fg="white")
login.place(relx=0.655555, rely=0.58+0.1, anchor=CENTER)

n = 1
username = ''
password = ''


def func():
    print(n)


def f1(n1):
    global n, username, password
    print('n = ', n)
    if n1 == 1:
        username = login_input.get()
        print(username)
        login_input.config(show="*")
        login_input.delete(0, END)
        backbt.place(relx=0.345555, rely=0.58+0.1, anchor=CENTER)
        unsername_display.configure(text=username)
        unsername_display.place(relx=0.5, rely=0.5, anchor=CENTER)
        n = n+1
        login.config(text="Login")

    if n1 >= 2:
        print("PASSWORD TIME")
        password = login_input.get()
        print(password)

        print("username = ", username, " password = ", password)
        # from here login process will start
        # password


def f():
    if(login_input.get() == ''):
        print("Empty input")
        return

    f1(n)


login.config(command=f)


def back():
    global n
    login_input.delete(0, END)
    n = 1
    login_input.config(show='')
    unsername_display.place_forget()
    backbt.place_forget()
    login.config(text="Next")


# Login Picture
img = PhotoImage(file="D:\\team_project\\project\\login_logo.png")
login_logo = tkinter.Label(image=img, bg="white", height=250, width=250)
login_logo.place(relx=0.5, rely=0.25, anchor=CENTER)

# Login input
entryFont = tkFont.Font(family='product sans', size=15)

login_input = tkinter.Entry(win, width=38, highlightthickness=3, font=entryFont, selectborderwidth=3,
                            relief='flat', bg="#f7f7f7", selectbackground="white")
login_input.place(relx=0.5, rely=0.5+0.08, anchor=CENTER)
login_input.bind('<Return>', (lambda event: f()))
login_input.bind('<Escape>', (lambda event: f()))

# Login buttons
buttonsFont = tkFont.Font(family='product sans', size=15)


unsername_display = tkinter.Label(bg="white", borderwidth=1, font=buttonsFont)

# Back Button
backbt = tkinter.Button(win, text="Back", bg="#4285F4", activebackground="#356AC3", activeforeground="white",
                        font=buttonsFont, anchor='c', width=13, relief="flat", fg="white", command=back)


win.mainloop()
