# Tkinter is the standard Python library for creating Graphical User Interfaces (GUIs).
# It provides tools to create windows, buttons, labels, text boxes, and more.
# Built-in with Python (no need to install separately)
# Simple and beginner-friendly

import tkinter as tk

# window = tk.Tk()
# window.title("My First GUI")
# window.geometry("300x200")
# label = tk.Label(window, text="Hello, Tkinter!")
# label.pack()
# window.mainloop()
             
# Tkinter components 
# Label – Displays text:
# Button – A clickable button:
# Entry – Single-line text input:
# Text – Multi-line text input:
# Checkbutton – Checkbox: 
# Radiobutton – Radio buttons for options:
# Listbox – List of selectable items:


# Basic login form using Label, Entry, and Button.

# from tkinter import messagebox

# def login():
#     username = user_entry.get()
#     password = pass_entry.get()
#     if username == "admin" and password == "1234":
#         messagebox.showinfo("Login", "Login Successful!")
#     else:
#         messagebox.showerror("Login", "Invalid credentials")

# window = tk.Tk()
# window.title("Login Form")
# window.geometry("300x200")
# 23
# tk.Label(window, text="Username").pack(pady=10)
# user_entry = tk.Entry(window)
# user_entry.pack()

# tk.Label(window, text="Password").pack(pady=10)
# pass_entry = tk.Entry(window)
# pass_entry.pack()

# tk.Button(window, text="Login", command=login).pack(pady=10)
# # window.bind("<Return>", login)
# window.mainloop()

# ===========================================================================

# #event-->events allow you to make your application interactive.
# #An event is something that the user does, like clicking a button, pressing a key, or moving the mouse.

# import tkinter as tk
 
# def on_click(event):
#     print("Button clicked!")

# def on_key_press(event):
#     print(f" {event.char}")

# window = tk.Tk()
# window.geometry("300x200")

# # Button click event
# btn = tk.Button(window, text="Click Me")
# btn.bind("<Button-1>", on_click)  # Left mouse click
# btn.pack(pady=10)

# # Key press event (bind to window)
# window.bind("<Key>", on_key_press)
# # window.bind("<Return>", on_click)
# window.focus_set()
# window.mainloop()

# =================================================
# Adding button 

# def on_button_click():
#     print("Button clicked!")


# # Create the root window
# root = tk.Tk()
# root.title("Grid Layout Example")
# root.geometry("300x200")

# # Label 1
# label1 = tk.Label(root, text="Label 1")
# label1.grid(row=0, column=0, padx=10, pady=10)  # Placed at row 0, column 0

# # Label 2
# label2 = tk.Label(root, text="Label 2")
# label2.grid(row=0, column=1, padx=10, pady=10)  # Placed at row 0, column 1

# # Button
# button = tk.Button(root, text="Click Me", command=on_button_click)
# button.grid(row=1, column=0, columnspan=2, pady=20)  # Spans 2 columns, placed at row 1

# # Start the event loop
# root.mainloop()

# # =======================================================================================

# Entry widgets 

# root = tk.Tk()
# root.geometry("400x300")

# # Create a Text widget
# text_widget = tk.Text(root, height=10, width=40)
# text_widget.pack(pady=10)

# # Insert text into the Text widget
# text_widget.insert(tk.END, "This is a multi-line Text widget.\nYou can edit this text.")

# root.mainloop()

# # # ==========================================
# Check button 

# def show_selection():
#     print("Checkbutton state:", check_var.get())
    
# root = tk.Tk()

# # Variable to hold the state of the Checkbutton (0 for unchecked, 1 for checked)
# check_var = tk.IntVar()

# # Create a Checkbutton
# check_button = tk.Checkbutton(root, text="Accept Terms", variable=check_var)
# check_button.pack(pady=10)

# # Button to print the Checkbutton state
# btn = tk.Button(root, text="Submit", command=show_selection)
# btn.pack()

# root.mainloop()

# # # =============================
# Radio button 


# def show_selection():
#     print("Selected option:", radio_var.get())

# root = tk.Tk()

# # Variable to hold the selected radio button value
# radio_var = tk.StringVar()

# # Create Radio Buttons
# radio_button1 = tk.Radiobutton(root, text="Male", value="male", variable=radio_var)
# radio_button2 = tk.Radiobutton(root, text="Female", value="female", variable=radio_var)
# radio_button1.pack()
# radio_button2.pack()

