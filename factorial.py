from tkinter import*
import math

root = Tk()
root.title("Factorial finder")
root.geometry("600x200")
root.config(bg = "#181818")

def find():
    num = var.get()
    num = int(num)
    n = math.factorial(num)
    n = str(n)
    num = str(num)
    txt = "Factorial of "+ num + " is = " + n
    lbl3.config(text=txt)
lbl1 = Label(root,text = "Factorial Finder",bg = "#181818",fg = "#9abecc",font = "verdana 16 ",pady = 5).pack()
lbl2 = Label(root,text = "Enter Number  -",bg = "#181818",fg = "#2888ff",font = "verdana 16 ").place(x = 10,y = 50)

var = StringVar()
ent1 = Entry(root,bg = "#1f1f1f",fg = "white",font = "verdana 16 ",width=14,textvariable=var).place(x = 200,y = 50)

btn1 = Button(root,text = "Find",bg = "#181818",fg = "#2888ff",font = "verdana 16 ",command=find).place(x = 170,y = 90)

lbl3 = Label(root,text = "",bg = "#181818",fg = "#2888ff",font = "verdana 16 ")
lbl3.place(x = 10,y = 160)

root.mainloop()
