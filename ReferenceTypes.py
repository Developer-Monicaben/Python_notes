# Iterators :
# An iterator is an object in Python that allows traversing through all the elements of a 
# collection (like lists, tuples, etc.) one at a time.Step-by-step access of data.

# my_list = [10, 20, 30]
# iterator = iter(my_list)

# print(next(iterator))  # 10
# print(next(iterator))  # 20
# print(next(iterator))  # 30 
# print(next(iterator))  # Raises StopIteration


# Generators: Step-by-step + lazy evaluation (huge memory saving).
# A generator is a special type of iterator that uses yield instead of return.
# It automatically saves the state of the function, allowing you to generate values on 
# the fly—perfect for large datasets or infinite sequences.
 

# def even_numbers(limit):
#     num = 0
#     while num <= limit:
#         yield num
#         num += 2

# for ev in even_numbers(6):
#     print(ev)
# print((even_numbers(6)))

# Closure :Keep function-specific state without global variables
# A closure is a function that remembers and uses variables from its enclosing scope,
# even after thting.
# It allows data to be encapsulated and persist between calls

# def outer():
#     msg = "Hello"
#     def inner():
#         print(msg)
#     return inner

# greet = outer()
# greet()  #at outer function has finished executing# Output: Hello


# Decorators:
# A decorator is a function that adds extra functionality to another function without changing its code.
# It wraps one function inside another using @decorator_name syntax.like gift wrapping

# def my_decorator12(func):
#     def wrapper():
#         print("Before the function")
#         func()
#         print("After the function")
#     return wrapper
                   
# @my_decorator12
# def say_hello():
#     print("Hello!")

# say_hello()
