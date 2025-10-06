from tkinter import *

window = Tk()

window.geometry("500x500")

button = Button(window, text="Click on me", width = 20)
button.place(x=25, y = 100)

window.mainloop()