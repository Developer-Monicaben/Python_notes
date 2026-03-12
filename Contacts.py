#contact management system
import tkinter as tk
import mysql.connector
from tkinter import messagebox
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*30Pm28*",
    database="contacts_db"
)
cursor = conn.cursor()

def Add_Contacts():
    name = entry_name.get()
    MobileNumber = entry_phone.get()
    if not name or not MobileNumber:
        messagebox.showerror("Input Error", "Please enter both Name and Mobile Number.")
        
    if len(MobileNumber) != 10 or not MobileNumber.isdigit():
        messagebox.showerror("Input Error", "Mobile number must be exactly 10 digits.")
    else:
        messagebox.showinfo("Success", "Contact Added Succesfully !!")
        
    cursor.execute("INSERT INTO contacts (name, mobile) VALUES (%s, %s)", (name, MobileNumber))
    conn.commit()
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def View_Contacts():
    listBox.delete(0, tk.END)
    cursor.execute("SELECT id, name, mobile FROM contacts")
    for row in cursor.fetchall():
        listBox.insert(tk.END, f"{row[0]}:{row[1]} - {row[2]}")
    listBox.pack(pady=10, fill=tk.BOTH, expand=True)  


def Delete_Contact():
    selected = listBox.curselection()
    if selected:
        item = listBox.get(selected[0])
        contact_id = item.split(":")[0].strip()
        cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
        if cursor.rowcount:
            messagebox.showinfo("Success","Deleted successfully.")
        else:
            print("ID not found.")
        conn.commit()
        View_Contacts()

root = tk.Tk()
root.title("Contacts Information")
root.geometry("400x400")
root.configure(bg="#9CC6DB")  # Light blue background


title_label = tk.Label(root, text="Contact Management System", bg="#14eb31", fg="#2c3e50", font=("Arial", 16, "bold"))
title_label.pack(pady=10, fill='x')

# === Form Frame ===
form_frame = tk.Frame(root, bg="#f0f4f8")
form_frame.pack(pady=10)



tk.Label(form_frame, text="Name", bg="#f4f6f8", fg="#2c3e50", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_name = tk.Entry(form_frame, width=20, font=("Arial", 10))
entry_name.grid(row=0, column=1, pady=5, ipadx=5, ipady=3)

tk.Label(form_frame, text="Mobile", bg="#f0f4f8", fg="#2c3e50", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_phone = tk.Entry(form_frame, width=20, font=("Arial", 10))
entry_phone.grid(row=1, column=1, pady=5, ipadx=5, ipady=3)

# === Button Frame ===
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Add Contact", command=Add_Contacts, bg="#3498db", activebackground="#2980b9", font=("Arial", 10, "bold"))
btn_add.grid(row=0, column=0, padx=10)

btn_view = tk.Button(button_frame, text="View Contacts", command=View_Contacts, bg="#3498db", fg="white", activebackground="#2980b9", font=("Arial", 10, "bold"))
btn_view.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(button_frame, text="Delete", command=Delete_Contact, bg="#e74c3c", fg="white", activebackground="#c0392b", font=("Arial", 10, "bold"))
btn_delete.grid(row=0, column=2, padx=5)

# === Listbox ===
listBox = tk.Listbox(root, width=50, bg="white", fg="#2c3e50", font=("Consolas", 10), selectbackground="#3498db", selectforeground="white", borderwidth=2, relief="groove")

root.mainloop()
