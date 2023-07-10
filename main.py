from tkinter import *
from tkinter import messagebox
from passgen import PassWord


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    new_pw = PassWord().pw_gen()
    pw_box.insert(END, new_pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    web_entry = web_box.get()
    user_entry = user_box.get()
    pw_entry = pw_box.get()
    if web_entry == "" or pw_entry == "" or user_entry == "":
        messagebox.showerror(title="ERROR", message="Incomplete section(s)")
    else:
        is_ok = messagebox.askokcancel(title=web_entry,
                                       message=f"These are the details entered: \nEmail: {user_entry} \nPassword: {pw_entry} \nOK to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{web_entry} | {user_entry} | {pw_entry}\n")
                web_box.delete(0, END)
                pw_box.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.config(padx=50, pady=50)
# screen.minsize(width=300, height=300)
screen.title("Password Manager")
# CANVAS
canvas = Canvas(width=200, height=200)
pw = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw)
canvas.grid(column=1, row=0)
# LABELS
web_lab = Label(text="Website:")
web_lab.grid(column=0, row=1)

user_name = Label(text="Email/Username:")
user_name.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)
# BUTTONS
gen_pw = Button(text="Generate Password", highlightthickness=0, command=gen_pw)
gen_pw.grid(column=2, row=3)

add_b = Button(text="Add", width=36, highlightthickness=0, command=save_pw)
# add_b.grid(column=1, row=4, columnspan=2)
add_b.place(x=145, y=270)
# ENTRIES
web_box = Entry(width=35)
web_box.grid(column=1, row=1, columnspan=2)
web_box.focus()

user_box = Entry(width=35)
user_box.grid(column=1, row=2, columnspan=2)
user_box.insert(END, "myemail@email.com")  # pre-populated email

pw_box = Entry(width=24)
pw_box.place(x=145, y=248)
# pw_box.grid(column=1, row=3)
screen.mainloop()
