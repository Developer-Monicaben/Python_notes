import ttkbootstrap as tb
from tkinter import messagebox
import pandas as pd


class LoginPage:
    def __init__(self, root, on_login_success):
        self.root = root
        self.root.title("Login - SmartCampus360")

        frame = tb.Frame(root, padding=30)
        frame.pack(pady=100)

        tb.Label(frame, text="Name", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        tb.Label(frame, text="Roll No", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)

        self.name_entry = tb.Entry(frame, width=30, bootstyle="info")
        self.roll_entry = tb.Entry(frame, width=30, bootstyle="info")

        self.name_entry.grid(row=0, column=1)
        self.roll_entry.grid(row=1, column=1)

        tb.Button(frame, text="Login", bootstyle="success", command=self.login_user)\
            .grid(row=2, columnspan=2, pady=20)

        self.on_login_success = on_login_success

    def login_user(self):
        name = self.name_entry.get().strip()
        roll = self.roll_entry.get().strip()

        if not name or not roll:
            messagebox.showwarning("Input Error", "Please enter both Name and Roll No.")
            return

        # Check for admin login (hardcoded)
        if name.lower() == "admin" and roll == "5687":
            self.on_login_success("admin", "5687")
            return

        try:
            df = pd.read_csv("data/students.csv")
            match = df[(df["Name"].str.strip().str.lower() == name.lower()) &
                       (df["Roll"].astype(str).str.strip() == roll)]

            if not match.empty:
                self.on_login_success(name, roll)
            else:
                messagebox.showerror("Login Failed", "Student not found. Please check your name and roll number.")

        except Exception as e:
            messagebox.showerror("Error", f"Could not read student file:\n{e}")
