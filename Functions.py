# Creating own functions : 

# def greet() :
#     print("Hello...Good Morning !!")
# greet()     #calling function


#Function Parameters

def Param(name,age) :
    print("My name is " +  name +  "my age is ",age)
# Param("John",56)

# #Types of function arguments 
# #Default 
# def defalt(name="Alice"):
#     print(name)
# defalt()
# defalt("Amit")

# # #keyword
# def keywod(name,age):
#   print(f"Name: {name}, Age: {age}")
# keywod(age=30,name="Ravi")

# # #Variable Arguments   -->args(tuple)  -->Use when you don’t know how many arguments will be passed.
# def VarArg(*args) :
#     print(args)
# VarArg(1,2,3,4,55,54,545,454)


# #Arbitary arguments --args  -->Use when you want to accept a dynamic number of keyword arguments.
# def sum_all(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     print("Sum:", total)
# sum_all(1,2,3,4)

# #**kwargs
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# show_info(name="Ajith",value=33,age=34,city="Chennai",Nick="Arun")

# #Combine
# def Allargs(*args, **kwargs):
#     print("args:", args)
#     print("kwargs:", kwargs)

# Allargs(1, 2, 3, name="John", age=22)



# name=str(input("Enter your name :"))
# age=int(input("Enter your Age :"))

# def details(name1,age1):
#     print(f"My name is {name1} and i am {age1} years old !! ")
# details(name,age)