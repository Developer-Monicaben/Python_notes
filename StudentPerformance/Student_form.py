import ttkbootstrap as tb
import pandas as pd
import os
from tkinter import messagebox

class StudentForm:
    def __init__(self, parent):
        self.frame = tb.Frame(parent)
        self.frame.pack(pady=30)

        tb.Label(self.frame, text="Name", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        tb.Label(self.frame, text="Roll No", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)

        self.name_entry = tb.Entry(self.frame, width=30, bootstyle="info")
        self.roll_entry = tb.Entry(self.frame, width=30, bootstyle="info")

        self.name_entry.grid(row=0, column=1)
        self.roll_entry.grid(row=1, column=1)

        tb.Button(self.frame, text="Save Student", bootstyle="success", command=self.save_student)\
            .grid(row=2, columnspan=2, pady=10)

        tb.Button(self.frame, text="📋 View All Students", bootstyle="info", command=self.view_students)\
            .grid(row=3, columnspan=2, pady=10)

    def save_student(self):
        name = self.name_entry.get().strip()
        roll = self.roll_entry.get().strip()

        if not name or not roll:
            messagebox.showwarning("Input Error", "Please fill both Name and Roll No.")
            return

        try:
            # Load existing student data if file exists
            try:
                df = pd.read_csv("data/students.csv")
                df["Roll"] = df["Roll"].astype(str).str.strip()
            except FileNotFoundError:
                df = pd.DataFrame(columns=["Name", "Roll", "Score"])

            if roll in df["Roll"].values:
                messagebox.showerror("Duplicate Roll No", f"Roll number '{roll}' already exists!")
                return

            new_row = pd.DataFrame([[name, roll, 0]], columns=["Name", "Roll", "Score"])
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv("data/students.csv", index=False)

            messagebox.showinfo("Success", f"Student '{name}' saved successfully!")
            self.name_entry.delete(0, 'end')
            self.roll_entry.delete(0, 'end')

        except Exception as e:
            messagebox.showerror("Error", f"Could not save student: {str(e)}")

    def view_students(self):
        try:
            df = pd.read_csv("data/students.csv")

            view_window = tb.Toplevel(self.frame)
            view_window.title("Student Records")
            view_window.geometry("700x400")

            tree = tb.Treeview(view_window, columns=("Name", "Roll", "Score", "Quiz", "Chart"), show="headings")
            tree.heading("Name", text="Name")
            tree.heading("Roll", text="Roll No")
            tree.heading("Score", text="Score")
            tree.heading("Quiz", text="📝 Quiz")
            tree.heading("Chart", text="📈 Chart")

            tree.column("Quiz", width=60, anchor="center")
            tree.column("Chart", width=60, anchor="center")

            for _, row in df.iterrows():
                tree.insert("", "end", values=(row["Name"], row["Roll"], row["Score"], "📝", "📈"))

            tree.pack(expand=True, fill="both", padx=10, pady=10)

            def on_item_click(event):
                selected = tree.focus()
                values = tree.item(selected, 'values')
                col = tree.identify_column(event.x)
                if not selected: return

                if col == '#4':
                    messagebox.showinfo("Quiz", f"Launch quiz for {values[0]} (Roll: {values[1]})")
                    # TODO: connect to student-specific quiz

                elif col == '#5':
                    messagebox.showinfo("Chart", f"Show analytics for {values[0]}")
                    # TODO: connect to student-specific chart

            tree.bind("<Button-1>", on_item_click)

        except Exception as e:
            messagebox.showerror("Error", f"Could not load student data:\n{e}")
