import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import threading
import pyttsx3
import time

# Load activities
with open('activities.json', 'r') as f:
    activities = json.load(f)

# CSV file to log moods
log_file = 'mood_log.csv'
if not os.path.exists(log_file):
    pd.DataFrame(columns=['Timestamp', 'Mood']).to_csv(log_file, index=False)

# Function to detect mood from text
def detect_mood():
    text = mood_input.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter your mood text.")
        return

    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0.1:
        mood = "Happy"
    elif sentiment < -0.1:
        mood = "Sad"
    else:
        mood = "Relaxed"

    mood_label.config(text=f"Detected Mood: {mood}")
    log_mood(mood)
    show_activities(mood)
    speak_mood(mood)

# Log mood to CSV (Pandas 2.x compatible)
def log_mood(mood):
    df = pd.read_csv(log_file)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = pd.DataFrame([{'Timestamp': timestamp, 'Mood': mood}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(log_file, index=False)

# Show activities
def show_activities(mood):
    acts = activities.get(mood, [])
    activity_text.set("Suggested Activities:\n" + "\n".join(acts[:3]))

# Threaded Text-to-Speech function
def speak_mood(mood):
    def tts():
        time.sleep(0.05)  # slight delay to prevent conflicts
        engine = pyttsx3.init()  # new engine for every call
        messages = {
            "Happy": "You are happy! Keep smiling and enjoy your day!",
            "Sad": "Feeling sad? Take a deep breath and relax.",
            "Relaxed": "You are relaxed. Keep enjoying the calm vibes.",
            "Energetic": "You are energetic! Channel your energy into a short workout."
        }
        message = messages.get(mood, f"You are feeling {mood}. Have a nice day!")
        engine.say(message)
        engine.runAndWait()
        engine.stop()
    threading.Thread(target=tts, daemon=True).start()

# Show mood analytics
def show_analytics():
    df = pd.read_csv(log_file)
    if df.empty:
        messagebox.showinfo("No Data", "No mood data available yet.")
        return
    counts = df['Mood'].value_counts()
    plt.figure(figsize=(6,4))
    counts.plot(kind='bar', color='skyblue')
    plt.title("Mood Distribution")
    plt.xlabel("Mood")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Tkinter GUI setup
root = tk.Tk()
root.title("Mood-Based Music & Activity Recommender")
root.geometry("500x500")

tk.Label(root, text="Enter your mood or thoughts:", font=("Arial", 12)).pack(pady=10)
mood_input = tk.Entry(root, width=50, font=("Arial", 12))
mood_input.pack(pady=5)

tk.Button(root, text="Detect Mood", font=("Arial", 12), command=detect_mood).pack(pady=10)
tk.Button(root, text="Show Mood Analytics", font=("Arial", 12), command=show_analytics).pack(pady=10)

mood_label = tk.Label(root, text="Detected Mood: None", font=("Arial", 12), fg="blue")
mood_label.pack(pady=10)

activity_text = tk.StringVar()
activity_text.set("Suggested Activities:\n")
tk.Label(root, textvariable=activity_text, font=("Arial", 12), justify="left").pack(pady=10)

root.mainloop()
