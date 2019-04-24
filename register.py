from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import mysql.connector
import os
#import subprocess 
from tkinter import messagebox


mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="project"
)
cursor = mydb.cursor()
r = Tk()
r.geometry("700x400")
r.configure(background='light blue')
r.title("Registration")

def new_register():
    username = entry_username.get()
    password = entry_password.get()
    register = (username,password,)
    sql2 = "INSERT INTO tb_login  VALUES (%s,%s)"
    cursor.execute(sql2,register)
    mydb.commit()
    tm.showinfo("Message", "Successfully Registered")
    r.destroy()
    os.system("main.py")
    #subprocess.call('main.py',shell=True)

label = Label(r, text="REGISTERATION" ,bg="light blue"  ,fg="blue"  ,width=20  ,height=2,font=('times', 30, 'italic bold '))
label_username = Label(r, text="Username",width=15  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold '))
label_password = Label(r, text="Password",width=15  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold '))

entry_username = Entry(r,width=15  ,bg="white" ,font=('times', 15, ' bold '))
entry_password = Entry(r, show="*",width=15  ,bg="white" ,font=('times', 15, ' bold '))
regbtn_user = Button(r, text="Register",
                                  command=new_register,fg="white"  ,bg="#4B4F4C"  ,width=10  ,height=1, activebackground = "blue" ,font=('times', 15, ' bold '))
       
        
label.grid(row=0,sticky=E)
label_username.grid(row=2, padx=10, pady=10)
label_password.grid(row=3, padx=10, pady=10)
entry_username.grid(row=2, column=1,padx=10, pady=10)
entry_password.grid(row=3, column=1,padx=10, pady=10)
regbtn_user.grid(row=4, columnspan=2,padx=10, pady=10)


     
mainloop()

