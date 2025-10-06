from tkinter import *

window = Tk()
window.geometry("500x500")

# method 1
"""
message = Message(window, text="Python", width=50)
message.pack()
"""

# method 2
"""
var = StringVar()
var.set("Welcome")
message = Message(window, width=50, textvariable= var, relief=RAISED, padx=3, pady=3)
message.pack()
"""

# method 3
var = StringVar()
ent_var = StringVar()

def insert():
    result = ent_var.get()
    var.set(result)

message = Message(window, textvariable= var, relief=RAISED, padx=50, pady=50)
message.pack()
#creating entry box
entry = Entry(window, textvariable= ent_var)
entry.pack()
#creating button
button = Button(window, text="OK", command=insert)
button.pack()

mainloop()