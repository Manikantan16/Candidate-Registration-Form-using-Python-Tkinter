
import tkinter as tk

root = tk.Tk()
root.title('Simple Tkinter App')
root.geometry('300x100') 

label = tk.Label(root,text='Hello World')
label.pack()
root.mainloop()