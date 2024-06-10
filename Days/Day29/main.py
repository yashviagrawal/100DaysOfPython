import json
from tkinter import *
import secrets
import string
import pyperclip
from tkinter import messagebox
import json

WHITE = "#ffffff"
BLACK = "#000000"


# ------------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_entry.delete(0, END)
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ------------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    website = get_website()
    username = get_username()
    password = get_password()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }
    if website == "" or username == "" or password =="":
        messagebox.showerror(title="ERROR", message="Empty fields found")
        is_okay = False
    else:
        is_okay = True
        # is_okay = messagebox.askokcancel(title=website,
        #                                  message=f"These are the details entered:\n"
        #                                          f"Email:{username}\n"
        #                                          f"Password: {password}\n"
        #                                          f"Is it okay to save?")
    # final = f"{website}, {username}, {password}\n"
    if is_okay:
# to store in txt
        # try:
        #     file = open("pass.txt", "a")
        # except FileNotFoundError:
        #     raise FileNotFoundError("database file was not found")
        #     file = open("pass.txt", "w")
        # else:
        #     pass
        # finally:
        #     file.write(final)
        #     file.close()
        #     website_entry.delete(0, END)
        #     password_entry.delete(0, END)
        try:
            data_file = open("data.json", "r")
        except FileNotFoundError:
            data_file = open("data.json", "w")
            data_file.close()
            data_file = open("data.json", "r")
        finally:
            # loading old content in a dictionary variable
            try:
                data = json.load(data_file)
            except json.decoder.JSONDecodeError:
                data_file = open("data.json", "w")
                json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                data_file.close()
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


        # with open("data.json", "w") as data_file:
        #     # saving data to data.json
        #     json.dump(data, data_file, indent=4)
        #     # deleting entries
        #     website_entry.delete(0, END)
        #     password_entry.delete(0, END)

def get_website():
    return website_entry.get()

def get_username():
    return username_entry.get()

def get_password():
    return password_entry.get()

# ------------------------------- SEARCH DATA ------------------------------- #
def search_data():
    website = get_website()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            pass
        messagebox.showerror(title="Not Found", message="There is no such website on the database")
    else:
        try:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        except KeyError:
            messagebox.showerror(title="Not Found", message="There is no such website on the database")
    finally:
        website_entry.delete(0, END)


# ------------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg=WHITE, padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg=WHITE, fg=BLACK, pady=10)
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", command=search_data)
search_button.grid(row=1, column=2)


username_label = Label(text="Email/Username: ", bg=WHITE, fg=BLACK, pady=10)
username_label.grid(row=2, column=0)

username_entry = Entry(width=30)
username_entry.insert(END, string="hirak214@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ", bg=WHITE, fg=BLACK, pady=20)
password_label.grid(row=3, column=0)

password_entry = Entry()
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate", command=generate_pass)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add_pass)
add_button.grid(row=4, column=1)

window.mainloop()
