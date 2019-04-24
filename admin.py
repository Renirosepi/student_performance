import tkinter as tk 
from tkinter import Message ,Text
import tkinter.ttk as ttk
import tkinter.font as font
import matplotlib.pyplot as plt
import csv
import os
import pandas as pd
import tkinter.messagebox as tm

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Admin Panel")
window.configure(background='light blue')
window.geometry("1000x720")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

def logout():
    window.destroy()
    os.system("main.py")

message = tk.Label(window, text="ADMIN " ,bg="light blue"  ,fg="blue"  ,width=40  ,height=2,font=('times', 30, 'italic bold ')) 

message.place(x=0, y=40)
lg= tk.Button(window, text="Logout", command=logout ,fg="white"  ,bg="#4B4F4C"  ,width=10, activebackground = "red" ,font=('times', 10, ' bold '))
lg.place(x=750, y=80)

b1 = tk.Button(window, text="Perform", command="" ,fg="white"  ,bg="#4B4F4C"  ,width=50  ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
b1.place(x=100, y=150)
#b2 = tk.Button(window, text="Graph", command=dataentry ,fg="white"  ,bg="#4B4F4C"  ,width=10  ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
#b2.place(x=400, y=600)
#b3 = tk.Button(window, text="Save", command=dataentry ,fg="white"  ,bg="#4B4F4C"  ,width=10  ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
#b3.place(x=400, y=600)
    
lbl= tk.Label(window, text="Student Details",width=20  ,height=1  ,fg="blue"  ,bg="light blue" ,font=('times', 25, ' bold ') )
lbl.place(x=50, y=250)
lb2= tk.Label(window, text="Student Id",width=15  ,bg="light blue" ,font=('times', 15, ' bold ') )
lb2.place(x=50, y=300)
textbox = tk.Entry(window,width=15  ,bg="white" ,font=('times', 15, ' bold '))
textbox.place(x=250, y=300)

lb2= tk.Label(window, text="Performance Graph",width=15 ,fg="blue" ,bg="light blue" ,font=('times', 18, ' bold ') )
lb2.place(x=50, y=450)

def get_info():
    value=textbox.get()
    df = pd.read_csv('ds.csv',usecols=['id','name', 'sslc', 'plustwo', 'ug', 'pg_cgpa'])
    df1 = df.loc[df['id'] ==value]
    s_name=df1['name'].values[0]
    s_sslc=int(df1['sslc'])
    s_plustwo=int(df1['plustwo'])
    s_ug=int(df1['ug'])
    s_pg=int(df1['pg_cgpa'])
    x=['sslc','plustwo','ug','mca']
    y=[s_sslc,s_plustwo,s_ug,s_pg]
    plt.plot(x,y)
    plt.ylabel('percentage',fontsize=10)
    plt.xlabel('education level',fontsize=10)
    title_string = "Academic Performance"
    subtitle_string = "Student : "+s_name
    plt.suptitle(title_string, fontsize=20,color='r')
    plt.title(subtitle_string,fontsize=10)
    plt.show()
def get_mca():
    value=textbox.get()
    df = pd.read_csv('ds.csv',usecols=['id','name'])
    df1 = df.loc[df['id'] ==value]
    s_name=df1['name'].values[0]
    dff = pd.read_csv('mca.csv')
    dff1 = dff.loc[dff['id'] ==value]
    sem1=int(dff1['1sem'])
    sem2=int(dff1['2sem'])
    sem3=int(dff1['3sem'])
    sem4=int(dff1['4sem'])
    if sem2==0:
        x=['sem1']
        y=[sem1]
        plt.plot(x,y,'ro')
    elif sem3==0:
        x=['sem1','sem2']
        y=[sem1,sem2]
        plt.plot(x,y)
    elif sem4==0:
        x=['sem1','sem2','sem3']
        y=[sem1,sem2,sem3]
        plt.plot(x,y)
    else:
        x=['sem1','sem2','sem3','sem4']
        y=[sem1,sem2,sem3,sem4]
        plt.plot(x,y)
    plt.ylabel('percentage',fontsize=10)
    plt.xlabel('semester',fontsize=10)
    title_string = "MCA Performance"
    subtitle_string = "Student : "+s_name
    plt.suptitle(title_string, fontsize=20,color='r')
    plt.title(subtitle_string,fontsize=10)
    plt.show()
    
def get_class():
    value=textbox.get()
    df = pd.read_csv('ds.csv',usecols=['id','final_grade'])
    df1 = df.loc[df['id'] ==value]
    cls=df1['final_grade'].values[0]
    cls="Student Performance : "+cls
    lb3= tk.Label(window, text=cls,width=30  ,fg="red"  ,bg="light blue" ,font=('times', 20, ' bold ') )
    lb3.place(x=50, y=375)
    

search = tk.Button(window, text="Predict", command=get_class ,fg="white"  ,bg="#4B4F4C"  ,width=10, activebackground = "yellow" ,font=('times', 15, ' bold '))
search.place(x=450, y=300)
info = tk.Button(window, text="Academic", command=get_info ,fg="white"  ,bg="#4B4F4C"  ,width=10  , activebackground = "yellow" ,font=('times', 15, ' bold '))
info.place(x=300, y=450)
info = tk.Button(window, text="MCA", command=get_mca ,fg="white"  ,bg="#4B4F4C"  ,width=10  , activebackground = "yellow" ,font=('times', 15, ' bold '))
info.place(x=450, y=450)




    

window.mainloop()

