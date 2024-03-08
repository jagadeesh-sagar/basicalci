import tkinter as tk
from tkinter import messagebox
def addition():
  try:
    num1=int(number1.get())
    num2=int(number2.get())
    add=num1+num2
    result_label.config=tk.Label(root,text=f"The adddition of {num1},{num2} is{add}")
  except (TypeError,ValueError):
      messagebox.showerror("info","ERROR")
      messagebox.showinfo("info","enter nnumeric data types")
def subtraction():
   try:

    num1=int(number1.get())
    num2=int(number2.get())
    sub=num1-num2
    result_label.config=tk.Label(root,text=f"The subtraction of {num1},{num2} is{sub}")
   except (TypeError,ValueError):
      messagebox.showerror("info","ERROR")
      messagebox.showinfo("information","enter nnumeric data types")
def multplication():
  try:
    num1=int(number1.get())
    num2=int(number2.get())
    multi=num1*num2
    result_label.config=tk.Label(root,text=f"The multiplication of {num1},{num2} is{multi}")
  except (TypeError,ValueError):
      messagebox.showerror("information","ERROR")
      messagebox.showinfo("information","enter nnumeric data types")
def divison():
    try:
        num1=int(number1.get())
        num2=int(number2.get())
        div=num1/num2
        result_label.config=tk.Label(root,text=f"The division of {num1},{num2} is{div}")
    except (ZeroDivisionError,TypeError,ValueError):
         messagebox.showerror("info","Error.")
         messagebox.showinfo("info"," cant divide by using zero are any special symbols.")

root=tk.Tk()
root.title("calculator")
root.geometry("1400x900")

label1=tk.Label(root,text="Enter the first number:",font=("Times New Roman",12,"bold")).pack()
number1=tk.Entry(root)
number1.pack()

label2=tk.Label(root,text="Enter the second number:",font=("Times New Roman",12,"bold")).pack()
number2=tk.Entry(root)
number2.pack()

button1=tk.Button(root,text="addition",command=addition,fg="black")
button1.pack()
button2=tk.Button(root,text="subtraction",command=subtraction,fg="black")
button2.pack()
button3=tk.Button(root,text="multiplication",command=multplication,fg="black")
button3.pack()
button4=tk.Button(root,text="division",command=divison,fg="black")
button4.pack()
result_label=tk.Label(root,text="")
result_label.pack()
root.mainloop()
