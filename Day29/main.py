from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("Generating password")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END) # delete the old password if entered
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    print("Saving password")
    webside = webside_input.get()
    password = password_input.get()
    username = username_input.get()

    if len(webside) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox_output = messagebox.askokcancel(webside, message=f"These are the details entered: \nUsername/Email:{username} \nPassword:{password}\n Is it ok to save?")
        if messagebox_output:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{webside} | {username} | {password}\n")
            # deleting from entries
            webside_input.delete(0, END)
            password_input.delete(0, END)
            username_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

# DEBUG: Function that colors the background of cells so you can see the borders
def debug_grid(widget):
    widget.config(highlightbackground="red", highlightthickness=1)

canvas_width = 200
canvas_height = 200
canvas = Canvas(width=canvas_width, height=canvas_height, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(canvas_width/2, canvas_height/2, image=logo_img )
canvas.grid(row=0, column=1)
# debug_grid(canvas) # visualization of how cell border

# Website
webside_label = Label(text="Website:")
webside_label.grid(row=1, column=0, sticky="e") # Added 'sticky=e', to align right
webside_input = Entry(width=51)
webside_input.focus()
webside_input.grid(row=1, column=1, columnspan=2, sticky="w")
# debug_grid(webside_input)

# Username
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="e")
username_input = Entry(width=51)
username_input.grid(row=2, column=1, columnspan=2, sticky="w")
# debug_grid(username_input)

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")
password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky="w")
# debug_grid(password_input)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="w")
# debug_grid(generate_password_button)

# Add Button
add_button = Button(text="Add", command=save_password, width=38)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")
# debug_grid(add_button)

window.mainloop()