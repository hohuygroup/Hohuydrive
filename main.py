# Nhập các thư viện cần thiết
from tkinter import *
from PIL import Image, ImageTk
from sys import path
path.append("Module/")
from ftplib import FTP
from PML import openfile, search, name
from openhh import OpenHH, run
from tkinter import messagebox
from tkinter import filedialog
import os 


# Kết nối tới server
# ftp = FTP("192.168.56.1")
# ftp.login(user="Windows 10", passwd="29092008")

# Mở file Data
data = openfile("Data/data.pml")
# Mở file App
application = openfile("Data/app.pml")


# Xử lí file Data
data_1 = data.read()
# 1 Backround
Backround = str(data_1["background"])
# 2 Logo
logo = str(data_1["logo"])
# 3 Display resolution
geometry = str(data_1["display_resolution"])

# Tạo cửa sổ
window = Tk()
window.title("Hohuydrive")
window.geometry(geometry)
window.resizable(0, 0)
window.iconbitmap(logo)



# Mở ảnh

#image = Image.open("Image/Folder.png")
image_1 = Image.open(Backround)
#image_2 = Image.open("Image/Hide.png")
# image_3 = Image.open("Image/Rar file.png")
# image_4 = Image.open("Image/Strange file.png")
image_5 = Image.open("Image/taskbar.png")
# image_6 = Image.open("Image/Txt file.png")
# image_7 = Image.open("Image/Zip file.png")
image_8 = Image.open("Image/Logo.png")
image_9 = Image.open("Image/Start.png")
image_10 = Image.open("Image/Logo_1.png")
image_11 = Image.open("Image/Button.png")

# Xử lí ảnh
# Image_Folder = ImageTk.PhotoImage(image)
Image_Backround = ImageTk.PhotoImage(image_1)
# Image_Hide = ImageTk.PhotoImage(image_2)
# Image_Rar file = ImageTk.PhotoImage(image_3)
# Image_Strange file = ImageTk.PhotoImage(image_4)
Image_taskbar = ImageTk.PhotoImage(image_5)
# Image_Txt file = ImageTk.PhotoImage(image_6)
# Image_Zip file = ImageTk.PhotoImage(image_7)
Image_Logo = ImageTk.PhotoImage(image_8)
Image_Logo_1 = ImageTk.PhotoImage(image_10)
Image_StartMenu = ImageTk.PhotoImage(image_9)
Image_Button = ImageTk.PhotoImage(image_11)

# lists = ftp.retrlines('LIST')
# for x in lists:
# 	if x[24] == "<":
# 		tach = x.split("       <DIR>          ")
# 	else:
# 		tach = x.split("                    ")
# 	del tach[0]


# 	a = 0
# 	name = tach[0]
# 	for y in name:
# 		try:
# 			ftp.cwd(name)
# 		except:
# 			try:
# 				int(y)
# 			except:
# 				name = name[a:]
# 				break
# 			if y == " ":
# 				name = name[a:]
# 				break
# 			a += 1
# 			if name[0] == " ":
# 				name = name[1:]
# 		else:	
# 			name = x
# 		ftp.cwd("..")
# print(ftp.pwd())

# Định nghĩa hàm
whiles = 0
Start = ""
Shut_downs = ""
Canvas = ""
lbs = ""
app = []
a = []
b = []
def logo(e):
    global Start, whiles, Shut_downs, Canvas, lbs, app, a, b

    def Shut_down():
        window.destroy()
        import Shut_down

    # Mở file start menu
    start_menu = openfile("Data/Start menu.pml")
    # Đọc file
    reads = start_menu.read()

    


    if whiles == 0:
        a.clear()
        b.clear()

        Start =  Label(window, image=Image_StartMenu)
        Start.place(x=0, y=260)
        Shut_downs = Button(window, text="Shut down", command=Shut_down)
        Shut_downs.place(x=300, y=800)
        
        Canvas = Label(window, text="│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│\n│", bg="#C3C3C3")
        Canvas.place(x=270, y=264)

        whiles += 1

        lbs = Label(window, text=reads["account"], bg="#C3C3C3", font=("Arial Bold", 15))
        lbs.place(x=315 , y=275)

        y = 350
        xx = 0
        xy = 310

        def ok(e):
            file = app[e]

            if file == "Installation":
                file = filedialog.askopenfilename(filetypes = (("Application files","*.hh"),("all files","*.*")))

                if file != "":
                    name_file = name(file)

                    if messagebox.askquestion('Installation', "Bạn có muốn cài ứng dụng " +  name_file + " ?") == "yes":
                        os.mkdir('Data/App/' + name_file)
                        OpenHH(file, "Data/App/" + name_file + "/").installation()
                        application.write(name_file, "Data/App/" + name_file + "/")
                        if messagebox.askquestion('Installation', 'Đã hoàn thành cài ứng dụng. Bạn có muốn chạy ứng dụng không?') == "yes":
                            run()

        # Tìm kiếm biến
        for x in search(reads, "app_1_s", "app_2_s", "app_3_s").return_search():

            if x == "app_2_s":
                xy = 320
            elif x == "app_3_s":
                xy = 305
 
            bts = Label(window, image=Image_Button, bg="#C3C3C3")
            bts.place(x=290 , y=y)

            btss = Label(window, text=reads[x], bg="#C3C3C3")
            btss.place(x=xy , y=y+5)

            bts.bind("<Button-1>", lambda aa, jj=xx: ok(jj))
            btss.bind("<Button-1>", lambda aa, jj=xx: ok(jj))

            y += 50
            xx += 1
            a.append(bts)
            b.append(btss)
            app.append(reads[x])

    else:
        Start.place(x=-1000, y=260) 
        Canvas.place(x=-1000, y=260)
        Shut_downs.place(x=-1000, y=260)
        lbs.place(x=-1000, y=260)
        start_menu.close()

        for x in range(0, len(a)):
            a[x].place(x=-1000, y=260)
        for y in range(0, len(b)):
            b[y].place(x=-1000, y=260)

        whiles -= 1



def mouse(e):
   Logo.configure(image=Image_Logo_1)
def mouse_1(e):
   Logo.configure(image=Image_Logo)

Backround = Label(window, image=Image_Backround)
Backround.place(x=0, y=0)
Taskbar = Label(window, image=Image_taskbar)
Taskbar.place(x=-2, y=848)
Logo = Label(window, image=Image_Logo, background="black")
Logo.bind("<Button-1>", logo)
Logo.bind("<Enter>", mouse)
Logo.bind("<Leave>", mouse_1)
Logo.place(x=5, y=857)



window.mainloop()