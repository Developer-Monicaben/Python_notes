import tkinter as tk
from tkinter import messagebox

balance = 1000

def check_balance():
    messagebox.showinfo("Your Balance:",balance)
    
def deposit():
    amount = entry.get()
    if amount.isdigit():
        global balance
        balance += int(amount)
        messagebox.showinfo("Success", "Money deposited!")
    else:
        messagebox.showerror("Error", "Enter valid amount")


def withdraw():
    amount = entry.get()
    if amount.isdigit():
        global balance
        amt = int(amount)
        if amt <= balance:
            balance -= amt
            messagebox.showinfo("Success", "Money withdrawn!")
        else:
            messagebox.showerror("Error", "Not enough balance")
    else:
        messagebox.showerror("Error", "Enter valid amount")

# GUI setup
win = tk.Tk()
win.title("Simple Bank")
win.geometry("250x200")

tk.Label(win, text="Amount:").pack(pady=5)
entry = tk.Entry(win)
entry.pack()

tk.Button(win, text="Check Balance", command=check_balance).pack(pady=5)
tk.Button(win, text="Deposit", command=deposit).pack(pady=5)
tk.Button(win, text="Withdraw", command=withdraw).pack(pady=5)

win.mainloop()
