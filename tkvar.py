import tkinter as tk
from tkinter import ttk
def button_click():
    print("button clicked")

root  =tk.Tk()
root.title('Buttons')
root.geometry('800x400')
root.iconbitmap('mars.ico')
root.resizable(True,True)

table=ttk.Treeview(root)
table.pack()
table.place(x=150,y=50)

def button_fun(n1,n2):
    sum= n1+n2
    answer.set(f'answer is {sum}')



num1=tk.IntVar()
num2=tk.IntVar()
answer =tk.StringVar()

entry1=tk.Entry(root , textvariable=num1)
entry1.pack()
entry1.place(x=10,y=10)


entry2=tk.Entry(root , textvariable= num2)
entry2.pack()
entry2.place(x=10,y=30)


button=ttk.Button(root, text="Click", command=lambda:button_fun(num1.get(), num2.get()))
button.pack()
button.place(x=10,y=70)


label=ttk.Label(root, textvariable=answer)
label.pack()
label.place(x=10,y=100)




root.mainloop()