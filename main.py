from tkinter import *
from PIL import Image, ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='white', highlightthickness=0)

# Use Pillow to open the PNG image with transparency
logo_img = Image.open('logo.png')
logo_img = ImageTk.PhotoImage(logo_img)  # Convert to a format Tkinter can use

width, height = logo_img.width(), logo_img.height()

canvas = Canvas(window, height=height, width=width, bg='white', highlightthickness=0)
canvas.create_image(0, 0, image=logo_img, anchor=NW)
canvas.pack()

window.mainloop()
