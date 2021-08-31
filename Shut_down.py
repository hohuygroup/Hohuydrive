from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Hohuydrive")
window.geometry("1600x900")
window.resizable(0, 0)
window.iconbitmap("Image\logo.ico")

Image = ImageTk.PhotoImage(Image.open("Image/Backround/backrounds.png"))
Backround = Label(window, image=Image)
Backround.place(x=-5, y=0)

a = Label(window, text="Đang tắt",  font=("Arial Bold", 20), bg="#000000", fg="#ffffff")
a.place(x=730, y=550)

b = Label(window, text="Tắt sau 5 giây",  font=("Arial Bold", 20), bg="#000000", fg="#ffffff")
b.place(x=690, y=410)

window.mainloop()