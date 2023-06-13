from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()#packer used for geometry mechanism can align left right top bottom , give padding , expand,

def button_clicked():
    my_label["text"] = input.get()
#button
button = Button(text = "Press me", command=button_clicked)
button.pack()

#Input

input = Entry(width = 10)
input.pack()

#positional functions
# pack puts everything from top to bottom order
# place(x= ,y= ) puts things on given co-ordinates
# grid make the entire window into grids based on rows -- and columns |



window.mainloop()