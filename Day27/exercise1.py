from tkinter import *
import tkinter

window = Tk()
window.title("My first GUI program")
window.minsize(width=400, height=400)

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


#Text entry (multiple lines)
text = Text(height=5, width=10)
text.focus()

#to get current value in textbox at line 1, character 0
print(text.get("1.0", END))

#SpinBox (text input for numbers)
def spinbox_used():
   #print out current value
   print(spinbox.get())

spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()

#Scale (slider)
def scale_used(scale_value):
   print(scale_value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#CheckBox
def checkbutton_used():
   print(checked_state.get())
checked_state = IntVar()
check_button = Checkbutton(text="Check", variable=checked_state, command=checkbutton_used)
check_button.pack()

#Radio button
def radio_used():
   print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="option 1", variable=radio_state, value=1, command=radio_used)
radiobutton2 = Radiobutton(text="option 2", variable=radio_state, value=2, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
   # Get current selection from listbox
   print(lb.get(lb.curselection()))

lb = Listbox(height=4)
positions = ["first", "second", "third", "fourth", "fifth"]
for item in positions:
   lb.insert(positions.index(item), item)

lb.bind("<<ListboxSelect>>", listbox_used)
lb.pack()

window.mainloop()