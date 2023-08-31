
from tkinter import *
import base64
from tkinter import messagebox
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def savetofile():
    note_title=entry1.get()
    note=text.get("1.0",END)
    secret_key=entry2.get()
    if len(note_title)==0 or len(note)==0 or len(secret_key)==0:
        messagebox.showerror("ERROR", "Please fill all !!!")
    else:
        encode_text=encode(secret_key,note)
        try:
            with open("secret.txt", "a") as data_file:
                data_file.write(f'\n{note_title}\n{encode_text}')
        except FileNotFoundError:
            with open("secret.txt", "w") as data_file:
                data_file.write(f'\n{note_title}\n{encode_text}')
        finally:
            entry1.delete(0, END)
            entry2.delete(0, END)
            text.delete("1.0", END)
def decodethetext():
    get_text=text.get("1.0",END)
    secrettkey = entry2.get()
    if len(get_text)==0 or len(secrettkey)==0:
        messagebox.showerror("ERROR", "Please fill all !!!")
    else:
        try:
         decode_message = decode(secrettkey,get_text)
         text.delete("1.0", END)
         text.insert("1.0",decode_message )
        except:
            messagebox.showerror(title="ERROR", message="Please make sure of encrypted info !!!")

window=Tk()

window.title("Secret Notes")
window.minsize(width=400,height=600)
window.config(background="azure3")

icon = PhotoImage(file="memo.png")
icon_Label = Label(image=icon)
icon_Label.place(x=140,y=5)

label1=Label(text="Enter your title :",font=('Arial',10,'bold'))
label1.place(x=150,y=140)

entry1=Entry(width=40)
entry1.place(x=90,y=170)

label2=Label(text="Enter your secret :",font=('Arial',10,'bold'))
label2.place(x=150,y=200)

text=Text(width=30,height=15)
text.place(x=90,y=220)

label2=Label(text="Enter master key :",font=('Arial',10,'bold'))
label2.place(x=150,y=470)

entry2=Entry(width=40)
entry2.place(x=90,y=490)

first_button=Button(text="Save & Encrypt",command=savetofile)
first_button.place(x=160,y=520)

second_button=Button(text="Decrypt",command=decodethetext)
second_button.place(x=180,y=550)

window.mainloop()