from tkinter import *

window = Tk()

window.title("First Program") # adding title
window.geometry("500x500") # adding dimensions
window.config(bg="yellow") # adding background color

frame1 = Frame(window, width=100, height=100, cursor="heart")
frame1.pack() #by default it is on top position

frame2 = Frame(window, width=100, height=100, cursor="dot")
frame2.pack(side=BOTTOM)

# How to create buttons?
# Adding button1 and 2 to frame1 and button3 to frame2
button1 = Button(frame1, text="Button1", bg="red", command= lambda: print("Button 1 clicked"))
button1.pack(side=LEFT)
button2 = Button(frame1, text="click me", bg="green", fg="white", command=lambda: print("click me clicked"))
button2.pack(side=RIGHT)

button3 = Button(frame2, text="Button2", bg="blue", command=lambda: print("Button 3 clicked"))
button3.pack(side=LEFT)

window.mainloop()
