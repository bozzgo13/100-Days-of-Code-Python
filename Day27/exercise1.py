from tkinter import *
import tkinter

window = Tk()
window.title("My first GUI program")
window.minsize(width=400, height=300)

#Label

#Label(window, text="My first GUI program").grid(row=0, column=0)
my_label=Label(text="My label", font=("Arial", 25, "bold"))
my_label.pack()

#Button

def button_clicked():
   print("I got clicked")
   new_text = input.get() 
   my_label.config(text=new_text) #my_label["text"] = new_text
   
my_button = Button(text="Click to change label", command=button_clicked)
my_button.pack()

#Entry (text input)
input = Entry()
input.pack()


window.mainloop()