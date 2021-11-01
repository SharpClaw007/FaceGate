from tkinter import *
#from tkinter import ttk
import tkinter as tk
import os
from pymongo import MongoClient
import pymongo
from pprint import pprint
import certifi

ca = certifi.where()

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://SharpClaw007:jcrc8383@cluster0.n5s2p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING, tlsCAFile=ca)

    # Create the database for our example (we will use the same database throughout the tutorial
studentlist = client['studentlist']

col = studentlist['Students']



def login():
    global username_verify
    username_verify = StringVar()

    login_window = tk.Toplevel()
    login_window.geometry('300x250')
    login_window.title('Login Window')
    title1 = Label(login_window, text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13))
    button1 = Button(login_window, text="Login", height="2", width="30", command = logincheck)
    label1 = Label(login_window, text = (''))
    entry1 = Entry(login_window, textvariable = username_verify)
    label2 = Label(login_window, text = (''))
    button2 = Button(login_window, text='Quit', height='2', width="30", command = quitfunction)


    title1.pack()
    label1.pack()
    entry1.pack()
    button1.pack()
    label2.pack()
    button2.pack()


    login_window.mainloop()

def logincheck():
    usernamecheck = username_verify.get()

    global myquery
    global ident
    global x
    ident = usernamecheck
    myquery = {'username' : ident}
    cur = col.find({'username': ident})

    if cur.count()==0:
        print('No students found in search.')
    else:
        for x in col.find({'username': ident}):
            studentinfo()
            print('\n')
            pprint(x)
            

def studentinfo():
    global student_window
    global studentreadout

    studentreadout = x

    student_window = tk.Toplevel()
    student_window.geometry('1000x100')
    student_window.title('Student Information')
    #title1V = Label(student_window, text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13))

    label1V = Label(student_window, text = studentreadout)
    label2V = Label(student_window, text = (''))
    button2V = Button(student_window, text='Quit', height='2', width="30", command = quitfunction)


    #title1V.pack()
    label1V.pack()
    label2V.pack()
    button2V.pack()


    student_window.mainloop()

def quitfunction():
    main_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login Page", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(main_screen, text='Quit', height='2', width="30", command = quitfunction).pack()
    #Button(text="Register", height="2", width="30", command = register_screen).pack()
 
    main_screen.mainloop()

main_account_screen()