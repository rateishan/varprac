import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root  =tk.Tk()
root.title('Buttons')
root.geometry('800x400')
root.iconbitmap('mars.ico')
root.resizable(True,True)

table=ttk.Treeview(root, columns=('num1', 'num2', 'answer'), show='headings')
table.heading('num1', text='Number1')
table.heading('num2', text='Number2')
table.heading('answer', text='Answer')
table.column('num1', anchor=tk.CENTER)
table.column('num2', anchor=tk.CENTER)
table.column('answer', anchor=tk.CENTER)
table.pack()
table.place(x=150,y=50)

num1=tk.IntVar()
num2=tk.IntVar()
answer =tk.StringVar()


def button_fun(n1,n2):
    sum= n1+n2
    answer.set(f'{sum}')


def entry_value():
        table.insert('', 'end', values=(num1.get(), num2.get(),answer.get()))
        num1.set('')
        num2.set('')

entry1=tk.Entry(root , textvariable=num1)
entry1.pack()
entry1.place(x=10,y=10)

entry2=tk.Entry(root , textvariable= num2)
entry2.pack()
entry2.place(x=10,y=30)

label=ttk.Label(root, textvariable=answer)
label.pack()
label.place(x=10,y=100)


button=ttk.Button(root, text="Click", command=lambda :button_fun[(num1.get(), num2.get()),entry_value()])
button.bind("<Return>",lambda event :entry_value())
button.pack()
button.place(x=10,y=70)


root.mainloop()
