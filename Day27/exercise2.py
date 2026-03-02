# Working with layouts
# Tkinter features three main geometry managers: Pack, Place, and Grid.
# Pack: Organizes widgets in blocks before placing them in the parent widget.
# Place: Allows precise positioning by defining absolute or relative x and y coordinates.
# Grid: Organizes widgets in a 2D table-like structure using rows and columns.

from tkinter import *
window = Tk()
window.title("My second GUI program - layouts")
window.minsize(width=400, height=400)

def button_clicked():
   print("I got clicked")
   new_text = entry.get()
   my_label.config(text=new_text) #my_label["text"] = new_text


my_label=Label(text="My label", font=("Arial", 18, "bold"))
my_label.place(x=10, y=50)

my_button = Button(text="Click to change label", command=button_clicked)
my_button.grid(column=0, row=1)

entry = Entry()
entry.grid(column=1, row=2)


window.mainloop()