import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import time
import csv
import os
from PIL import Image, ImageTk
def win():
    import checkbutton
    checkbutton.win1()


root = Tk()
root.title("Desi Swaad Restaurant")
root.geometry("1000x650")
root.configure(bg="lightgreen")

#---------------- Heading ----------------#
title = Label(root,
              text="Desi Swaad Restaurant",
              font=("Arial",30,"bold"),
              fg="red",
              bg="white")
title.place(x=180,y=10)
# Logo
img = Image.open("logo.jpeg")
img = img.resize((100, 100))   # Logo का size
logo = ImageTk.PhotoImage(img)

logo_label = Label(root, image=logo, bg="lightgreen")
logo_label.place(x=700, y=10)

#---------------- Date & Time ----------------#
localtime = time.asctime(time.localtime(time.time()))
lbltime = Label(root,
                text=localtime,
                font=("Arial",14,"bold"),
                bg="white",
                fg="blue")
lbltime.place(x=320,y=70)

#------------- MENU & BILL PAYMENT -------------#
menu = Label(root, text="MENU",
             font=("Arial",18,"bold"),
             bg="lightgreen")
menu.place(x=180, y=110)

bill = Label(root, text="BILL PAYMENT",
             font=("Arial",18,"bold"),
             bg="lightgreen")
bill.place(x=580, y=110)

line = Frame(root, bg="black", width=3, height=370)
line.place(x=470, y=140)

#---------------- Variables ----------------#
ref = StringVar()
fries = StringVar()
noodles = StringVar()
soup = StringVar()
burger = StringVar()
sandwich = StringVar()

drinks = StringVar()
costmeal = StringVar()
service = StringVar()
tax = StringVar()
subtotal = StringVar()
total = StringVar()

ref = StringVar()

#---------------- Left Side ----------------#
Label(root,text="Reference",font=("Arial",14,"bold"),bg="white").place(x=30,y=150)
Entry(root,textvariable=ref,font=("Arial",14),width=20).place(x=170,y=150)

Label(root,text="Fries",font=("Arial",14,"bold"),bg="white").place(x=30,y=200)
Entry(root,textvariable=fries,font=("Arial",14),width=20).place(x=170,y=200)

Label(root,text="Noodles",font=("Arial",14,"bold"),bg="white").place(x=30,y=250)
Entry(root,textvariable=noodles,font=("Arial",14),width=20).place(x=170,y=250)

Label(root,text="Soup",font=("Arial",14,"bold"),bg="white").place(x=30,y=300)
Entry(root,textvariable=soup,font=("Arial",14),width=20).place(x=170,y=300)

Label(root,text="Burger",font=("Arial",14,"bold"),bg="white").place(x=30,y=350)
Entry(root,textvariable=burger,font=("Arial",14),width=20).place(x=170,y=350)

Label(root,text="Sandwich",font=("Arial",14,"bold"),bg="white").place(x=30,y=400)
Entry(root,textvariable=sandwich,font=("Arial",14),width=20).place(x=170,y=400)

Label(root,text="Drinks",font=("Arial",14,"bold"),bg="white").place(x=30,y=450)
Entry(root,textvariable=drinks,font=("Arial",14),width=20).place(x=170,y=450)
#---------------- Right Side ----------------#


Label(root,text="Cost of Meal",font=("Arial",14,"bold"),bg="white").place(x=500,y=200)
Entry(root,textvariable=costmeal,font=("Arial",14),width=20).place(x=650,y=200)

Label(root,text="Service Charge",font=("Arial",14,"bold"),bg="white").place(x=500,y=250)
Entry(root,textvariable=service,font=("Arial",14),width=20).place(x=650,y=250)

Label(root,text="State Tax",font=("Arial",14,"bold"),bg="white").place(x=500,y=300)
Entry(root,textvariable=tax,font=("Arial",14),width=20).place(x=650,y=300)

Label(root,text="Sub Total",font=("Arial",14,"bold"),bg="white").place(x=500,y=350)
Entry(root,textvariable=subtotal,font=("Arial",14),width=20).place(x=650,y=350)

Label(root,text="Total Cost",font=("Arial",14,"bold"),bg="white").place(x=500,y=400)
Entry(root,textvariable=total,font=("Arial",14),width=20).place(x=650,y=400)
#---------------- Functions ----------------#

def Total():
    try:
        f = int(fries.get() or 0)
        n = int(noodles.get() or 0)
        s = int(soup.get() or 0)
        b = int(burger.get() or 0)
        sw = int(sandwich.get() or 0)
        d = int(drinks.get() or 0)

        # Price Calculation
        meal = (f * 80) + (n * 120) + (s * 70) + (b * 150) + (sw * 100) + (d * 50)

        service_charge = meal * 0.10
        state_tax = meal * 0.05
        sub_total = meal + service_charge
        grand_total = sub_total + state_tax

        costmeal.set("Rs:%.2f" % meal)
        service.set("Rs:%.2f" % service_charge)
        tax.set("Rs:%.2f" % state_tax)
        subtotal.set("Rs:%.2f" % sub_total)
        total.set("Rs:%.2f" % grand_total)

        filename = "orders.csv"

        header = [
            "Reference", "Fries", "Noodles", "Soup",
            "Burger", "Sandwich", "Drinks",
            "CostMeal", "ServiceCharge",
            "Tax", "SubTotal", "Total"
        ]

        data = [
            ref.get(),
            fries.get(),
            noodles.get(),
            soup.get(),
            burger.get(),
            sandwich.get(),
            drinks.get(),
            costmeal.get(),
            service.get(),
            tax.get(),
            subtotal.get(),
            total.get()
        ]

        file_exists = os.path.isfile(filename)

        with open(filename, "a", newline="",encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(header)

            writer.writerow(data)

        messagebox.showinfo("Success", "Order Saved Successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def Reset():
    ref.set(str(random.randint(1000,9999)))
    fries.set("")
    noodles.set("")
    soup.set("")
    burger.set("")
    sandwich.set("")
    drinks.set("")
    costmeal.set("")
    service.set("")
    tax.set("")
    subtotal.set("")
    total.set("")


def Exit():
    root.destroy()


#---------------- Buttons ----------------#

Button(root,
       text="Total",
       font=("Arial",14,"bold"),
       bg="brown",
       width=10,
       command=Total).place(x=180,y=500)

Button(root,
       text="Reset",
       font=("Arial",14,"bold"),
       bg="brown",
       width=10,
       command=Reset).place(x=360,y=500)

Button(root,
       text="Exit",
       font=("Arial",14,"bold"),
       bg="brown",
       width=10,
       command=Exit).place(x=540,y=500)
Button(root,
       text="CheckButton",
       font=("Arial",14,"bold"),
       bg="brown",
       width=10,
       command=win).place(x=700,y=500)
root.mainloop()