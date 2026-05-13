from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Alert! Virus Detected")
root.geometry("400x200")
def msg(): 
    messagebox.showwarning("Virus Detected", "A virus has been detected on your computer.")
button = Button(root, text="Scan for Viruses", command=msg)
button.place(x= 40 , y= 80)
root.mainloop()