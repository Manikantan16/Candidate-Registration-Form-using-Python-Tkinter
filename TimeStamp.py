from tkinter import *
import time
from datetime import datetime

root = Tk()
root.title('DATE TIME STAMP - DIGITAL CLOCK')
root.geometry('900x150')
root.resizable(False,False)

    
def refresh_datetimestamp():
    _Currdatetime = datetime.now().strftime("%A, %d %B %Y") + ' ' + time.strftime('%H:%M:%S %p')
    clock_label.config(text = _Currdatetime)    
    clock_label.after(1000,refresh_datetimestamp)

clock_label = Label(root,font=('Calibri',30,'bold'),background='pink',foreground='white')
clock_label.pack(anchor=CENTER,fill=BOTH,expand=1)
refresh_datetimestamp()
root.mainloop()