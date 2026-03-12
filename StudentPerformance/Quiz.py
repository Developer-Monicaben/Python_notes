import ttkbootstrap as tb
from tkinter import messagebox
import pandas as pd

questions = [
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["def", "func", "function", "define"],
        "answer": "def"
    },
    {
        "question": "What data type is the result of: 3 / 2 in Python 3?",
        "options": ["int", "float", "double", "str"],
        "answer": "float"
    },
    {
        "question": "What does 'len([1,2,3])' return?",
        "options": ["2", "3", "1", "Error"],
        "answer": "3"
    },
    {
        "question": "Which symbol is used to comment a single line in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
    "question": "Which of the following is mutable?",
    "options": ["tuple", "str", "list", "int"],
    "answer": "list"
    },
    {
        "question": "What is the output of: bool('False')?",
        "options": ["True", "False", "None", "Error"],
        "answer": "True"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["/", "//", "%", "^"],
        "answer": "//"
    },
    {
        "question": "Which built-in function returns the length of a list?",
        "options": ["count()", "length()", "len()", "size()"],
        "answer": "len()"
    },
    {
        "question": "What is the default return value of a function that doesn’t return anything?",
        "options": ["None", "0", "False", "Empty string"],
        "answer": "None"
    }

      ]

class QuizUI:
    def __init__(self, root, student_name, student_roll):
        self.root = root
        self.student_name = student_name
        self.student_roll = student_roll
        self.index = 0
        self.score = 0
        self.answers = []

        self.frame = tb.Frame(root, padding=20)
        self.frame.pack()

        self.question_label = tb.Label(self.frame, text="", wraplength=600, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.selected_option = tb.StringVar()
        self.option_buttons = []
        for _ in range(4):
            btn = tb.Radiobutton(self.frame, text="", variable=self.selected_option,
                                 value="", bootstyle="info")
            btn.pack(anchor="w", pady=5)
            self.option_buttons.append(btn)

        self.next_btn = tb.Button(self.frame, text="Next", command=self.next_question, bootstyle="primary")
        self.next_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        q = questions[self.index]
        self.question_label.config(text=f"Q{self.index + 1}. {q['question']}")
        self.selected_option.set(None)
        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option.")
            return

        correct = questions[self.index]["answer"]
        self.answers.append((questions[self.index]["question"], selected, correct))
        if selected == correct:
            self.score += 1

        self.index += 1
        if self.index < len(questions):
            self.load_question()
        else:
            self.show_result()


    def show_result(self):
        self.frame.destroy()

        # ===== Scrollable Frame Setup =====
        container = tb.Frame(self.root)
        canvas = tb.Canvas(container)
        scrollbar = tb.Scrollbar(container, orient="vertical", command=canvas.yview)
        scroll_frame = tb.Frame(canvas)

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        # ===================================

        tb.Label(scroll_frame, text=f"✅ {self.student_name} - Quiz Completed!", font=("Arial", 16)).pack(pady=10)
        tb.Label(scroll_frame, text=f"🎯 Score: {self.score} / {len(questions)}", font=("Arial", 14)).pack(pady=10)

        for i, (q, selected, correct) in enumerate(self.answers):
            color = "success" if selected == correct else "danger"
            status = "✔️ Correct" if selected == correct else f"❌ Wrong (Ans: {correct})"
            tb.Label(scroll_frame, text=f"{i+1}. {q}\nYour Answer: {selected} — {status}",
                    bootstyle=color, wraplength=800, justify="left").pack(anchor="w", pady=5)

        self.save_score()


        