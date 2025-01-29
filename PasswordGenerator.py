from tkinter import *
import random,string
import pyperclip

root = Tk()
root.geometry('500x200')
root.title('TKINTER - PASSWORD GENERATOR')

Label(root,text='PASSWORD GENERATOR',font='arial 15 bold').pack()
#Label(root,text='PASSWORD GENERATOR WINDOW',font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root,text='PASSWORD LENGTH',font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root,from_=8,to=32,textvariable=pass_len,width=15).pack()
pass_str = StringVar()

def generator():
    pwd = []
    if pass_len.get() >= 4:
        pwd+= random.choice(string.ascii_uppercase)
        pwd+= random.choice(string.ascii_lowercase)
        pwd+= random.choice(string.punctuation)
        pwd+= random.choice(string.digits)
        
        for _ in range(pass_len.get() - 4):
            pwd+= random.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits)
            random.shuffle(pwd)
    else:
        for _ in range(pass_len.get()):
            pwd.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits))
    
    pass_str.set(''.join(pwd))
    
def copy_pwd():
    pyperclip.copy(pass_str.get())
    
    
Button(root,text='GENERATE PASSWORD',activebackground='yellow',command=generator).pack(pady=5)
Entry(root,textvariable=pass_str).pack()
Button(root,text='COPY TO CILPBOARD',command=copy_pwd).pack(pady=5)

root.mainloop()

