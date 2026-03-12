# pip install pandas
# pip install openpyxl

import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import re

# Load employee data
df = pd.read_excel("Employee_Data.xlsx")
df = df.rename(columns={"Salary (₹)": "Salary"})

# GUI setup
root = tk.Tk()
root.title("💼 Smart Employee Report System")
root.geometry("1100x600")
root.configure(bg="#dff6f0")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#009879", foreground="white")
style.configure("Treeview", font=("Arial", 11), rowheight=26, background="white", fieldbackground="white")
style.map('Treeview', background=[('selected', '#75c9b7')])

# Control Frame
control_frame = tk.Frame(root, bg="#c0e5dc")
control_frame.pack(fill="x", padx=10, pady=10)

title_label = tk.Label(control_frame, text="📊 Employee Report Dashboard", font=("Arial", 16, "bold"), bg="#c0e5dc")
title_label.pack(pady=5)

search_label = tk.Label(control_frame, text="🔍 Search:", font=("Arial", 12), bg="#c0e5dc")
search_label.pack(side="left", padx=(10, 5))

search_entry = ttk.Entry(control_frame, width=40)
search_entry.pack(side="left", padx=5)

def display_data(data):
    tree.delete(*tree.get_children())
    for _, row in data.iterrows():
        tree.insert("", "end", values=[
            row["EmployeeID"],
            row["Name"],
            row.get("Salary (₹)", row.get("Salary")),
            row["Experience (Years)"],
            row["Mobile Number"],
            row["Email ID"]
        ])

def search_data():
    query = search_entry.get().strip()
    result = pd.DataFrame()

    if not query:
        result = df.copy()
    elif re.match(r'(>=|<=|==|>|<)\s*\d+', query):
        try:
            result = df.query(f"Salary {query}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid condition: {e}")
            return
    else:
        for col in df.columns:
            match = df[df[col].astype(str).str.contains(query, case=False, na=False)]
            if not match.empty:
                result = match
                break

    if result.empty:
        messagebox.showinfo("No Results", f"No match found for '{query}'")
    else:
        display_data(result)

def apply_bonus():
    try:
        bonus_str = simpledialog.askstring("Bonus", "Enter bonus percentage (%):")
        if bonus_str:
            bonus = float(bonus_str)
            filtered = df.copy()
            filtered["Salary (₹)"] = filtered["Salary"] * (1 + bonus / 100)
            display_data(filtered)
    except Exception:
        messagebox.showerror("Error", "Invalid bonus amount")

def export_excel():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        rows = [tree.item(child)["values"] for child in tree.get_children()]
        columns = ["EmployeeID", "Name", "Salary (₹)", "Experience (Years)", "Mobile Number", "Email ID"]
        export_df = pd.DataFrame(rows, columns=columns)
        export_df.to_excel(file_path, index=False)
        messagebox.showinfo("Exported", f"Report saved to:\n{file_path}")

# Buttons
tk.Button(control_frame, text="Search", command=search_data, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=10)
tk.Button(control_frame, text="Apply Bonus", command=apply_bonus, bg="#007BFF", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=10)
tk.Button(control_frame, text="Export Excel", command=export_excel, bg="#F44336", fg="white", font=("Arial", 10, "bold")).pack(side="right", padx=10)

# Treeview setup
columns = ["EmployeeID", "Name", "Salary (₹)", "Experience (Years)", "Mobile Number", "Email ID"]
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180)

tree.pack(fill="both", expand=True, padx=10, pady=10)
display_data(df)

root.mainloop()


