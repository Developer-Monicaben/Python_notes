import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np

# Store item data
item_names = []
item_prices = []
item_quantities = []
item_units = []

def add_item():
    name = name_entry.get()
    unit = unit_var.get()
    try:
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")
        return

    if name.strip() == "":
        messagebox.showwarning("Missing Item", "Item name cannot be empty.")
        return

    item_names.append(name)
    item_prices.append(price)
    item_quantities.append(quantity)
    item_units.append(unit)

    total = price * quantity
    tree.insert('', 'end', values=(name, f"₹{price:.2f}", quantity, unit, f"₹{total:.2f}"))

    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def show_total():
    total = sum([p * q for p, q in zip(item_prices, item_quantities)])
    messagebox.showinfo(" Total Price", f"Total Bill: ₹{total:.2f}")

def filter_by_threshold():
    condition = threshold_entry.get().strip()
    if not condition:
        messagebox.showerror("Input Error", "Please enter a condition like >200 or <150.")
        return

    try:
        operator = condition[0]
        amount = float(condition[1:])
    except:
        messagebox.showerror("Input Error", "Invalid format. Use >200, <150, =300, etc.")
        return

    filtered = []
    for i in range(len(item_prices)):
        total = item_prices[i] * item_quantities[i]
        if (operator == '>' and total > amount) or \
           (operator == '<' and total < amount) or \
           (operator == '=' and total == amount):
            filtered.append((item_names[i], item_prices[i], item_quantities[i], item_units[i], total))

    if not filtered:
        messagebox.showinfo("🔍 Filter Result", "No items matched the condition.")
        return

    win = tk.Toplevel(root)
    win.title("🔍 Filtered Items")
    win.geometry("700x350")

    tree_filter = ttk.Treeview(win, columns=("Name", "Price", "Qty", "Unit", "Total"), show='headings')
    for col in ["Name", "Price", "Qty", "Unit", "Total"]:
        tree_filter.heading(col, text=col)
    tree_filter.pack(fill=tk.BOTH, expand=True)

    for row in filtered:
        tree_filter.insert('', 'end', values=(row[0], f"₹{row[1]:.2f}", row[2], row[3], f"₹{row[4]:.2f}"))

def show_full_summary():
    if not item_prices:
        messagebox.showinfo("No Data", "No items added.")
        return

    summary_window = tk.Toplevel(root)
    summary_window.title("📊 Detailed Summary")
    summary_window.geometry("800x400")

    summary_tree = ttk.Treeview(summary_window, columns=("Name", "Price", "Quantity", "Unit", "Total"), show='headings')
    for col in ["Name", "Price", "Quantity", "Unit", "Total"]:
        summary_tree.heading(col, text=col)
    summary_tree.pack(fill=tk.BOTH, expand=True)

    total_prices = []

    for name, price, qty, unit in zip(item_names, item_prices, item_quantities, item_units):
        total = price * qty
        total_prices.append(total)
        summary_tree.insert('', 'end', values=(name, f"₹{price:.2f}", qty, unit, f"₹{total:.2f}"))

    max_price = max(item_prices)
    min_price = min(item_prices)
    max_index = item_prices.index(max_price)
    min_index = item_prices.index(min_price)
    total_bill = sum(total_prices)

    analysis = f"""
📌 Highest Price Product: {item_names[max_index]} (₹{max_price:.2f})
📌 Lowest Price Product: {item_names[min_index]} (₹{min_price:.2f})
🧾 Total Bill (all items): ₹{total_bill:.2f}
    """

    tk.Label(summary_window, text=analysis, font=("Helvetica", 12), justify="left", bg="#fff8dc").pack(pady=10, fill=tk.X)

def show_highest_price():
    if not item_prices:
        messagebox.showinfo("No Data", "No items added yet.")
        return
    max_price = max(item_prices)
    index = item_prices.index(max_price)
    total = max_price * item_quantities[index]
    messagebox.showinfo(
        "📈 Highest Price Item",
        f"Item: {item_names[index]}\nPrice: ₹{max_price:.2f}\nQuantity: {item_quantities[index]} {item_units[index]}\nTotal: ₹{total:.2f}"
    )

def show_lowest_price():
    if not item_prices:
        messagebox.showinfo("No Data", "No items added yet.")
        return
    min_price = min(item_prices)
    index = item_prices.index(min_price)
    total = min_price * item_quantities[index]
    messagebox.showinfo(
        "📉 Lowest Price Item",
        f"Item: {item_names[index]}\nPrice: ₹{min_price:.2f}\nQuantity: {item_quantities[index]} {item_units[index]}\nTotal: ₹{total:.2f}"
    )

