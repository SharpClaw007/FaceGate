from tkinter import *
#from tkinter import ttk
import tkinter as tk

#main_screen = Tk()  # create a GUI window


def testfunction():
    print('The login shoudl be workinggggg')


def login_screen():
    global login_window

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    login_window = tk.Toplevel(main_screen)
    login_window.geometry("300x250")
    login_window.title("Login Page")
    labelExample = Label(login_window, text = "Please enter your username:")
    entryExample = Entry(login_window, textvariable= username_verify)
    loginbuttonExample = Button(text = 'Login', height = '2', width = '30', command = loginverification)

    entryExample.pack()
    labelExample.pack()
    entryExample.pack()
    loginbuttonExample.pack()

    login_window.mainloop()

def loginverification():
    username_verify = StringVar()
    password_verify = StringVar()

    print(username_verify, password_verify)


def register_screen():
    print('Register stuff')
    return


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login_screen).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command = register_screen).pack()
 
    main_screen.mainloop()

main_account_screen()