
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_btn():
    web = website_entry.get()
    eml = email_user_entry.get()
    pswd = password_entry.get()

    if web == "" or pswd == "":
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        save(web, eml, pswd)
        print(f"{web} , {eml} , {pswd}")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

def save(website, email,  password):
    with open('file.txt', 'a') as f:
        f.write(f"{website} | {email} | {password}\n")
    messagebox.showinfo(message="Password Saved Successfully")






    # create function called save
    # add button command that appends the data to the end of a text file as a newline, clears the text


# ---------------------------- UI SETUP ------------------------------- #
window = Style()
window.configure("Password Manager", foreground='black', background='white')
# window.config(padx=20, pady=20, background='white')

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

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_btn)
add_button.grid(column=1, row=4, columnspan=2)




mainloop()
