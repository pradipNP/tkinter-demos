from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("500x500")

# Creating Entry Box
e = Entry(window, width=39, borderwidth=5)
e.place(x=0, y=0)

def click(number):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(number))

# Adding Buttons
b = Button(window, text="1", width=10, command=lambda: click(1))
b.place(x=0, y=40)

b = Button(window, text="2", width=10, command=lambda: click(2))
b.place(x=80, y=40)

b = Button(window, text="3", width=10, command=lambda: click(3))
b.place(x=160, y=40)

b = Button(window, text="4", width=10, command=lambda: click(4))
b.place(x=0, y=70)

b = Button(window, text="5", width=10, command=lambda: click(5))
b.place(x=80, y=70)

b = Button(window, text="6", width=10, command=lambda: click(6))
b.place(x=160, y=70)

b = Button(window, text="7", width=10, command=lambda: click(7))
b.place(x=0, y=100)

b = Button(window, text="8", width=10, command=lambda: click(8))
b.place(x=80, y=100)

b = Button(window, text="9", width=10, command=lambda: click(9))
b.place(x=160, y=100)

b = Button(window, text="0", width=10, command=lambda: click(0))
b.place(x=0, y=130)


def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="+", width=10, command=add)
b.place(x=80, y=130)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="-", width=10, command=sub)
b.place(x=160, y=130)

def mul():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="*", width=10, command=mul)
b.place(x=0, y=160)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="/", width=10, command=div)
b.place(x=80, y=160)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))

b = Button(window, text="=", width=10, command=equal)
b.place(x=160, y=160)
b.place(x=160, y=160)

def clear():
    e.delete(0, END)

b = Button(window, text="clear", width=10, command=clear)
b.place(x=0, y=190)

mainloop()