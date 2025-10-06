from tkinter import *

window = Tk()

window.title("Checkbutton")
window.geometry("500x500")

def button_clicked():
    print("You clicked the button")

button = Button(window, text="Click me", command = button_clicked, width=10, bg = "red", fg = "white", font = ("bold",12), activebackground="black", activeforeground="red" )
button.pack()

mainloop()