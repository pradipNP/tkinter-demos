from tkinter import *

window = Tk()

# Create a menu bar (top-level menu container)
menu = Menu(window)

# Create a "File" submenu inside the menu bar
# tearoff=False removes the dashed line (which allows detaching menus in some systems)
file = Menu(menu, tearoff=0)

# Add menu items (commands) to the "File" menu
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")

# Add a horizontal separator line in the menu
file.add_separator()

# Add an "Exit" option that closes the window when clicked
file.add_command(label="Exit", command=window.quit)

# Attach the "File" submenu to the main menu bar with the label "File"
menu.add_cascade(label="File", menu=file)

# Attaching the menu bar into window / # Configure the window to use the created menu bar
window.config(menu=menu)

mainloop()