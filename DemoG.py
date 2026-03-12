# import tkinter as tk
# import random

# def change_position():
#     button.place(x=random.randint(0, 250), y=random.randint(0, 250))

# window = tk.Tk()
# window.title("Catch Me! 🎯")
# window.geometry("300x300")

# button = tk.Button(window, text="Click Me!", command=change_position)
# button.place(x=100, y=100)

# window.mainloop()

# import tkinter as tk
# import random

# def change_color():
#     colors = ["red", "blue", "green", "yellow", "pink", "orange", "purple"]
#     window.config(bg=random.choice(colors))

# window = tk.Tk()
# window.title("Color Changer 🎨")
# window.geometry("400x400")

# button = tk.Button(window, text="Change Color!", command=change_color, font=("Arial", 20))
# button.pack(expand=True)

# window.mainloop()

# import tkinter as tk
# import random

# def move_star():
#     global star_y
#     star_y += 5
#     canvas.move(star, 0, 5)
#     if star_y > 400:
#         reset_star()
#     window.after(50, move_star)

# def reset_star():
#     global star_y
#     star_y = 0
#     new_x = random.randint(50, 350)
#     canvas.coords(star, new_x, star_y, new_x+30, star_y+30)

# def move_basket(event):
#     if event.keysym == "Left":
#         canvas.move(basket, -20, 0)
#     elif event.keysym == "Right":
#         canvas.move(basket, 20, 0)

# window = tk.Tk()
# window.title("Catch the Star ✨")
# window.geometry("400x400")

# canvas = tk.Canvas(window, width=400, height=400, bg="black")
# canvas.pack()

# # Create star
# star = canvas.create_oval(180, 0, 210, 30, fill="yellow")
# star_y = 0

# # Create basket
# basket = canvas.create_rectangle(160, 350, 240, 370, fill="white")

# window.bind("<Left>", move_basket)
# window.bind("<Right>", move_basket)

# move_star()

# window.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
# import random

# def move_star():
#     global star_y
#     star_y += 5
#     canvas.move(star_item, 0, 5)
#     if star_y > 400:
#         reset_star()
#     window.after(50, move_star)

# def reset_star():
#     global star_y
#     star_y = 0
#     new_x = random.randint(50, 350)
#     canvas.coords(star_item, new_x, star_y)

# def move_basket(event):
#     if event.keysym == "Left":
#         canvas.move(basket_item, -20, 0)
#     elif event.keysym == "Right":
#         canvas.move(basket_item, 20, 0)

# window = tk.Tk()
# window.title("Catch the Falling Star ✨")
# window.geometry("400x400")

# canvas = tk.Canvas(window, width=400, height=400)
# canvas.pack()

# # Load images
# bg_image = Image.open("background.png")  # A nice night sky image
# bg_photo = ImageTk.PhotoImage(bg_image)
# canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# star_image = Image.open("star.png").resize((30, 30))
# star_photo = ImageTk.PhotoImage(star_image)

# basket_image = Image.open("basket.png").resize((80, 40))
# basket_photo = ImageTk.PhotoImage(basket_image)

# # Create star and basket
# star_item = canvas.create_image(200, 0, image=star_photo)
# star_y = 0

# basket_item = canvas.create_image(200, 350, image=basket_photo)

# # Controls
# window.bind("<Left>", move_basket)
# window.bind("<Right>", move_basket)

# move_star()

# window.mainloop()


# import tkinter as tk
# import random

# def create_balloon():
#     x = random.randint(50, 350)
#     color = random.choice(colors)
#     balloon = canvas.create_oval(x, 400, x+30, 430, fill=color, outline="white", width=3)
#     balloons.append(balloon)
#     move_balloon(balloon)

# def move_balloon(balloon):
#     if canvas.coords(balloon)[1] > 0:
#         canvas.move(balloon, 0, -5)
#         window.after(40, move_balloon, balloon)
#     else:
#         canvas.delete(balloon)
#         balloons.remove(balloon)

# def pop_balloon(event):
#     clicked_items = canvas.find_overlapping(event.x, event.y, event.x, event.y)
#     for item in clicked_items:
#         if item in balloons:
#             # Get the balloon's current position
#             x1, y1, x2, y2 = canvas.coords(item)
#             cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Center of the balloon
            
#             # Create star spread effect
#             for _ in range(30):
#                 size = random.randint(5, 10)
#                 angle = random.uniform(0, 6.28)  # Random angle
#                 dx = size * random.uniform(1, 2) * random.choice([1, -1])
#                 dy = size * random.uniform(1, 2) * random.choice([1, -1])

