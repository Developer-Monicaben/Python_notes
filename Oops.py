# Class: A blueprint for creating objects.
# Object: An instance of a class.
# Inheritance: A way to reuse code from an existing class.
# Encapsulation: Wrapping data (attributes) and methods (functions) in a single unit (class).
# Polymorphism: Using the same method name but having different implementations.
# Abstraction: Hiding complex implementation details and showing only essential features.


# Creating classes and Instance methods
# class Person :
      
#     def __init__(self,name,age):    #Constructor
#         self.name=name
#         self.age=age
#     def greet(self):    
#         print(f"My name is {self.name} and i am {self.age} years old!")

# person1=Person("Alice",44)   
# person1.greet() 


# #Task->Create a Student class with __init__, and methods display() and check_pass() to show name, marks, 
# and pass/fail based on marks ≥ 40.

# class Student:
    
#     def __init__(self,names,Marks):
#         self.names=names
#         self.Marks=Marks

#     def Display(self):
#         print("\n Display :")
#         print("Name :",self.names)
#         print("Marks :",self.Marks)
        
#     def check_pass(self):
#         if self.Marks >=40:
#             print("Result is :pass")
#         else :
#             print("Result is :Fail")
# print("Task1 :")
# name=input("Enter your Name :")
# Marks=int(input("Enter your Marks :"))

# clg=Student(name,Marks)   #object creation
# clg.Display()
# clg.check_pass()


# #Task :->Create a `BankAccount` class with `__init__`, `deposit()`, `withdraw()`, and `display()`
# methods to manage account holder and balance.

# class BankAccount:
#     def __init__(self ,accountHolder,Balance):
#         self.accountHolder=accountHolder
#         self.Balance =Balance

#     def withdraw(self,amount):
#         if self.Balance>=amount:
#            self.Balance-=amount
#            print("Withdraw:",amount)
#         else:
#             print("InSufficient Balance")
#         print("Balance :",self.Balance)

#     def Deposit(self,amount):
#         self.Balance += amount
#         print("Deposited :",amount)
#         print("DBalance :",self.Balance)
    
#     def Display(self):
#         print("Account Holder Name :", self.accountHolder)
#         print("Balance is :",self.Balance)

# print("Bank Account :")
# bc=BankAccount("Jeslyn",10000)

# bc.withdraw(5000)
# bc.Deposit(500)
# bc.Display()

# #Inheritance :

# # single :

# class Animal:
#     def cat(self):
#         print("meaw meaw....!")
        
# class Dog(Animal):
#     def puppy(self):
#         print(" loll....lol.. ...!")

# print("Task2 :")

# animal=Animal()
# animal.cat()

# dog=Dog()
# dog.puppy()
# dog.cat()



# #MultiLevel
# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# class Puppy(Dog):
#     def cute(self):
#         print("Puppy is cute")

# p = Puppy()
# p.sound()
# p.bark()
# p.cute()


#multiple 

# class Father:
#     def car(self):
#         print("Father's car")

# class Mother:
#     def house(self):
#         print("Mother's house")

# class Child(Father, Mother):
#     def own(self):
#         print("Child's Scooty")

# c = Child()
# c.car()
# c.house()
# c.own()

# #Hierarchical 

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")

# d = Dog()
# d.speak()
# d.bark()

# c = Cat()
# c.speak()
# c.meow()

# #Hybrid

# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def display(self):
#         print("Class B")

# class C(A):
#     def print_msg(self):
#         print("Class C")

# class D(B, C):  # Inherits from both B and C, which inherit from A
#     def final(self):
#         print("Class D")

# obj = D()
# obj.show()
# obj.display()
# obj.print_msg()
# obj.final()


#Polymorphism->"many forms".It allows methods or functions to behave differently based on the object or class they are acting upon. 
#1)Method Overriding (Runtime Polymorphism) 2)Method Overloading (Not directly supported in Python,
# but can be mimicked)


#1)
# class Animal:
#     def speak(self):
#         print("Self ")

# class Dog(Animal):
#     def speak(self):  # Overriding the speak method
#         print("Dog barks")

# class Cat(Dog):
#     def speak(self):  # Overriding the speak method
#         print("Cat meows")

# # Polymorphism in action
# animals = [Dog(), Cat(),Animal()]

# for animal in animals:
#     animal.speak()             # Calls the overridden method for each object

# 2
# class Calculator:
#     def add(self, a, b, c=2):  # Default parameter to mimic overloading
#         return a + b + c

# calc = Calculator()
# print(calc.add(2, 3))       # Works like add(a, b)
# print(calc.add(2,4,5))    # Works like add(a, b, c)

#1)task:Method Overloading: Create a class Multiplication with a method multiply that works 
# for two numbers or three numbers
#(default argument for the third number).
#2)task:Method Overriding: Create a class Shape with a method area(), 
# then create two subclasses Circle and Rectangle that override 
#area() to calculate their respective areas.

  
#Abstraction:
# Abstraction hides the details of the implementation and exposes only the essential features.
# Abstract classes provide a template for other classes to follow.
# Abstract methods must be implemented by the subclasses.
 
