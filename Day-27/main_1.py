from tkinter import *


def button_clicked():
    print("Button clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=500)
# Padding around the entire window
window.config(padx=20, pady=20)

# label
my_label = Label(text="This a label", font=("Arial", 18, "italic"))
# widget position
# button.pack()
# my_label.place(x=50, y=0)
my_label.grid(column=0, row=0)


#  Buttons
button = Button(text="Click Me", command=button_clicked)
# widget position
# button.pack()
# button.place(x=38, y=90)
button.grid(column=1, row=1)


# Entry
input = Entry(width=20)
# widget position
# input.pack()
# input.place(x=78, y=100)
input.grid(column=2, row=2)


# Keeps GUI on the screen
window.mainloop()
