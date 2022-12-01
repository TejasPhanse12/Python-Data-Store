from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk

root = Tk()
root.geometry("550x600")
root.title("Registration Form")
root.iconbitmap('D:\clg stuff\python prog\internship\peep.ico')

label0 = Label(root, text="Registration form",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 20 bold")
label0.place(x=150,y=20)

label_1 = Label(root, text="Enter Name:",width=20,fg='Black',font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root) #text field
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Enter Number:",width=20,fg='Black',font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root) #text field
entry_2.place(x=240,y=180)

label_3 = Label(root, text="View Your Information",font=("bold", 10)).place(x=98,y=250)

text1 = Text(root, height=10, width=50)
text1.grid(row=5, columnspan=4)
text1.place(x=98, y=270)

def process():
	check = open('register.txt', 'a')
	check1 = open('register.txt', 'r')
	
	name = str(entry_1.get()) # to retrive data from the user from text box
	number = str(entry_2.get()) 
	
	for char in number:
		b = char.isalpha() #this returns a bool value
		if(b == True):
			break 
	
	if len(number) == 10:
		test = check1.read()
		if number in test:
			mb.showwarning("Caution", "number already exists")
			entry_1.delete(0, tk.END)
			entry_2.delete(0, tk.END)
		elif (b == True):
			mb.showwarning("Caution", "number invalid number format")
			entry_1.delete(0, tk.END)
			entry_2.delete(0, tk.END)
		elif (name == ""):
			mb.showwarning("Caution", "Name is not mentioned")
			entry_1.delete(0, tk.END)
			entry_2.delete(0, tk.END)
		else:
			check.write(name)
			check.write("\t")
			check.write(number)
			check.write("\n")
			mb.showinfo("Info", "number is saved")
				
	elif number == str(number):
		mb.showwarning("Danger", "Enter the correct information")
			
	entry_1.delete(0, tk.END)
	entry_2.delete(0, tk.END)

	
	
def checking():
	check = open('register.txt', 'r')
	rest = check.read()
	for a in rest[::-1]:
		text1.insert(0.0, a)

def clearing():
	text1.delete(0.0, END)
	
insert = Button(root, text='Insert',width=20,bg='brown',fg='white', command=process)
insert.place(x=168,y=210)

check = Button(root, text="Check", width=10, command=checking)
check.grid(row=6, column=2)
check.place(x=360, y=450)

clear = Button(root, text="Clear", width=10, command=clearing)
clear.grid(row=6, column=3)
clear.place(x=450, y=450)

root.mainloop()