from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image	
root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("400x300")
root.resizable(False,False)
img =Image.open('C:\\Users\\Acer\\Desktop\\progarming-py\\dist\\enc.jpg')
img=img.resize((400,300))
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
label.place(x =0,y =0)

# set global variables
global filepath
global Key
global keypath

# generates the key for encrypting/decrypting
def Generate():
    keypath = filedialog.askopenfilename()
    key = Fernet.generate_key()
    try:
        with open(keypath, "wb") as filekey:
            filekey.write(key)
    except FileNotFoundError:
        messagebox.showerror("Error", "no file was selected, try again")
        return
    messagebox.showinfo( "", "Key generated successfully!")

# function to encrypt files of your choosing
def Encrypt():
    messagebox.showinfo( "", "select a key")
    # prompts the user to select a file with a key
    keypath = filedialog.askopenfilename()
    # open key file
    try:
        with open(keypath, "rb") as filekey:
            key = filekey.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "no file was selected, try again")
        return

    # if the file selected doesn't have a key in it, it stops the function and gives the user an error
    try:
        global fernet
        fernet = Fernet(key)
    except ValueError:
        messagebox.showerror("Error", "This is not a key file, try again")
        return

    messagebox.showinfo( "", "select one or more files to encrypt")
    # prompts the user to select a file to encrypt
    filepath = filedialog.askopenfilenames()
    for x in filepath:
        # opens each file in filepath 
        with open(x, "rb") as file:
            original = file.read()
        
        # encrypts the selected file
        global encrypted
        encrypted = fernet.encrypt(original)
        with open(x, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    if not filepath:
        messagebox.showerror("Error", "no file was selected, try again")
    else:
        messagebox.showinfo( "", "files encrypted successfully!")
    

# function to decrypt files of your choosing
def Decrypt():
    messagebox.showinfo( "", "select a key")
    keypath = filedialog.askopenfilename()
    try:
        with open(keypath, "rb") as filekey:
            key = filekey.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "no file was selected, try again")
        return

    # if the file selected doesn't have a key in it, it stops the function and gives the user an error
    try:
        global fernet
        fernet = Fernet(key)
    except ValueError:
        messagebox.showerror("Error", "This is not a key file, try again")
        return

    messagebox.showinfo( "", "select one or more files to decrypt")
    # User to select a file to decrypt
    filepath = filedialog.askopenfilenames()
    for x in filepath:
        with open(x, "rb") as enc_file:
            encrypted = enc_file.read()
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        with open(x, "wb") as dec_file:
            dec_file.write(decrypted)
    if not filepath:
        messagebox.showerror("Error", "no file was selected, try again")
    else:
        messagebox.showinfo( "", "files decrypted successfully!")

my_label = tk.Label()

label1 = tk.Label(root, text="Click the below button to generate a new key")
label1.pack(pady=20)
B = Button(root, text="Generate Key", command=Generate)
B.config(font=("Areal", 12, "bold"),background="red")
B.pack()

label2 = tk.Label(root, text="Click the button below to encrypt your file")
label2.pack(pady=20)
ebutton = Button(root, text="encrypt", command=Encrypt)
ebutton.config(font=("Areal", 12, "bold"),background="yellow")
ebutton.pack()

label3 = tk.Label(root, text="Click the button below to decrypt an encrypted file")
label3.pack(pady=20)
ebutton = Button(root, text="decrypt", command=Decrypt)
ebutton.config(font=("Areal", 12, "bold"),background="green")
ebutton.pack()

root.mainloop()
