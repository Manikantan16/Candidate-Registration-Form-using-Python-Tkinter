import tkinter as tk
import tkinter.messagebox as msgbox

root = tk.Tk()
root.title('Simple Tkinter App')
root.geometry('300x100') 

def say_hello():
    print('Hello World!')
    msgbox.showinfo("Python","This is my First Task in Tkinter GUI Module.")
    
    
    
hello_button = tk.Button(root,text='Click Me',command=say_hello)
hello_button.pack(pady=20)

root.mainloop()