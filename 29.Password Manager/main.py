from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as file:
        file.write(f"\n{website} | {username} | {password}")
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
generate_button = Button(text="Generate Password",width=14)
generate_button.grid(column=2, row=3)

#Add
add_button = Button(text="Add", width=44,command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()