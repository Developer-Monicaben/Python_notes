# Exception_Handling:
# try, except, and finally :
# try: Block where you put code that might raise an error.
# except: Catches the error and handles it.
# # finally: Code that will always run, no matter what (even if an exception was raised or not).

# try:
#     num = int(input("Enter a number: "))
#     assert num >= 0, "Number must be non-negative"
#     result = 10 / num         # Might raise ZeroDivisionError or ValueError
#     print("Result :",result)
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# except ValueError:
#     print("That's not a valid number!")
# finally:
#     print("This runs no matter what.")

#assert
# import math

# try:
#     def safe_sqrt(x):
#         assert x >= 0, "Number must be non-negative"
#         return math.sqrt(x)
#     num = int(input("Enter a number: "))
#     print("Square root:", safe_sqrt(num))
# except ValueError :
#     print("Its not a valid number ")

#Task

# try:
#     nums = [10, 20, 30, 40, 50]
#     print(nums)
#     index = int(input("Enter index to access (0-4): "))
#     print("Value at index:", nums[index])
# except IndexError:
#     print("Error: Index out of range.")
# except ValueError:
#     print("Error: Invalid input. Please enter a number.")
# finally:
#     print("List access attempt complete.")



#Task :check age eligible for vote :

def check_voting_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age < 18:
            print("You are not eligible to vote.")
        else:
            print("You   eligible to vote!")
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Age check complete.")

check_voting_age()
