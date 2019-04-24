import tkinter as tk 
from tkinter import Message ,Text
import tkinter.ttk as ttk
import tkinter.font as font
import csv
import os
import tkinter.messagebox as tm
window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Detail")
window.configure(background='light blue')
window.geometry("900x500")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

def logout():
    window.destroy()
    os.system("main.py")


message = tk.Label(window, text="MCA DETAIL       " ,bg="light blue"  ,fg="blue"  ,width=40  ,height=2,font=('times', 30, 'italic bold ')) 

message.place(x=0, y=40)
lg= tk.Button(window, text="Logout", command=logout ,fg="white"  ,bg="#4B4F4C"  ,width=10, activebackground = "red" ,font=('times', 10, ' bold '))
lg.place(x=650, y=80)
names1=["Id","Semester 1","Semester 2","Semester 3","Semester 4"]
var0= []
for num in range(5):
    
    lbl= tk.Label(window, text=names1[num],width=20  ,height=1  ,fg="white"  ,bg="grey" ,font=('times', 15, ' bold ') )
    lbl.place(x=200, y=150+(num*30))

    textbox = tk.Entry(window,width=15  ,bg="white" ,font=('times', 15, ' bold '))
    textbox.place(x=500, y=150+(num*30))
    #textbox.grid(row=4+x, column=0)
    var0.append(textbox)

def dataentry():
    data = []
    for num in range(5):
        
        val=var0[num].get()
        if(val!=None):
            data.append(val)
            var0[num].delete(0, 'end')  
    
    with open('mca.csv','a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(data)
    csvFile.close()
    tm.showinfo("Message", "Successful")
    #os.system("main.py")

takedata = tk.Button(window, text="Save", command=dataentry ,fg="white"  ,bg="#4B4F4C"  ,width=10  ,height=1, activebackground = "blue" ,font=('times', 15, ' bold '))
takedata.place(x=450, y=350)

window.mainloop()

