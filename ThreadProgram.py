# Threading :
# Threading is a technique in Python that allows a program to run multiple tasks concurrently
# (one at a time, but fast) using threads.
# It uses the threading module to create and manage threads.
# Useful for I/O-bound tasks (e.g., file reading, network requests).

# Multithreading :
# Multithreading means running multiple threads in parallel within a single process.
# In Python, due to the Global Interpreter Lock (GIL),threads don’t run truly in parallel for CPU tasks — 
# but multithreading still improves performance for I/O-bound tasks.
# Best for tasks like (downloading files or reading web pages.)


import threading
import time

# def print_cube(num):
#     print(f"Cube: {num * num * num}")

# def print_square(num):
#     print("Square: {}" .format(num * num))

# def print_Numbers(num):
#     print("Numbers: {}" .format(num))
  
# t1 = threading.Thread(target=print_square, args=(10,))
# t2 = threading.Thread(target=print_cube, args=(10,))
# t3= threading.Thread(target=print_Numbers, args=(10,))

# t1.start()
# t2.start()
# t3.start()
# print("Done!")
# 

# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")
#         time.sleep(3)

# def print_letters():
#     for ch in ['A', 'B', 'C', 'D', 'E']:
#         print(f"Letter: {ch}")
#         time.sleep(3)

# # Creating threads
# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters)

# # Starting threads
# t1.start()
# t2.start()


# def task(name, delay):
#     print(f"{name} started")
#     time.sleep(delay)
#     print(f"{name} finished")

# # Creating threads
# t1 = threading.Thread(target=task, args=("Thread 1", 2))
# t2 = threading.Thread(target=task, args=("Thread 2", 4))

# t1.start()
# t2.start()

# # Wait for both threads to finish
# t1.join()
# t2.join()

# print("All threads done!")

# Synchronized
# 
# Example 1 :

# Lock object
# lock = threading.Lock()

# def task1():
#     # with lock:
#         for i in range(3):
#             print(f"Task1: Step {i+1}")
#             time.sleep(2)

# def task2():
#     # with lock:
#         for i in range(3):
#             print(f"Task2: Step {i+1}")
#             time.sleep(2)

# # Create threads
# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# # Start threads
# t1.start()
# t2.start()

# # Wait for both to complete
# t1.join()
# t2.join()

# print("Both tasks done.")

# Example 2 :
# lock = threading.Lock()

# def fruits():
#     items = ["Apple", "Banana", "Grapes"]
#     for fruit in items:
#         with lock:
#             print(f"Fruit: {fruit}")
#             time.sleep(0.5)

# def vegetables():
#     items = ["Tomato", "Potato", "Carrot"]
#     for veg in items:
#         with lock:
#             print(f"Vegetable: {veg}")
#         time.sleep(0.5)

# t1 = threading.Thread(target=fruits)
# t2 = threading.Thread(target=vegetables)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Finished listing all items.")


# Example 3 :

# lock = threading.Lock()

# def task1():
#     with lock:
#         print("Task1 is starting")
#         time.sleep(0.5)
#         print("Task1 is done")

# def task2():
#     with lock:
#         print("Task2 is starting")
#         time.sleep(0.5)
#         print("Task2 is done")

# # Create and start threads
# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Both tasks completed.")