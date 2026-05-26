from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x400")
root.title("Login Screen")
root.config(bg="lightblue")
title = Label(
    root,
    text="LOGIN SYSTEM",
    font=("Arial", 24, "bold"),
    bg="darkblue",
    fg="white"
)
title.pack(pady=20)
frame = Frame(root, bg="#2c2c3e", padx=30, pady=30)
frame.pack(pady=20)
user_label = Label(
    frame,
    text="Username",
    font=("Arial", 14),
    bg="#2c2c3e",
    fg="white"
)
user_label.grid(row=0, column=0, pady=10, sticky="w")
user_entry = Entry(
    frame,
    font=("Arial", 14),
    width=25
)
user_entry.grid(row=0, column=1, pady=10)
pass_label = Label(
    frame,
    text="Password",
    font=("Arial", 14, "bold"),
    bg="#2c2c3e",
    fg="white"
)
pass_label.grid(row=1, column=0, pady=10, sticky="w")
pass_entry = Entry(
    frame,
    font=("Arial", 14),
    width=25,
    show="*"
)
pass_entry.grid(row=1, column=1, pady=10)
def login():
    username = user_entry.get()
    password = pass_entry.get()
    if username == "Jasraj" and password == "Jasraj123":
        messagebox.showinfo("Login Success", "Welcome, Jasraj!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
login_btn = Button(
    frame,
    text="Login",
    font=("Arial", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    command=login
)
login_btn.grid(row=2, column=0, columnspan=2, pady=20)
root.mainloop()