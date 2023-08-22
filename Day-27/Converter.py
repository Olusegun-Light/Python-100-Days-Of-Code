#  Miles to Km Converter
from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_results_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(height=300, width=300)
window.config(padx=30, pady=30)


# Entry
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

# Label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

km_results_label = Label(text=0)
km_results_label.grid(row=1, column=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

# Keep the GUI on screen
window.mainloop()
