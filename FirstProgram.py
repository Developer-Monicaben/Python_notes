#python:
#It is a high-level, interpreted programming language .its simplicity and readability.
#Developed by: Guido van Rossum
#First released: 1991
#Current version: Python 3 (most used)

#Python Features :
#1) Simple Syntax – Easy to write and understand (like English).
#2) Interpreted – No need to compile; runs directly.
#3) Dynamically Typed – No need to declare variable types.
#4) High-Level Language – Focus on logic, not hardware details.
#5) Portable – Write once, run anywhere (Windows, Linux, Mac).
#6) Object-Oriented – Supports classes and objects.
#8) Extensible & Embeddable – Can combine with other languages like C/C++.
#9) Free and Open Source – Completely free to use and modify.

#Differences -->Java vs Python 
#Python code is shorter, Java code is longer.
#Python is easier to learn, Java is a bit harder.
#Python runs slower, Java runs faster.
#Python doesn't need variable types, Java does.
#Python is used in AI & scripts, Java is used in big apps.

# print is a function
# print("Hello \n World!")
# print("Good Morning!!")


# #Variables 
# x="40"
# y="50"
# z=x+y
# print("z value is :",z)

# Z="Python"
# print("Z value is :" ,Z)

# x=60
# print()
# x="python"
# print(x)    # dispaly the output

# # #casting
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  #z will be 3.0
# print(x)
# print(y)
# print(z)

# P="4"

# # #get the type 
# x = 5
# y = "John"
# z=4.78
# print(type(x))
# print(type(y))
# print(type(z))

# # #case 
# #Camel Case  -->myVariableName = "John"  -->firstNumber
# #pascal case -->MyVariableName = "John"  -->FirstNumber
# #snake case -->my_variable_name = "John"-->separated by underscore
 

# #  #MultipleValues assign 
# x, y, z = "Orange", "Banana", "Cherry"
# print(x,y,z)
# print(y)
# print(z)

# # #oneValueFormulitplevaraibles
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


isAvailable =True

# # #unpack a collection
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# # #output
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x + y + z)

# x = 5
# y = "John"
# print(x, y)

#Global variables can be used by everyone, both inside of functions and outside.

# n ="program"

# def myfunc():
#    q=50 
# # print("Python is ",q)

# q=50
# myfunc()
# print("N value is : ",n)

# #Using global keyword

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)