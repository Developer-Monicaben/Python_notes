import ttkbootstrap as tb
from Quiz import QuizUI
from Dashboard import Dashboard
from Login import LoginPage

def launch_dashboard(name, roll):
    root = tb.Window(themename="cosmo")

    if name.lower() == "admin":
        root.title("Admin Dashboard")
        Dashboard(root)
    else:
        root.title(f"{name}'s Quiz")
        QuizUI(root, student_name=name, student_roll=roll)
        

    root.mainloop()

if __name__ == "__main__":
    root = tb.Window(themename="cosmo")  # Themes: flatly, darkly, minty, cyborg, journal, etc.
    root.title("SmartCampus360 - Student Dashboard")
    root.geometry("1000x700")
    app = Dashboard(root)
    root.mainloop()
