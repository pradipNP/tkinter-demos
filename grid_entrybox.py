from tkinter import *
window = Tk()

window.title("Login Window")
window.geometry("300x300")

# Creating labels and setting location on the window via grid()
label1 = Label(window, text= "mail:")
label1.grid(row=0, column=0)
label2 = Label(window, text="password:")
label2.grid(row=1, column=0)

# Creating EntryBox for both frames & managing required location
e1 = Entry(window, width=40, borderwidth=4)
e1.grid(row=0, column=1)
e2 = Entry(window, width=40)
e2.grid(row=1, column=1)


window.mainloop()