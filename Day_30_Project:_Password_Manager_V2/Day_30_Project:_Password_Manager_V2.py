from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------------- SEARCH ------------------------------------- #
def find_password():
    try:
        with open("password_manager_data.json", "r") as pass_data:
            data = json.load(pass_data)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found!")
    else:
        website = website_entry.get()
        email_or_username = email_or_username_entry.get()
        if website != "" and email_or_username != "":
            if website in data:
                if data[website]["email/username"] == email_or_username:
                    messagebox.showinfo(title="Password Manager", message=f'Website: {website} \nEmail: {email_or_username} \nPassword: {data[website]["password"]}')
                else:
                    messagebox.showerror(title="Oops", message="You typed your Email/Username wrong!")
            else:
                messagebox.showerror(title="Oops", message="You typed website name wrong or you have never added an account on this website!")
        else:
            messagebox.showerror(title="Oops", message="You have to fill both Website and Email/Username entryes to get your password!")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_or_username = email_or_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email/username": email_or_username,
            "password": password
        }
    }

    if website != "" and email_or_username != "" and password != "":
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"These are the details entered: \nWebsite: {website} \nEmail: {email_or_username} \nPassword: {password} \n is it ok to save?")
        if is_ok:
            try:
                with open("password_manager_data.json", "r") as pass_data:
                    data = json.load(pass_data)
            except FileNotFoundError:
                with open("password_manager_data.json", "w") as pass_data:
                    json.dump(new_data, pass_data, indent=4)
            else:
                data.update(new_data)
                with open("password_manager_data.json", "w") as pass_data:
                    json.dump(data, pass_data, indent=4)
            finally:
                website_entry.delete(0, END)
                email_or_username_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager By Emivvvvv")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_or_username_label = Label(text="Email/Username:")
email_or_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_or_username_entry = Entry(width=38)
email_or_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


window.mainloop()
