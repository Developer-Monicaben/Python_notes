import ttkbootstrap as tb
from Quiz import QuizUI
from Analytics import AnalyticsUI
from Student_form import StudentForm

class Dashboard:
    def __init__(self, master):
        self.master = master

        style = tb.Style()
        # style.configure("Dashboard.TFrame", background="lightgrey")
        # style.configure("CustomEntry.TEntry", fieldbackground="lightgrey", background="lightgrey")

        self.tabControl = tb.Notebook(master, bootstyle="primary")
        self.tab1 = tb.Frame(self.tabControl, padding=20, style="Dashboard.TFrame")
        self.tab2 = tb.Frame(self.tabControl, padding=20, style="Dashboard.TFrame")
        self.tab3 = tb.Frame(self.tabControl, padding=20, style="Dashboard.TFrame")

        self.tabControl.add(self.tab1, text='📚 Student Info')
        self.tabControl.add(self.tab2, text='🗘️ Quiz')
        self.tabControl.add(self.tab3, text='📈 Analytics')
        self.tabControl.pack(expand=1, fill="both")

        StudentForm(self.tab1)
        QuizUI(self.tab2, student_name="test", student_roll="000")
        AnalyticsUI(self.tab3)

if __name__ == '__main__':
    root = tb.Window(themename="cosmo")  # Use a professional theme
    app = Dashboard(root)
    root.mainloop()
