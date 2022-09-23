from tkinter import *
from tkinter import messagebox
import base64
import os

def encrypt():
    password = code.get()

    if password=="1234":
        screen1 =Toplevel(screen)
        screen1.geometry("375x398")
        screen1.title("EnC")
        screen1.configure(bg="orange")

        message = text1.get(1.0, END)
        encode_message=message.encode("ascii")
        base64_bytes= base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1, text ="Encrypt", bg='orange' ,fg="black", font=("calbri", 13)).place(x=10,y=0)
        text2 = Text(screen1, font=("calbri", 15), bg="white", relief=GROOVE, wrap=WORD, bd = 0)
        text2.place(x=10, y=40, width=360, height=150)
        text2.insert(END, encrypt)

    elif password=="":
        messagebox.showerror("encryption", "Input Password" )


    elif password!="1234":
        messagebox.showerror("encryption", "Invalid Password")


def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.geometry("375x398")
        screen2.title("DeC")
        screen2.configure(bg="orange")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="Decrypt", bg='skyblue', fg="black", font=("calbri", 13)).place(x=10, y=0)
        text3 = Text(screen2, font=("calbri", 15), bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text3.place(x=10, y=40, width=360, height=150)
        text3.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")


    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid Password")

def main_screen():

    global screen
    global code
    global  text1

    screen =Tk()
    screen.geometry("375x398")
    screen.title("EnC DeC")

    def reset():
        code.set("")
        text1.delete(1.0, END)


    Label(text= "Enter text for Encryption and Decryption", fg="black", font=("calbri", 13)).place(x=10,y=10)
    text1 = Text(font=("calbri", 15), bg="white", relief=GROOVE, wrap=WORD, bd = 0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10,y=170)

    code =StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="Encrypt", height="2", width="23", bg="orange", fg="white",  bd=0, command=encrypt).place(x=10,y=250)
    Button(text="Decrypt", height="2", width="23", bg="skyblue", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="Reset", height="2", width="50", bg="skyblue", fg="white", bd=0, command=reset).place(x=10, y=300)


    screen.mainloop()

main_screen()