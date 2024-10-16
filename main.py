import os
import subprocess
import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)
    subprocess.Popen(['notify-send', password])

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_data = input_website.get()
    email_data = input_email.get()
    password_data = input_password.get()
    if website_data != '' and password_data != '':
        question = f"Entered values:\nSite: {website_data}\nEmail: {email_data}\nPassword: {password_data}\nIt's ok to save?";
        is_ok = messagebox.askyesno(website_data, question)
        if is_ok:
            str = f"{website_data} | {email_data} | {password_data}\n"
            with open('data.txt', 'a') as file:
                file.write(str)
            input_website.delete(0, END)
            input_email.delete(0, END)
            input_password.delete(0, END)
            #close window
            window.destroy()
    else:
        messagebox.showerror('Error message', 'All fields are requried')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white', highlightthickness=0)

# Use Pillow to open the PNG image with transparency
logo_img = Image.open('logo.png')
logo_img = ImageTk.PhotoImage(logo_img)  # Convert to a format Tkinter can use

width, height = logo_img.width(), logo_img.height()

canvas = Canvas(window, height=height, width=width, bg='white', highlightthickness=0)
canvas.create_image(0, 0, image=logo_img, anchor=NW)
canvas.grid(row=0, column=1)

#labels
label_website = Label(text="Timer", bg="white", font=(FONT_NAME, 12, "bold"))
label_website.grid(row=1, column=0)

input_website = Entry(window, width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

label_email = Label(text="Email/Username", bg="white", font=(FONT_NAME, 12, "bold"))
label_email.grid(row=2, column=0)

input_email = Entry(window, width=35)
input_email.grid(row=2, column=1, columnspan=2)

label_password = Label(text="Password", bg="white", font=(FONT_NAME, 12, "bold"))
label_password.grid(row=3, column=0)

input_password = Entry(window, width=27)
input_password.grid(row=3, column=1)

button_generate_password = Button(text="Gen", highlightthickness=0, command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=33, highlightthickness=0, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
