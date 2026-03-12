# import tkinter as tk
# from tkinter import messagebox
# import random

# class RockPaperScissorsGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Rock, Paper, Scissors Game")
        
#         # Label for instructions
#         self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
#         self.label.pack(pady=20)
        
#         # Buttons for choices
#         self.rock_button = tk.Button(self.root, text="Rock", font=("Arial", 14), command=lambda: self.player_choice("Rock"))
#         self.rock_button.pack(side=tk.LEFT, padx=20, pady=20)
        
#         self.paper_button = tk.Button(self.root, text="Paper", font=("Arial", 14), command=lambda: self.player_choice("Paper"))
#         self.paper_button.pack(side=tk.LEFT, padx=20, pady=20)
        
#         self.scissors_button = tk.Button(self.root, text="Scissors", font=("Arial", 14), command=lambda: self.player_choice("Scissors"))
#         self.scissors_button.pack(side=tk.LEFT, padx=20, pady=20)
        
#         # Label for result display
#         self.result_label = tk.Label(self.root, text="Your choice will appear here!", font=("Arial", 12))
#         self.result_label.pack(pady=20)
        
#     def player_choice(self, player_choice):
#         # Computer makes a random choice
#         computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        
#         # Determine the winner
#         winner = self.determine_winner(player_choice, computer_choice)
        
#         # Show the choices and result
#         self.result_label.config(text=f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\nResult: {winner}")
    
#     def determine_winner(self, player_choice, computer_choice):
#         # Determine the winner based on the rules of Rock, Paper, Scissors
#         if player_choice == computer_choice:
#             return "It's a tie!"
#         elif (player_choice == "Rock" and computer_choice == "Scissors") or \
#              (player_choice == "Paper" and computer_choice == "Rock") or \
#              (player_choice == "Scissors" and computer_choice == "Paper"):
#             return "You win!"
#         else:
#             return "Computer wins!"

# # Create the main window
# root = tk.Tk()
# game = RockPaperScissorsGame(root)
# root.mainloop()



# import random

# def game():                                                                                                                                                                                                                                    
#     choices = ["rock", "paper", "scissors"]
#     # Get the user's choice
#     user_choice = input("Enter rock, paper, or scissors: ").lower()
    
#     # Randomly pick the computer's choice
#     computer_choice = random.choice(choices)
    
#     print(f"Computer chose: {computer_choice}")
    
#     # Determine the winner
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "scissors" and computer_choice == "paper") or \
#          (user_choice == "paper" and computer_choice == "rock"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# # Main loop for playing multiple rounds
# def play_again():
#     while True:
#         print(game())  # Run the game
#         play = input("Do you want to play again? (yes/no): ").lower()
#         if play != "yes":
#             print("Thanks for playing!")
#             break

# # Start the game
# play_again()