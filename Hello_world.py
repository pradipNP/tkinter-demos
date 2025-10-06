# What is Tkinter?
"""
- Python's built-in GUI-package (don't need to install separately)
- Tells you how to create window, buttons, labels, textboxes, menus, etc.
"""

# Steps to use
"""
1. import tkinter as tk
2. GUI interaction
3. adding inputs
4. main loop
"""

#Step 1:
from tkinter import *

#Step 2:
window = Tk()

#Step 3:
inp = Label(window, text="Hello World")
inp.pack()
window.title("First Program") # adding title
window.geometry("500x400") # adding dimensions
window.config(bg="blue") # adding background color
inp.config(bg="red")  # adding background color of input text

#Step 4:
window.mainloop()
