from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    pswrd_entry.insert(0, password) # this will fill the password field with the randomly generated password
    pyperclip.copy(password) # this automatically copies the generated password to your clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    a = website_entry.get()
    b = email_usrnm_entry.get()
    c = pswrd_entry.get()

    if len(a) == 0 or len(b) == 0 or len(c) == 0:
        messagebox.showinfo(title = "Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=a, message=f"These are the details entered: \n Email: {b} \n Password: {c} "
                                                f"\n Is it okay to save?")
        if is_ok:
            with open("data.txt", mode="a") as login_data:
                login_data.write(a + " | " + b + " | " + c + "\n")
            website_entry.delete(0, END)
            pswrd_entry.delete(0, END)



#    file.write("New text.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg="#FCFCFC")


canvas = Canvas(width=300, height=300, bg="#FCFCFC", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(200, 150, image=lock_img)
canvas.grid()

#Labels
website_label = Label(text="Website:", bg="#FCFCFC")
website_label.grid(column=0, row=1, sticky=W)

email_usrnm_lable = Label(text="Email/Username:",bg="#FCFCFC")
email_usrnm_lable.grid(column=0, row=2, sticky=W)

pswrd_label = Label(text="Password:",bg="#FCFCFC")
pswrd_label.grid(column=0, row=3, sticky=W)

# Input Boxes
website_entry = Entry(width=25)
website_entry.grid(row=1, column=0, columnspan=2)
website_entry.focus()

email_usrnm_entry = Entry(width=25)
email_usrnm_entry.grid(row=2, column=0, columnspan=2)
email_usrnm_entry.insert(0,"dummy_email@gmail.com")

pswrd_entry = Entry(width=21)
pswrd_entry.grid(row=3, column=0)

# Buttons

gen_pswd_button = Button(text="Generate Password", command=generate_password)
gen_pswd_button.grid(column=1, row=3)

add_button = Button(text="Add", command=save)
add_button.grid(column=0, row=4)

window.mainloop()