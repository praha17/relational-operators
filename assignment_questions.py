#discount based on purchased amount using tkinter
from pyexpat.errors import messages
from tkinter import*
from tkinter import messagebox, Button
from tkinter import Label

window=Tk()
window.title("Discount")
def discount():
    amt=int(e1.get())
    if amt>=500:
        dis=(amt*15)/100
        total_amt_to_be_paid=amt-dis
        messagebox.showinfo("Amount to be paid after discount",total_amt_to_be_paid)
    elif amt>=200 and amt<=500:
        dis=(amt*10)/100
        total_amt_to_be_paid=amt-dis
        messagebox.showinfo("Amount to be paid after discount",total_amt_to_be_paid)

    else:
        total_amt_to_be_paid=amt
        messagebox.showinfo("Amount to be paid after discount",total_amt_to_be_paid)

window.geometry("500x500")
window.config(background="white")
l1=(Label(window,text="Enter payable amount: "))
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
b1=Button(window,text="Payable Amount",command=discount)
b1.grid(row=2,column=1)
window.mainloop()