# # Button to show the selected radio option
# btn = tk.Button(root, text="Submit", command=show_selection)
# btn.pack(pady=10)

# root.mainloop()


# # ===================================================
# # Combo-box


# from tkinter import ttk

# def show_selection():
#     print("Selected option:", combo.get())

# root = tk.Tk()

# # Create a Combobox
# combo = ttk.Combobox(root, values=["Option 1","Option 2", "Option 3"])
# combo.pack(pady=10)

# btn = tk.Button(root, text="Submit", command=show_selection)
# btn.pack(pady=1)

# root.mainloop()

# #
# # =================================================
# Combine 

# import tkinter as tk
# from tkinter import messagebox, ttk

# def show_message():
#     messagebox.showinfo("Message", "This is a message box.")

# def show_selection():
#     print("Radio selection:", radio_var.get())
#     print("Checkbutton state:", check_var.get())
#     print("Combo selection:", combo.get())
#     print("Text area :",text_widget.get(1.0,tk.END))

# root = tk.Tk()
# root.title("Widgets Example")
# root.geometry("400x400")

# # Label
# label = tk.Label(root, text="Tkinter Widgets Example", font=("Arial", 18))
# label.pack(pady=10)

# # Text widget3
# text_widget = tk.Text(root, height=5, width=40)
# text_widget.insert(tk.END, "Enter your message here...")
# text_widget.pack(pady=10)

# # Checkbutton
# check_var = tk.IntVar()
# check_button = tk.Checkbutton(root, text="Accept Terms", variable=check_var)
# check_button.pack()

# # Radio Buttons
# radio_var = tk.StringVar()
# radio_button1 = tk.Radiobutton(root, text="Option 1", value="1", variable=radio_var)
# radio_button2 = tk.Radiobutton(root, text="Option 2", value="2", variable=radio_var)
# radio_button1.pack()
# radio_button2.pack()

# #Combobox
# combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
# combo.set("Select the option")
# combo.pack(pady=10)

# # Buttons
# btn_show = tk.Button(root, text="Show Message", command=show_message)
# btn_show.pack(pady=5)

# btn_submit = tk.Button(root, text="Submit", command=show_selection)
# btn_submit.pack(pady=10)

# root.mainloop()

# # ============================================

# Add image in GUI 

# import tkinter as tk

# root = tk.Tk()

# # Load image (must be .png or .gif)
# image = tk.PhotoImage(file="PythonImage.Png,GIF")

# # Create label with image
# img_label = tk.Label(root, image=image)
# img_label.pack()

# root.mainloop()

# # ==============================================pip install Pillow

# from tkinter import Tk, Label
# from PIL import Image, ImageTk

# root = Tk()
# root.geometry("300x300") 

# # Load JPG image
# img = Image.open("ImageOfNature.jpg")
# img = img.resize((200, 200))  # Optional: resize the image

# # Convert to Tkinter-compatible image
# tk_img = ImageTk.PhotoImage(img)

# # Display image
# label = Label(root, image=tk_img)
# label.pack()

# root.mainloop()

# # ===========================================
# Speech recognition -->pip install SpeechRecognition,pip install PyAudio

# import tkinter as tk
# import speech_recognition as sr
# from tkinter import messagebox


# def recognize_speech():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         status_label.config(text="Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             text = recognizer.recognize_google(audio)
#             result_box.delete(1.0, tk.END)
#             result_box.insert(tk.END,text)
#             status_label.config(text="Done!")
#         except sr.UnknownValueError:
#             messagebox.showerror("Error", "Could not understand audio")
#         except sr.RequestError:
#             messagebox.showerror("Error", "Speech service failed")
#         except sr.WaitTimeoutError:
#             messagebox.showerror("Error", "Listening timed out")

# # # GUI setup
# window = tk.Tk()
# window.title("Speech Recognition GUI")
# window.geometry("400x300")

# tk.Button(window, text="Start Listening", command=recognize_speech).pack(pady=10)
# result_box = tk.Text(window, height=10, width=40)
# result_box.pack(pady=10)
# status_label = tk.Label(window, text="")
# status_label.pack()

# window.mainloop()

# # ==============================================

# # GUI Generate QR code   -->pip install qrcode[pil]

# import qrcode

# # Link to encode (it can be any website link or any upi)
# data = "https://www.google.com"

# # Generate QR code
# qr = qrcode.make(data)   # make function --> create a qr code for this link
                     
# # Save as image file
# qr.save("google_qr.png")

# # Optional: Show the QR code
# qr.show()

# ============================