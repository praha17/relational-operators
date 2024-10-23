#bank eligibility
#discount based on purchased amount using tkinter
from pyexpat.errors import messages
from tkinter import*
from tkinter import messagebox, Button
from tkinter import Label

window=Tk()
window.title("Bank loan eligibility")
def eligibility():
    age=int(e1.get())
    salary=float(e2.get())
    credit_score=int(e3.get())
    if 21 <= age < 60:
        if salary>=20000:
            if credit_score>=650:
                messagebox.showinfo("You are eligible for bank loan","approved")
    else:
        messagebox.showinfo("Your are not eligible","failed")

window.geometry("500x500")
window.config(background="white")
l1=(Label(window,text="Enter your age: "))
l1.grid(row=0,column=0)

l2=Label(window,text="Enter your salary: ")
l2.grid(row=1,column=0)

l3=Label(window,text="Credits score: ")
l3.grid(row=2,column=0)

e1=Entry(window)
e1.grid(row=0,column=1)

e2=Entry(window)
e2.grid(row=1,column=1)

e3=Entry(window)
e3.grid(row=2,column=1)

b1=Button(window,text="Payable Amount",command=eligibility)
b1.grid(row=4,column=3)
window.mainloop()