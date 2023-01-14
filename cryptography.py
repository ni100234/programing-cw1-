import onetimepad		
from tkinter import *
from PIL import ImageTk
from PIL import Image	
root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("620x200")
img =Image.open('C:\\Users\\Acer\\Desktop\\progarming-py\\cw1\\enc.jpg')
img=img.resize((620,200))
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
label.place(x =0,y =0)
root.mainloop()
