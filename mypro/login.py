from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
from hotel import hotelman

#connecting to the database
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="hoteldb")
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    #root1.destroy()

def error():
    global err
   # err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",fg="#142966",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="#142966",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
   # succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="#CCCCCCoo", width=8, height=1, command=succ_destroy).pack()





def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry("300x300")
    global username_varify
    global password_varify
    Label(root2, text="Log-In Portal", bg="#142966", fg="white", font=("times new roman", 20, "bold"),width=300,pady=18).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In",font=("times new roman", 18, "bold"), bg="#999900",command=login_varify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("200x100")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()


def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()


def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login where username = %s and password = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        hotelman(root)
    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.title("Log-IN Portal")
    root.geometry("300x300")
    Label(root,text="Welcome to Log-In Protal",font=("times new roman", 20, "bold"),bg="#142966",fg="WHITE",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Log-IN",width="8",height="1",bg="#E6E600",font=("times new roman", 20, "bold"),command=login).pack()


    Label(root,text="").pack()
    Label(root,text="Developed By Nisha & Mansi").pack()
main_screen()
root.mainloop()