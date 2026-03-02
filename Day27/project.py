# Miles to Km converter
# UI build with TKinter


from tkinter import *


def calculate_clicked():
   miles = float(miles_input.get())
   km = round(miles * 1.60934, 2)  # round to 2 digits
   converted_value_label.config(text=km)


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=400, height=400)


my_font = ("Arial", 16 )

miles_input=Entry()
miles_input.grid(row=0, column=1)


miles_label=Label(text="miles", font=my_font)
miles_label.grid(row=0, column=2)

is_equal_label=Label(text="is equal to", font=my_font)
is_equal_label.grid(row=1, column=0)

converted_value_label=Label(text="0", font=my_font)
converted_value_label.grid(row=1, column=1)

km_label=Label(text="Km", font=my_font)
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", font=my_font, command=calculate_clicked)
calculate_button.grid(row=2, column=1)

window.mainloop()