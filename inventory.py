from tkinter import*
from tkinter import messagebox as ms
import tkinter as tk


root = Tk()
root.geometry('800x300')

def insert():
	
	file1 = open("D:\\clg stuff\\python prog\\internship\\file.txt","a")
	file2 = open("D:\\clg stuff\\python prog\\internship\\file.txt","r")
	p_id = str(Product_id.get())
	name = str(Product_Name.get())
	number = str(Selling_P.get())
	Q_n = str(Quantity.get())
	test = file2.read()
	
	qn=int(Q_n)
	
	if (name == ""):
		ms.showwarning("Caution", "Name is not mentioned")
		Product_id.delete(0,tk.END)
		Product_Name.delete(0,tk.END)
		Selling_P.delete(0,tk.END)
		Quantity.delete(0,tk.END)
	elif name in test:
		ms.showwarning("warning","Name already exist")
		Product_Name.delete(0,tk.END)
		Selling_P.delete(0,tk.END)
	
	elif p_id in test:
		for char in p_id:
			b = char.isalpha() 
			if(b == True):
				break 
		if (b == True):
			ms.showwarning("Caution", "number invalid number format for product id")
			Product_id.delete(0,tk.END)
			Product_Name.delete(0,tk.END)
			Selling_P.delete(0,tk.END)
			Quantity.delete(0,tk.END)
		else :
			ms.showwarning("warning","Number already exist")
			Product_Name.delete(0,tk.END)
			Selling_P.delete(0,tk.END)
	elif len(number) < 1:
		ms.showwarning("Caution", "Selling Price not mentioned")
		Product_id.delete(0,tk.END)
		Product_Name.delete(0,tk.END)
		Selling_P.delete(0,tk.END)
		Quantity.delete(0,tk.END)
	elif (qn <= 10):
		for char in p_id:
			b = char.isalpha() 
			if(b == True):
				break 
		if (b == True):
			ms.showwarning("Caution", "number invalid number format for product id")
			Product_id.delete(0,tk.END)
			Product_Name.delete(0,tk.END)
			Selling_P.delete(0,tk.END)
			Quantity.delete(0,tk.END)
		else:
			ms.showwarning("Caution", "too less quantity")
			Product_id.delete(0,tk.END)
			Product_Name.delete(0,tk.END)
			Selling_P.delete(0,tk.END)
			Quantity.delete(0,tk.END)
	
	else:
		file1.write("\t")
		file1.write(p_id)
		file1.write("\t")
		file1.write(name)
		file1.write("\t")
		file1.write("\t")
		file1.write(number)
		file1.write("\t")
		file1.write("\t")
		file1.write(Q_n)
		file1.write("\n")
		ms.showinfo("Info", "number is executed")		
           
	Product_id.delete(0,tk.END)
	Product_Name.delete(0,tk.END)
	Selling_P.delete(0,tk.END)
	Quantity.delete(0,tk.END)
	file1.close()
def check():
	run=0
	file1 = open("D:\\clg stuff\\python prog\\internship\\file.txt","r")
	for count in file1:
			run+=1
			Output.insert(INSERT,run)
			Output.insert(INSERT, count)			
	
	file1.close()
def clear():
    Output.delete(0.0,tk.END)
    
    
label_0 = LabelFrame(root, text=" Inventory Management",fg='blue',width=185,height=250,font=("bold",10))
label_0.place(x=65,y=20)

label_1 = Label(root, text="Product id:",width=20,font=("bold", 10))
label_1.place(x=68,y=50)

Product_id=Entry(root)
Product_id.place(x=90,y=70)

label_2 = Label(root, text="Product Name:",width=20,font=("bold", 10))
label_2.place(x=70,y=90)

Product_Name=Entry(root)
Product_Name.place(x=90,y=110)\

label_2 = Label(root, text="Selling price :",width=20,font=("bold", 10))
label_2.place(x=70,y=130)

Button(root, text='Insert',width=5,command = insert).place(x=90,y=210)

Selling_P=Entry(root)
Selling_P.place(x=90,y=150)

label_3 = Label(root, text="Quantity :",width=20,font=("bold", 10))
label_3.place(x=70,y=170)

Quantity=Entry(root)
Quantity.place(x=90,y=190)

label_3 = Label(root, text="Item no",width=20,font=("bold", 10))
label_3.place(x=225,y=60)

labelF = LabelFrame(root,text="Product List",fg='blue',width=530,height=250,font=("bold",10))
labelF.place(x=248,y=20)

Output = Text(root, height =12, width = 64) 
Output.place(x=255,y=60) 


A = Label(root, text="Iteam No.", width=15, 
          height=1, borderwidth=1, relief="ridge", anchor = 'w')
A.place(x=255,y=40)

B = Label(root, text="Product id", width=15, 
          height=1, borderwidth=1, relief="ridge", anchor = 'w')
B.place(x=360,y=40)

C = Label(root, text="Product Name", width=15, 
          height=1, borderwidth=1, relief="ridge", anchor = 'w')
C.place(x=460,y=40)

D = Label(root, text="Selling Price", width=15, 
          height=1, borderwidth=1, relief="ridge", anchor = 'w')
D.place(x=560,y=40)

E = Label(root, text="Quantity", width=15, 
          height=1, borderwidth=1, relief="ridge", anchor = 'w')
E.place(x=660,y=40)		  
	  
	
Button(root, text='show',width=5,command = check).place(x=150,y=210)

Button(root, text='Clear',width=5,bg='black',fg='white',command = clear).place(x=125,y=240)

root.mainloop()