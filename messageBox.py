from tkinter import *
import tkinter.messagebox

window = Tk()

tkinter.messagebox.showerror("Info", "Running out time")
question = tkinter.messagebox.askyesno("weather", "Will it rain?")

if question == True:
    print("Take an umberlla")

else:
    print("Okay")

mainloop()