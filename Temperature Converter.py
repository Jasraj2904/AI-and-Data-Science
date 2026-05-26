from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Temperature Converter")
root.geometry("450x350")
root.config(bg="#87CEEB")

title = Label(
    root,
    text="Celsius to Fahrenheit Converter",
    font=("Arial", 20, "bold"),
    bg="#1E3A5F",
    fg="white",
    pady=10
)
title.pack(fill=X)

frame = Frame(root, bg="#87CEEB")
frame.pack(pady=40)

label1 = Label(
    frame,
    text="Enter Temperature in Celsius:",
    font=("Arial", 14),
    bg="#87CEEB"
)
label1.grid(row=0, column=0, pady=10)

celsius_entry = Entry(
    frame,
    font=("Arial", 14),
    width=15,
    bd=3
)
celsius_entry.grid(row=0, column=1, padx=10)

result_label = Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#87CEEB",
    fg="darkblue"
)
result_label.pack(pady=20)

def convert_temperature():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32

        result_label.config(
            text=f"Temperature in Fahrenheit: {fahrenheit:.2f} °F"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number!"
        )

convert_btn = Button(
    root,
    text="Convert",
    font=("Arial", 14, "bold"),
    bg="darkblue",
    fg="white",
    padx=20,
    pady=5,
    command=convert_temperature
)
convert_btn.pack(pady=10)

exit_btn = Button(
    root,
    text="Exit",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    padx=20,
    pady=5,
    command=root.destroy
)
exit_btn.pack(pady=10)

root.mainloop()