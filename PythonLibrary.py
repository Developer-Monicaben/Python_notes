import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = None

def load_csv():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        text.delete("1.0", tk.END)
        text.insert(tk.END, str(df.describe()))

def show_numpy_stats():
    if df is not None:
        marks = df.drop("Name", axis=1).values
        mean = np.mean(marks)
        max_ = np.max(marks)
        min_ = np.min(marks)
        text.delete("1.0", tk.END)
        text.insert(tk.END, f"NumPy Stats:\nMean: {mean}\nMax: {max_}\nMin: {min_}")
    else:
        messagebox.showerror("Error", "Please load a CSV file first.")

def plot_graph():
    if df is not None:
        df.drop("Name", axis=1).mean().plot(kind='bar')
        plt.title("Average Marks by Subject")
        plt.ylabel("Marks")
        plt.show()
    else:
        messagebox.showerror("Error", "Please load a CSV file first.")

# GUI setup
root = tk.Tk()
root.title("Student Marks Analyzer")

tk.Button(root, text="Load CSV", command=load_csv).pack(pady=5)
tk.Button(root, text="Show NumPy Stats", command=show_numpy_stats).pack(pady=5)
tk.Button(root, text="Plot Subject Averages", command=plot_graph).pack(pady=5)

text = tk.Text(root, height=12, width=60)
text.pack(pady=10)

root.mainloop()
