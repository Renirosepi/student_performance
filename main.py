from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
import mysql.connector
import os
from tkinter import messagebox
#import ynot

mydb = mysql.connector.connect(
 host="localhost",
user="root",
passwd="",
database="project"
)
cursor = mydb.cursor()
root = tk.Tk()
root.geometry("700x400")
root.configure(background='light blue')
root.title("Login")

def user_home():
        
    username = entry_username.get()
    password = entry_password.get()
    sql1 = "SELECT * FROM tb_login WHERE user_name = %s and password=%s"
    login = (username,password,)
    cursor.execute(sql1, login)
    result = cursor.fetchall()
    validate=len(result)
    if validate==1:
        for x in result:
            user_id=x[0]
            pw=x[1]
        if(user_id=="admin"):
            root.destroy()
            os.system("admin.py")
                
        else:
            root.destroy()
            os.system("student.py")
                
            
    else:
        tm.showerror("Login error", "Incorrect details")
            
   

def user_register():
    root.destroy()
    os.system("register.py")


label = Label(root, text="LOGIN",bg="light blue"  ,fg="blue"  ,width=20  ,height=2,font=('times', 30, 'italic bold '))
label_username = Label(root, text="Username",width=15  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold '))
label_password = Label(root, text="Password",width=15  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold '))

entry_username = Entry(root,width=15  ,bg="white" ,font=('times', 15, ' bold '))
entry_password = Entry(root, show="*",width=15  ,bg="white" ,font=('times', 15, ' bold '))
logbtn_user = Button(root, text="Login",
                                  command=user_home,fg="white"  ,bg="#4B4F4C"  ,width=10  ,height=1, activebackground = "blue" ,font=('times', 15, ' bold '))
regbtn_user = Button(root, text="New Register",
                                  command=user_register,fg="white"  ,bg="#4B4F4C"  ,width=10  ,height=1, activebackground = "blue" ,font=('times', 15, ' bold '))
       
        
label.grid(row=0,sticky=E)
label_username.grid(row=2, padx=10, pady=10)
label_password.grid(row=3, padx=10, pady=10)
entry_username.grid(row=2, column=1,padx=10, pady=10)
entry_password.grid(row=3, column=1,padx=10, pady=10)
logbtn_user.grid(row=4, columnspan=2,padx=10, pady=10)
regbtn_user.grid(row=4, columnspan=2,sticky=E,padx=10, pady=10)
#root.pack()

mainloop()
