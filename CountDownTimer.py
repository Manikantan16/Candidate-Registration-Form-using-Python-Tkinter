from tkinter import *
import time
from tkinter import messagebox
def gettime():
    strtime = time.strftime('%H:%M:%S %p')
    Label_time.config(text=strtime)
    Label_time.after(1000,gettime)
    
def start_timer():
    temptime = int(hrs.get()) * 3600 + int(mts.get()) * 60 + int(secs.get())
    print(temptime)
    while temptime >= 0:
        vmin,vsec = divmod(temptime,60)
        print(vmin,vsec)
        vhr =0
        if vmin > 60:
            vhr,vmin = divmod(vmin,60)
            print(vhr,vmin)
            
        hrs.set(vhr)
        mts.set(vmin)
        secs.set(vsec)
        window.update()
        time.sleep(1)
        temptime-=1
       
    messagebox.showinfo("Count Down Timer","Count Down Timer finished..")
        

window = Tk()
window.title('Count Down Timer') #set the title to the windoow
window.geometry('400x600') #specify the size 
window.config(background='#000') #specify the background color
window.resizable(0,0) # can not be resized 

#Create a label
Label(window,text="Timer",font="arial 30 bold",background='#000',foreground='#ea3548').pack(pady=10)

#Create a label Show the system time
Label(window,font="arial 15 bold",text='Current Time -',background="papaya whip").place(x=65,y=70)
Label_time = Label(window,text='',font="arial 15 bold",foreground="#000",background="papaya whip")
Label_time.place(x=190,y=70)

#define the Hours Minutes and Seconds textbox 
hrs = StringVar()
Entry(window,textvariable=hrs,width=2,font="arial 50",border=0).place(x=30,y=155)
Label(window,text="hrs",font="arial 10",background='#000',foreground='#fff').place(x = 105, y = 200)
hrs.set("00")

mts = StringVar()
Entry(window,textvariable=mts,width=2,font="arial 50",border=0).place(x=150,y=155)
Label(window,text="mts",font="arial 10",background='#000',foreground='#fff').place(x = 225, y = 200)
mts.set("00")

secs = StringVar()
Entry(window,textvariable=secs,width=2,font="arial 50",border=0).place(x=270,y=155)
Label(window,text="secs",font="arial 10",background='#000',foreground='#fff').place(x = 345, y = 200)
secs.set("00")

Button(window,text='Start',background='#ea3548',foreground='#fff',width=20,height=2,font='aria 10 bold',
       bd=0,command=start_timer).pack(padx=5,pady=50,side=BOTTOM)

gettime()
window.mainloop()