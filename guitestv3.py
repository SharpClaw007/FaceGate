from tkinter import *
#from tkinter import ttk
import tkinter as tk
import os



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
    print(usernamecheck)
    

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