def show_most_sold():
    if not item_quantities:
        messagebox.showinfo("No Data", "No items added yet.")
        return
    max_qty = max(item_quantities)
    index = item_quantities.index(max_qty)
    price = item_prices[index]
    total = price * max_qty
    messagebox.showinfo(
        "📦 Most Sold Item",
        f"Item: {item_names[index]}\nQuantity Sold: {max_qty} {item_units[index]}\nUnit Price: ₹{price:.2f}\nTotal: ₹{total:.2f}"
    )

def show_least_sold():
    if not item_quantities:
        messagebox.showinfo("No Data", "No items added yet.")
        return
    min_qty = min(item_quantities)
    index = item_quantities.index(min_qty)
    price = item_prices[index]
    total = price * min_qty
    messagebox.showinfo(
        "📉 Least Sold Item",
        f"Item: {item_names[index]}\nQuantity Sold: {min_qty} {item_units[index]}\nUnit Price: ₹{price:.2f}\nTotal: ₹{total:.2f}"
    )

# GUI setup
root = tk.Tk()
root.title("🛒 NumPy Supermarket Billing System")
root.geometry("850x680")
root.configure(bg="#f0f8ff")

tk.Label(root, text="🛒 NumPy Supermarket Billing", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#003366").pack(pady=10)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

# Item Name
tk.Label(frame, text="Item Name:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, font=("Helvetica", 12))
name_entry.grid(row=0, column=1, padx=5)

# Unit Price & Unit (in same row)
tk.Label(frame, text="Unit Price (₹):", font=("Helvetica", 12), bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5)
price_entry = tk.Entry(frame, font=("Helvetica", 12), width=10)
price_entry.grid(row=1, column=1, sticky="w", padx=(5, 0))

unit_var = tk.StringVar()
unit_var.set("kg")
unit_menu = ttk.Combobox(frame, textvariable=unit_var, values=["kg", "liter", "packet", "piece", "dozen"], state="readonly", font=("Helvetica", 12), width=10)
unit_menu.grid(row=1, column=1, sticky="e", padx=(0, 5))

# Quantity
tk.Label(frame, text="Quantity:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=2, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(frame, font=("Helvetica", 12))
quantity_entry.grid(row=2, column=1, padx=5)

tk.Button(frame, text="Add Item", font=("Helvetica", 12), bg="#28a745", fg="white", command=add_item).grid(row=3, column=0, columnspan=2, pady=10)

# Table
tree = ttk.Treeview(root, columns=("Name", "Price", "Quantity", "Unit", "Total"), show='headings', height=10)
for col in ["Name", "Price", "Quantity", "Unit", "Total"]:
    tree.heading(col, text=col)
tree.pack(pady=10)

# Price & Quantity Analysis
price_btn_frame = tk.Frame(root, bg="#f0f8ff")
price_btn_frame.pack(pady=5)

tk.Button(price_btn_frame, text="📈 Highest Price Item", font=("Helvetica", 11), bg="#17a2b8", fg="white", command=show_highest_price).grid(row=0, column=0, padx=10)
tk.Button(price_btn_frame, text="📉 Lowest Price Item", font=("Helvetica", 11), bg="#fd7e14", fg="white", command=show_lowest_price).grid(row=0, column=1, padx=10)
tk.Button(price_btn_frame, text="📦 Most Sold Item", font=("Helvetica", 11), bg="#6f42c1", fg="white", command=show_most_sold).grid(row=0, column=2, padx=10)
tk.Button(price_btn_frame, text="📉 Least Sold Item", font=("Helvetica", 11), bg="#dc3545", fg="white", command=show_least_sold).grid(row=0, column=3, padx=10)

# Threshold input + summary
bottom_frame = tk.Frame(root, bg="#f0f8ff")
bottom_frame.pack()

tk.Label(bottom_frame, text="Enter threshold (e.g. >200):", font=("Helvetica", 12), bg="#f0f8ff").grid(row=0, column=0, padx=5)
threshold_entry = tk.Entry(bottom_frame, font=("Helvetica", 12))
threshold_entry.grid(row=0, column=1, padx=5)

tk.Button(bottom_frame, text="Show Summary", font=("Helvetica", 12), bg="#007bff", fg="white", command=show_full_summary).grid(row=1, column=0, columnspan=2, pady=10)

btn_frame2 = tk.Frame(root, bg="#f0f8ff")
btn_frame2.pack(pady=5)

tk.Button(btn_frame2, text="🧮 Show Total Price", font=("Helvetica", 12), bg="#20c997", fg="white", command=show_total).grid(row=0, column=0, padx=10)
tk.Button(btn_frame2, text="🔍 Filter by Threshold", font=("Helvetica", 12), bg="#6610f2", fg="white", command=filter_by_threshold).grid(row=0, column=1, padx=10)

root.mainloop()
