import tkinter as tk 
from tkinter import Message ,Text
import tkinter.ttk as ttk
import tkinter.font as font
import csv
import tkinter.messagebox as tm
import os
#import mysql.connector

#mydb = mysql.connector.connect(
 #host="localhost",
#user="root",
#passwd="",
#database="project"
#)
#cursor = mydb.cursor()

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Detail")
window.configure(background='light blue')
window.geometry("1000x720")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

def logout():
    window.destroy()
    os.system("main.py")


message = tk.Label(window, text="STUDENTS DETAIL       " ,bg="light blue"  ,fg="blue"  ,width=40  ,height=2,font=('times', 30, 'italic bold ')) 

message.place(x=0, y=40)
lg= tk.Button(window, text="Logout", command=logout ,fg="white"  ,bg="#4B4F4C"  ,width=10, activebackground = "red" ,font=('times', 10, ' bold '))
lg.place(x=750, y=80)
names1=["User Id","Name","Sslc %","PlusTwo %","UG%","PG cgpa","Practical %","Internal mark%","Attendance %","Intrested subject","Presented seminar topic ","Evaluate yourself as student","Work experience?","Project topic","Support alcohol?","Rate your health(5)","Usage of mobile(5)","Evaluate code ability(10)?","Knowledgr on subject(10)?","Weekly study time(3)?",  "Number of failure?","Have support of family?"]
var0= []
var1 = []
for num in range(11):
    
    lbl= tk.Label(window, text=names1[num],width=20  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold ') )
    lbl.place(x=50, y=150+(num*30))

    textbox = tk.Entry(window,width=15  ,bg="white" ,font=('times', 15, ' bold '))
    textbox.place(x=300, y=150+(num*30))
    #textbox.grid(row=4+x, column=0)
    var0.append(textbox)
for num in range(11):
    
    lbr= tk.Label(window, text=names1[num+11],width=20  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold ') )
    lbr.place(x=500, y=150+(num*30))

    textbox = tk.Entry(window,width=15  ,bg="white" ,font=('times', 15, ' bold '))
    textbox.place(x=750, y=150+(num*30))
    #textbox.grid(row=4+x, column=0)
    var1.append(textbox)

def mcadata():
    window.destroy()
    os.system("mca_detail.py")

def dataentry():
    data = []
    for num in range(11):
        
        val=var0[num].get()
        if(val!=None):
            data.append(val)
            var0[num].delete(0, 'end')  
    for num in range(11):
        val=var1[num].get()
        if(val!=None):
            data.append(val)
            var1[num].delete(0, 'end')
    
    '''with open('ds.csv','a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(data)
    csvFile.close()'''
    with open('test.csv','a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(data)
    csvFile.close()
    tm.showinfo("Message", "Successful")
    os.system("predict.py")
    
    #print(data)
    #sql2 = "INSERT INTO tb_student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #cursor.execute(sql2,data)
    #mydb.commit()
    #tm.showinfo("Message", "Saved")
    
    

takedata = tk.Button(window, text="Save", command=dataentry ,fg="white"  ,bg="#4B4F4C"  ,width=10  ,height=1, activebackground = "blue" ,font=('times', 15, ' bold '))
takedata.place(x=300, y=600)
takedata = tk.Button(window, text="Next", command=mcadata ,fg="white"  ,bg="#4B4F4C"  ,width=10  ,height=1, activebackground = "blue" ,font=('times', 15, ' bold '))
takedata.place(x=600, y=600)

window.mainloop()

