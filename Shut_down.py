from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Hohuydrive")
window.geometry("1600x900")
window.resizable(0, 0)
window.iconbitmap("Image\logo.ico")

Image = ImageTk.PhotoImage(Image.open(Backround))

window.mainloop()