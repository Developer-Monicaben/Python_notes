import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import ttkbootstrap as tb

class AnalyticsUI:
    def __init__(self, parent):
        frame = tb.Frame(parent)
        frame.pack(pady=30)

        try:
            df = pd.read_csv("data/students.csv")

            if "Score" not in df.columns:
                df["Score"] = 0
            df["Score"] = df["Score"].fillna(0).astype(int)

            names = df["Name"].tolist()
            scores = df["Score"].tolist()

            if not any(scores):
                tb.Label(frame, text="No scores available yet.", font=("Arial", 12)).pack()
                return

            # ✅ Set emoji-friendly font before plotting
            plt.rcParams['font.family'] = 'Segoe UI Emoji'

            fig, ax = plt.subplots(figsize=(8, 4))

            bars = ax.bar(names, scores, color="#5DADE2", width=0.6, edgecolor="black")

            ax.set_title("📊 Student Quiz Scores", fontsize=14, weight='bold')
            ax.set_ylabel("Score (out of 10)", fontsize=12)
            ax.set_ylim(0, 10)

            ax.set_xticks(range(len(names)))
            ax.set_xticklabels(names, rotation=45, ha="right")

            # 🏆 Highlight top scorer
            max_score = max(scores)
            for bar, score in zip(bars, scores):
                if score == max_score and max_score > 0:
                    ax.text(bar.get_x() + bar.get_width()/2, score + 0.2, "🏆", ha="center", fontsize=14)
                ax.text(bar.get_x() + bar.get_width()/2, score - 0.5, str(score), ha="center", fontsize=10, color="white")

            fig.tight_layout()

            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.get_tk_widget().pack()

        except Exception as e:
            tb.Label(frame, text=f"Error loading chart: {e}", bootstyle="danger").pack()
