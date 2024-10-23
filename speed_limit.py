#discount based on purchased amount using tkinter
from pyexpat.errors import messages
from tkinter import*
from tkinter import messagebox, Button
from tkinter import Label

window=Tk()
window.title("Speed Limit")
def speed():
    car_speed=int(e1.get())
    speed_limit=90
    if car_speed<=speed_limit:
        messagebox.showinfo("No Penalty",message="NO penatly!HAPPY JOURNEY")
    #elif car_speed>speed_limit:
        #messagebox.showinfo("Warning",message="Warning")
    else:
        car_speed+=20
        messagebox.showinfo("Penality Warning",message="1000rs penality")

window.geometry("500x500")
window.config(background="white")
l1=(Label(window,text="Car Speed: "))
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
b1=Button(window,text="Go",command=speed)
b1.grid(row=2,column=1)
window.mainloop()






