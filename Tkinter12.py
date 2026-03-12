import tkinter as tk 
from tkinter import messagebox
def firstProg():
    messagebox.showinfo("Success ","Click me button is clicked !!!!")

def show_name():
    name = entry.get()
    result_label.config(text=f"Hello, {name}!")

window=tk.Tk()
window.title("My Tkinter First App")
window.geometry("500x500")
window.config(bg="Blue")
button=tk.Button(window,text="Click me" ,command=firstProg)
button.pack()
button=tk.Button(window,text="Submit" ,command=show_name)
button.pack()
label=tk.Label(window,text="Enter your name")
label.pack(pady=10)
entry = tk.Entry(window)
entry.pack()
result_label = tk.Label(window, text="")
result_label.pack(pady=5)
window.mainloop()