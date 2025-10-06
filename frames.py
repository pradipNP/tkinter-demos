from tkinter import *

window = Tk()

window.title("First Program") # adding title
window.geometry("500x400") # adding dimensions
window.config(bg="yellow") # adding background color

#How to create frame?
frame1 = Frame(window, bg="red", width=100, height=100, cursor="heart")
frame1.pack() #by default it is on top position

frame2 = Frame(window, bg="green", width=100, height=100, cursor="dot")
frame2.pack(side=BOTTOM)


window.mainloop()
