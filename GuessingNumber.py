import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
        self.attempts = 0
        
        # Label and entry field for the user's guess
        self.label = tk.Label(self.root, text="Guess the number between 1 and 100", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)
        
        # Button to check the guess
        self.check_button = tk.Button(self.root, text="Check Guess", font=("Arial", 14), command=self.check_guess)
        self.check_button.pack(pady=10)
        
        # Label to show attempts
        self.attempts_label = tk.Label(self.root, text="Attempts: 0", font=("Arial", 12))
        self.attempts_label.pack(pady=10)
        
    def check_guess(self):
        user_guess = int(self.entry.get())  # Get the user's guess from the entry field
        self.attempts += 1  # Increment attempt count
        
        # Check if the guess is correct, too high, or too low
        if user_guess < self.number_to_guess:
            messagebox.showinfo("Try Again", "Your guess is too low! Try again.")
        elif user_guess > self.number_to_guess:
            messagebox.showinfo("Try Again", "Your guess is too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.attempts} attempts.")
            self.reset_game()  # Reset the game after winning
        
        # Update the attempts label
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        
        # Clear the entry field
        self.entry.delete(0, tk.END)
    
    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)  # Reset the number
        self.attempts = 0  # Reset attempts count
        self.attempts_label.config(text="Attempts: 0")  # Reset attempts label

# Create the main window
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()

