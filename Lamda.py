#You can write quick, one-line functions without naming them.
# Instead of writing a full def block,
# you can do simple logic inline.
#predefined methods :
# map() – apply a function to all items in a list.
# filter() – filter elements based on a condition.
# sorted() – sort with custom logic.


# Double Each Number(without Lambda)
# def m1():
#    numbers = [1, 2, 3, 4, 5]
#    doubled = []  
#    for num in numbers:
#      doubled.append(num * 2)
#    print("Doubled:", doubled)  # Output: [2, 4, 6, 8, 10]
# m1()

#With lambda
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []
# for num in numbers:
#     squared_numbers.append(lambda x: x * x,(num))

# print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]



# # Program 
# #Add two numbers :

# def AddTwo(a,b):
#     c=a+b
#     return c
# print(AddTwo(30,40))

# # # # #Using lambda :
# add=lambda x,y:x+y
# print(add(40,33))

# # Square a Number

# def st(sq):
#     d=sq*sq
#     return d
# print(st(4))

# # # Using lambda
# Square=lambda y:y*y
# print(Square(5))

# # #Get the last character of a String
# def GetLast(name):
#    t=name[-1]
#    return t
# print(GetLast("Python"))
# # #Using lambda
# GetLas =lambda r:r[-1]
# print(GetLas("Java"))

# #Check number is even 
# def Even(num):
#     if num%2 ==0:
#         print("Even")
#     else :
#         print("Odd")
# Even(433)
# # # #Using lambda
# EvenorAdd =lambda k:k%2==0
# print(EvenorAdd(72))

# #Get length  of a String 
# sub=str(input("Enter any name : "))
# def Length(sub):
#       t=len(sub)
#       return t
# print(Length(sub))
# # #Using lambda
# getLength =lambda gt:len(gt)
# print(getLength(sub))

# #using map and filter :

# numbers=[4,5,3,4,3,2,5,7,7,86,99]
# even_numbers =list(filter(lambda x:x%2==0,numbers))
# square_numbers=list(map(lambda y:y*y,even_numbers))
# print(numbers)
# print(even_numbers)
# print(square_numbers)

# #Filter name and convert uppercase :
# names =["Ananya","anandhi","balaji","Arun","Deepika"]
# Afilter =list(filter(lambda q:q.startswith("A"),names))
# Mapping =list(map(lambda z:z.upper(),Afilter))
# print(names)
# print(Afilter)
# print(Mapping)