# from abc import ABC, abstractmethod
# # Abstract class
# class Animal(ABC):
    
#     @abstractmethod
#     def sound(self):
#         pass            # Abstract method with no implementation

#     @abstractmethod
#     def sound1(self):
#         pass

# # Subclass of Animal (Concrete Class)
# class Dog(Animal):
#     def sound(self):     # Implementing the abstract method
#         print("Dog barks")

#     def sound1(self):
#          print("Sound!!!")

# # Subclass of Animal (Concrete Class)
# class Cat(Animal):
#     def sound(self):     # Implementing the abstract method
#         print("Cat meows")
    
#     def sound1(self):
#         print("Sound!!!")
# # Creating objects of concrete classes
# dog = Dog()
# cat = Cat()
        
# dog.sound()
# dog.sound1()  # Output: Dog barks
# cat.sound()   # Output: Cat meows
# cat.sound1()


#Encapsulation :

# class BankAccount:
#     def __init__(self, holder_name, balance):
#         self.__holder_name = holder_name  # Private variable
#         self.__balance = balance          # Private variable

#     # Getter for holder_name
#     def get_holder_name(self):
#         return self.__holder_name

#     # Setter for holder_name
#     def set_holder_name(self, name):
#         self.__holder_name = name

#     # Getter for balance
#     def get_balance(self):
#         return self.__balance

# # Method to deposit money
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Deposit amount must be positive.")

# # Method to withdraw money
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance.")

# # Creating an object of BankAccount
# account = BankAccount("John Doe", 1000)

# # Accessing private attributes using getter methods
# print(account.get_holder_name())  # Output: John Doe
# print(account.get_balance())      # Output: 1000

# # Modifying balance using setter methods
# account.deposit(500)              # Deposits 500
# print(account.get_balance())      # Output: 1500

# account.withdraw(200)             # Withdraws 200
# print(account.get_balance())      # Output: 1300

# account.set_holder_name("Kajol")
# print(account.get_holder_name()) 


# 
# Task


# 1)Abstract Class with Constructor
# Create an abstract class Employee with attributes name and salary.
# Define an abstract method calculate_bonus().
# Subclasses Manager and Developer should implement different bonus calculations.
# 2)Create an abstract class Shape with an abstract method area().
# Implement two subclasses Circle and Rectangle that calculate area differently.

# 1)Encapsulation with Validation
# Create a class PasswordManager that stores a private password.
# Add a setter that only updates the password if it has at least 8 characters and one special symbol.
# Add a method to check if a given password matches the stored one.
# 2)Write a class BankAccount with private attributes _balance and _account_number.
# Provide getter/setter methods to access and update balance safely.

# 1)Create a class Animal with a method make_sound().
# Subclasses Dog and Cat should override this method.
# Write a function that accepts an Animal object and calls make_sound().

# 1)Inheritance 
# Build a Person class with attributes name and age.
# Derive a Student class that adds roll_number and grade.
# Demonstrate single inheritance by printing details of a student.
# 2)Multiple Inheritance 
# Create two classes Teacher and Researcher.
# Derive a new class Professor that inherits from both and demonstrates method resolution order (MRO).     

# 1)Method Overloading (using default arguments)
# Write a class Calculator with a method add() that can accept either 2 or 3 numbers.
# 2)Method Overriding
# Create a base class Vehicle with a method fuel_type().
# Subclasses Car and Bike should override the method to show different fuel types.




# 1

# from abc import ABC 
 
# class Employee(ABC):
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def calculateBonus():
#         pass
# class Manager(Employee):
#       def calculateBonus(self,bonus):
#        return self.salary*bonus

# class Developer(Employee):
#       def calculateBonus(self,bonus):
#        return self.salary*bonus
# M=Manager("Ashok",45000)
# D=Developer("Anandhi",38000)
# print(M.calculateBonus(3))
# print(D.calculateBonus(2))

# # 2.

# class shape(ABC):
#     def area():
#         pass
# class circle(shape):
#     def area(self,radius):
#         return 3.14*radius
# class rectangle(shape):
#     def area(self,length,breadth):
#         return length*breadth
# circle1=circle()
# print(circle1.area(30))
# rect=rectangle()  
# print(rect.area(13,32) )

# 2.Encaps

# class BankAccount:
#     def __init__(self,accountHolderName,Balance):
#         self.__accountHolderName=accountHolderName
#         self.__Balance=Balance
    
#     def get_accountHolderName(self):
#         return self.__accountHolderName
#     def set_accountHolderName(self,name):
#         self.__accountHolderName=name
#     def get_balance(self):
#         return self.__Balance
#     def set_balance(self,amount):
#         self.__Balance=amount

# bc1=BankAccount("Anjali",50000)
# bc1.set_balance(3000)
# print(bc1.get_balance())



# 1.Inheritance

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
   
#     def view(self):
#         print("Name is :",self.name)
#         print("Age is :",self.age)
# class student(person):
#     def __init__(self,rollno,grade):
#          self.rollno=rollno
#          self.grade=grade

#     def view(self):
#         print("Roll no :",self.rollno)
#         print("Grade is  :",self.grade)
# std=student(78,"A")
# std.view()
# std.view()



