from tkinter import *

window = Tk()

window.geometry("500x500")
window.title("My window")

label1 = Label(window, text="Label 1", bg="red", fg="white")
label2 = Label(window, text="Label 2", bg="green", fg="white")
label3 = Label(window, text="Label 3", bg="blue", fg="white")

label1.pack(side=TOP, fill=X, expand=False) # fill=X means fill horizontally, expand = False means create without any spaces for the widget
label2.pack(side=LEFT, fill=Y, expand=False) # fill=Y means fill vertivally
label3.pack(side=RIGHT, fill=Y, expand=True) # expand = True means it will leave some spaces for the widgets at the right side of the window

mainloop()