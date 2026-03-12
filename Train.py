import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Train Status")
label=tk.Label(root,text="Live Running Train Status ",font=("Times New Roman",21,"bold"))
label.pack(pady=15)

trainName=tk.Label(root,text="Train Name")
trainName.grid(row=0,column=1,padx=10,pady=12)

tk.Label(root,text="Train No").grid(row=0,column=2)
tk.Label(root,text="From").grid(row=0,column=3)
tk.Label(root,text="To").grid(row=0,column=4)
tk.Label(root,text="Time").grid(row=0,column=5)
tk.Label(root,text="Status").grid(row=0,column=6)
root.mainloop()