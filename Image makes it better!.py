from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Image makes it better!")
root.geometry("500x500")
upload = Image.open("Brabus.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image)
label.image = image
label.place(x=50, y=0)
label2 = Label(root, text="Brabus is the best car in the world!")
label2.place(x=40, y=450)
root.mainloop()