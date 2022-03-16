from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pass_letters = [password_list.append(random.choice(letters)) for letter in range(nr_letters)]
    pass_symbols = [password_list.append(random.choice(symbols)) for symbol in range(nr_symbols)]
    pass_numbers = [password_list.append(random.choice(numbers)) for number in range(nr_numbers)]

    random.shuffle(password_list)

    new_password = "".join(password_list)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        no = messagebox.showerror(title="No", message="Please do not leave any fields empty")

    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                file_data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # Updating old data with new data
            file_data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(file_data, file, indent=4)

        finally:
            website_entry.delete(0, END)
            # email_username_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    email = email_username_entry.get()

    try:
        with open("data.json", "r") as file:
            file_data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in file_data:
            password = file_data[website]["password"]
            site_info = messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for this website available.")

# ---------------------------- UI SETUP ------------------------------- #


# Window

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.eval("tk::PlaceWindow . center")


# Entries

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.insert(0, "@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3, sticky="EW")


# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Buttons

search_button = Button(text="Search", width=10, highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

gen_password_button = Button(text="Generate", width=10, command=generate_password)
gen_password_button.grid(column=2, row=3, sticky="EW")

add_password_button = Button(text="Add", font=("Arial", 10), width=25, command=save)
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")


# Logo Canvas

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_art = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_art)
canvas.grid(column=1, row=0)


# Loop

window.mainloop()
