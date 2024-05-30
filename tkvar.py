import tkinter as tk
from tkinter import ttk
def button_click():
    print("button clicked")

root  =tk.Tk()
root.title('Buttons')
root.geometry('300x200')
root.iconbitmap('mars.ico')

def button_fun(n1,n3):
    sum= n1+n3
    answer.set(f'answer is {sum}')



num1=tk.IntVar()
num2=tk.IntVar()
answer =tk.StringVar()

entry1=tk.Entry(root , textvariable=num1)
entry1.pack()

entry2=tk.Entry(root , textvariable= num2)
entry2.pack()


button=ttk.Button(root, text="Click", command=lambda:button_fun(num1.get(), num2.get()))
button.pack()
button.place(x=100,y=50)


label=ttk.Label(root, textvariable=answer)
label.pack()
label.place(x=10,y=10)




root.mainloop()