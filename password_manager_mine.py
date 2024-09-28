
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for char in range(random.randint(8, 10))]

    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]

    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]


    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_btn():
    web = website_entry.get()
    eml = email_user_entry.get()
    pswd = password_entry.get()

    if len(web) == 0 or len(pswd) == 0:
        messagebox.showwarning(title="OOPS!", message="Please don't leave any fields empty!")
    else:
        save(web, eml, pswd)
        print(f"{web} , {eml} , {pswd}")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

def save(website, email,  password):
    with open('file.txt', 'a') as f:
        f.write(f"{website} | {email} | {password}\n")
    messagebox.showinfo(title="Success", message="Password Saved Successfully")



# ---------------------------- UI SETUP ------------------------------- #
window = Style()
window.configure("Password Manager", foreground='black', background='white')


canvas = Canvas(background='white', width=200, height=200, highlightthickness=0)
canvas.grid(column=1, row=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100,image=logo)

website_label = Label(text='Website:',background='black', foreground='white')
website_label.grid(column=0, row=1)
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_user_label = Label(text="Email / Username:")
email_user_label.grid(column=0, row=2)
email_user_entry = Entry(width=39)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, 'alexkharrod@gmail.com')

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_btn)
add_button.grid(column=1, row=4, columnspan=2)


mainloop()