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

d = 5

def c():
	global d

	if d == 0:
		quit()

	b.config(text="Tắt máy sau " + str(d))

	d -= 1

	b.after(1000, c)


b = Label(window,  font=("Arial Bold", 20), bg="#000000", fg="#ffffff")
b.place(x=690, y=430)

c()

window.mainloop()