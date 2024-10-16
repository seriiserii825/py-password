from tkinter import *
from PIL import Image, ImageTk

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

label_email = Label(text="Email/Username", bg="white", font=(FONT_NAME, 12, "bold"))
label_email.grid(row=2, column=0)

input_email = Entry(window, width=35)
input_email.grid(row=2, column=1, columnspan=2)

label_password = Label(text="Password", bg="white", font=(FONT_NAME, 12, "bold"))
label_password.grid(row=3, column=0)

input_password = Entry(window, width=27)
input_password.grid(row=3, column=1)

button_generate_password = Button(text="Gen", highlightthickness=0)
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=33, highlightthickness=0)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
