from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
FONT = "Courier 12"
STD_WIDTH = 24

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = user_entry.get()
    passtext = pass_entry.get()
    # json format
    new_data = {
        website: {
            "email": email,
            "password": passtext,
        }
    }

    if len(website) < 0 or len(passtext) < 8:
        messagebox.showwarning(
            title='Password Error', message="Password must be at least 8 characters long")
    else:
        try:
            with open('Projects/D29_password-manager/passwords.json', 'r') as data_file:
                # Loading(reading) existing data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('Projects/D29_password-manager/passwords.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            # Saving(writing) updated data
            with open('Projects/D29_password-manager/passwords.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()
            messagebox.showinfo(
                title="Success", message="Password Saved Successfully")

# -------------------------- SEARCH A PASSWORD --------------------------#


def search_pass():
    website = website_entry.get().capitalize()
    try:
        with open('Projects/D29_password-manager/passwords.json', 'r') as data_file:
        # Loading(reading) existing data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No DataFile found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(
                title="Details", message=f"email:{email}\n password:{password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"NO DATA FOR {website}")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.geometry('650x450')
window.config(padx=50, pady=50)

# Logo
logoicon=PhotoImage(file='Projects/D29_password-manager/logo.png')
canvas=Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logoicon)
canvas.grid(row=0, column=1)

# Website Field
website_label=Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

website_entry=Entry(width=22, font=FONT)
website_entry.grid(row=1, column=1)
website_entry.focus()

# Username Field
user_label=Label(text="Email/Username:", font=FONT)
user_label.grid(row=2, column=0)

user_entry=Entry(width=35, font=FONT)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(END, 'rogerdavid@aol.com')

# Password field
password=Label(text="Password:", font=FONT)
password.grid(row=3, column=0)

pass_entry=Entry(width=19, font=FONT)
pass_entry.grid(row=3, column=1)

# buttons
passgen_btn=Button(text="Generate Password",
                     activebackground='red', command=gen_password, font=FONT)
passgen_btn.grid(row=3, column=2)

passsave_btn=Button(text="Save Password", activebackground='black',
                      activeforeground='white', width=36, font=FONT, command=save_password)
passsave_btn.grid(row=4, column=1, columnspan=2)

search_pass_btn=Button(text="Search", activebackground='blue', activeforeground='white',
                         command=search_pass, font=FONT, width=15)
search_pass_btn.grid(row=1, column=2)

window.mainloop()