#                 # Create the star (small circles with glow effect)
#                 star = canvas.create_oval(cx - size + dx, cy - size + dy, 
#                                           cx + size + dx, cy + size + dy, 
#                                           fill="yellow", outline="white", width=2)
                
#                 # Animate the star by moving outward and fading
#                 animate_star(star)

#             canvas.delete(item)
#             balloons.remove(item)

# def animate_star(star):
#     for _ in range(20):
#         canvas.move(star, random.uniform(-2, 2), random.uniform(-2, 2))  # Move the star randomly
#         canvas.after(30)
    
#     canvas.delete(star)  # Remove the star after animation

# window = tk.Tk()
# window.title("Balloon Pop 🎈✨")
# window.geometry("400x600")

# # Create a beautiful gradient background manually
# canvas = tk.Canvas(window, width=400, height=600)
# canvas.pack()

# # Make a gradient sky (manual way)
# for i in range(0, 600, 2):
#     color = f"#%02x%02x%02x" % (135 - i//8, 206 - i//8, 250)  # light blue to purple
#     canvas.create_rectangle(0, i, 400, i+2, outline=color, fill=color)

# colors = ["#ff4d4d", "#66ff66", "#4da6ff", "#ffff66", "#ff66ff", "#ffa64d", "#99ffcc"]
# balloons = []

# canvas.bind("<Button-1>", pop_balloon)

# def spawn_balloons():
#     create_balloon()
#     window.after(800, spawn_balloons)

# spawn_balloons()

# window.mainloop()

import tkinter as tk
import random
import math
def create_balloon():
    x = random.randint(50, 350)
    color = random.choice(colors)
    balloon = canvas.create_oval(x, 400, x+30, 430, fill=color, outline="white", width=3)
    balloons.append(balloon)
    move_balloon(balloon)

def move_balloon(balloon):
    if canvas.coords(balloon)[1] > 0:
        canvas.move(balloon, 0, -5)
        window.after(40, move_balloon, balloon)
    else:
        canvas.delete(balloon)
        balloons.remove(balloon)

def pop_balloon(event):
    clicked_items = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    for item in clicked_items:
        if item in balloons:
            # Get the balloon's current position
            x1, y1, x2, y2 = canvas.coords(item)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Center of the balloon
            
            # Create a burst of stars with more impact
            for _ in range(50):
                size = random.randint(5, 12)
                angle = random.uniform(0, 6.28)  # Random angle
                speed = random.uniform(2, 5)
                dx = speed * random.cos(angle)
                dy = speed * random.sin(angle)

                # Create the star (smaller circles with a glow effect)
                star = canvas.create_oval(cx - size + dx, cy - size + dy, 
                                          cx + size + dx, cy + size + dy, 
                                          fill="yellow", outline="white", width=2)
                
                # Start animating the star by moving outward
                animate_star(star)

            canvas.delete(item)
            balloons.remove(item)

def animate_star(star):
    def move_star():
        # Move the star randomly outward with a "bursting" effect
        canvas.move(star, random.uniform(-5, 5), random.uniform(-5, 5))
        # Gradually fade the star out
        canvas.itemconfig(star, fill=f"#{random.randint(150, 255):02x}{random.randint(150, 255):02x}{random.randint(150, 255):02x}")

        # Repeat the movement animation
        window.after(20, move_star)

    move_star()  # Start the animation

    # Remove the star after 1 second for the final "disappearance"
    window.after(1000, lambda: canvas.delete(star))

window = tk.Tk()
window.title("Balloon Pop 🎈✨")
window.geometry("400x600")

# Create a beautiful gradient background manually
canvas = tk.Canvas(window, width=400, height=600)
canvas.pack()

# Make a gradient sky (manual way)
for i in range(0, 600, 2):
    color = f"#%02x%02x%02x" % (135 - i//8, 206 - i//8, 250)  # light blue to purple
    canvas.create_rectangle(0, i, 400, i+2, outline=color, fill=color)

colors = ["#ff4d4d", "#66ff66", "#4da6ff", "#ffff66", "#ff66ff", "#ffa64d", "#99ffcc"]
balloons = []

canvas.bind("<Button-1>", pop_balloon)

def spawn_balloons():
    create_balloon()
    window.after(800, spawn_balloons)

spawn_balloons()

window.mainloop()

