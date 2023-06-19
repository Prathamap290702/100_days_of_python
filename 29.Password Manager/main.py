from tkinter import *
from tkinter import messagebox
import pyperclip
from random import *
import string
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = list(string.ascii_letters)
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['~', ':', "'", '+', '[', '\\', '@', '^',
               '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,5))]
    password_symbols = [choice(symbols) for _ in range(randint(2,5))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data= {website: {
        "username": username,
        "password": password,
    } }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")

    else:
        is_ok = messagebox.askokcancel(title=f"Website_info: {website}", message=f"These are the details entered: \nEmail: {username} "
                                       f"\n Password: {password} \nIs it ok to save?")
        if is_ok:
            # used to write in a txt file
            # with open("data.txt", "a") as file:
            #     file.write(f"{website} | {username} | {password}\n")

            #using a JSON file
        try:
            with open("data.json", "r") as file:
                # json.dump(new_data, file, indent=4)#how to write in json file
                # data = json.load(file) #how to read json file
                # print(data)

                # # 3-step
                # # Reading old data
                data = json.load(file)
                # print(data)
                # #updating old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # saving new data
                json.dump(data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                # saving new data
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img )
canvas.grid(column=1, row = 0)

# labels
# Website line
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width = 52 )
website_entry.grid(column=1, row=1,columnspan=2)
website_entry.focus()


# Email line
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "prathamap2002@gmail.com")

# Password line
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

#Buttons
#Generate
generate_button = Button(text="Generate Password",width=14, command=generate_password)
generate_button.grid(column=2, row=3)

#Add
add_button = Button(text="Add", width=44,command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()