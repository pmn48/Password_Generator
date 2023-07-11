from tkinter import *
from tkinter import messagebox
from passgen import PassWord
import json as js


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    new_pw = PassWord().pw_gen()
    pw_box.insert(END, new_pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    web_entry = web_box.get()
    user_entry = user_box.get()
    pw_entry = pw_box.get()
    new_data = {
        web_entry: {
            "Email": user_entry, "Password": pw_entry
        }
    }
    if web_entry == "" or pw_entry == "" or user_entry == "":
        messagebox.showerror(title="Error", message="Incomplete section(s)")
    else:
        is_ok = messagebox.askokcancel(title=web_entry,
                                       message=f"These are the details entered: \nEmail: {user_entry} \nPassword: {pw_entry} \nOK to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    # reading old data
                    data = js.load(data_file)
                    # update old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                # Create a new data file and save the pw
                with open("data.json", mode="w") as data_file:
                    js.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", mode="w") as data_file:
                    # Save the updated data
                    js.dump(data, data_file, indent=4)
            finally:
                web_box.delete(0, END)
                pw_box.delete(0, END)


# ------------------------------SEARCH INFO----------------------------------#
def search_info():
    web_entry = web_box.get()
    if len(web_entry) == 0:
        messagebox.showerror(title="Error", message="Incomplete Website Section")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                content = js.load(data_file)
                line = ""
                for key, value in content[web_entry].items():
                    line += f"{key}: {value}\n"
        except KeyError:
            # The website has not been saved in the json file
            messagebox.showerror("Error", f"No data for {web_entry} exists")
        except FileNotFoundError:
            # There is no json file yet
            messagebox.showerror("Error", "No Data File found\nCreate the first entry by adding all sections")
        else:
            messagebox.askquestion(title=web_entry, message=line)


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

add_b = Button(text="Add", width=45, highlightthickness=0, command=save_pw)
add_b.grid(column=1, row=4, columnspan=3)
# add_b.place(x=145, y=270)

search_b = Button(text="Search", width=14, highlightthickness=0, command=search_info)
search_b.grid(column=2, row=1)

# ENTRIES
web_box = Entry(width=35)
web_box.grid(column=1, row=1)
web_box.focus()

user_box = Entry(width=53)
user_box.grid(column=1, row=2, columnspan=3)
user_box.insert(END, "myemail@email.com")  # pre-populated email

pw_box = Entry(width=35)
# pw_box.place(x=145, y=248)
pw_box.grid(column=1, row=3)
screen.mainloop()
