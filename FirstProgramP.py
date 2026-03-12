# print("Hello World!!!")
# print("Good Morning !!!!")

# a=3
# b=5
# c=a+b
# print("c value is :",c)

# waterBottle="Water"
# print("WaterBottle : ",waterBottle)


# Number=9
# NumberTwo=15
# NumberThree=Number-NumberTwo
# print("Number 3 value is :",NumberThree)

# Volume1=90
# Volume2=80
# Volume3=Volume1*Volume2
# print("value of volume 3 is:",Volume3 )

# Area500=983
# Area900=3948
# Area3000=Area500/Area900
# print("The Value Of Area 3000 is:",Area3000)


# # Get a value from user

# Name=input("Enter your name :")
# Email=input("Enter your email :")
# Age=input("Enter vyour age :")

# print("My name is ",Name,"My email id is ",Email,"and i am ",Age,"years old!!!")

# #formatted String
# print(f"My name is {Name} and my email id is {Email} and i am {Age} years old")


# Variable10=int(input("Type Your Number1:"))
# Variable20=int(input("Type Your Number2: "))
# Variable30=Variable10+Variable20
# print(f"My Number1 is {Variable10},My Number2 is{Variable20},My Sum is {Variable30}")

# Set1=int(input("Input Your first Set:"))
# Set2=int(input("Input your Second Set:"))
# print(Set1*Set2)





# Name=input('Full Name : ')
# Age=input("How old are You : ")
# City=input("in which City do you live? : ")
# print(f"Dear,{Name},From {City},You are {Age} Years Old")

# Author=input('Who is Your Favourite Author? : ')
# Book=input("What is Your Favourite Book? : ")
# print(f"The {Book} By {Author},is a true masterpiece that cannot be replicated")


# first_name=input("First Name: ")
# last_name=input("Surname: ")
# print(f"{first_name} {last_name},Welcome To the community")


# Main_score=900
# Negative_points=700
# Total_score=(Main_score)/(Negative_points)
# print(Total_score)



# If else task 

# age_check=int(input("enter your age here : "))
# print(age_check)
# if age_check > 18 :
#     print("Eligible to vote")
# else: print("Not eligible to vote")

# Number_type=int(input('enter a number here :'))
# print(Number_type)
# if Number_type%2 ==0 :
#     print("even Number")
# else : print("odd Number")


# Number1=int(input("enter your number1 here : "))
# Number2=int(input("enter youre number 2 here :"))
# Number3=int(input("enter youre number3 here : "))
# if Number1>Number2 : 
#     if Number1>Number3 :
#         print(f"{Number1}")
# elif Number2>Number1 : 
#     if Number2>Number3 : 
#         print(Number2)
# elif Number3>Number1 : 
#     if Number3>Number2 : 
#         print(Number3)

# if Number1>Number2 and Number1>Number3:
#     print("Number1 value is greater")


# Number1=int(input("enter youre number1 here : "))
# Number2=int(input("enter Youre number2 here : "))
# Number3=int(input("enter youre number 3 here : "))

# if Number1<Number2 and Number1<Number3 : 
#     print(Number1)
# elif Number2<Number1 and Number2<Number3 : 
#     print(Number2)
# else : print(Number3)



# Marks=int(input("Enter youre marks here : "))
# if Marks==100 : 
#     print("A+ perfect score")
# elif Marks>=90 and Marks<100 : 
#     print("A+")
# elif Marks<=89 and Marks>=80 : 
#     print("A")
# elif Marks<=79 and Marks>=70 : 
#     print("B+")
# elif Marks<=69 and Marks>=60 : 
#     print("B")
# elif Marks<=59 and Marks>=50 : 
#     print("C")
# else :  print("Fail") 


# print how many even number in a list 
# count=0
# Numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
# for Num in Numbers :
#      if Num%2==0 :
#           count+=1
# print(count)


# 2)Write a Python program to input an age and print the age category (Child, Teenager, Adult, Senior Citizen)


# Age=int(input("Rnter Youre Age Here : "))
# print(Age)
# if Age<=5 : 
#     print("Child")
# elif Age>=12 and Age<=18 : 
#     print("Teenager")
# elif Age>18 and Age<60 : 
#     print("Adult")
# else : 
#     print("Senior Citizen")

# for v in range(1,10,2):
#     print(v)



# Fibonacci
# G=0
# H=1
# Number=int(input("enter youre number here : "))
# print(f"{G}   {H}")
# for i in range(Number) : 
#    N=(G+H)
#    print(N)
#    G=H
#    H=N




# number=1234
# print(len(str(number)))


# Count the number of digit

# number1=1234    #123 -->12   --->1   --->0

# count=0
# while number1 !=0:
#     number1=number1//10
#     count+=1
# print(count)


# Number=int(input("Enter Youre Number here : "))
# while True: 
#     if Number<0:
#         print("You are entered Negative Number !!!")
#         break
#     else:
#         Number=int(input("Please enter a number again : "))
     

# count=0
# integers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for num in integers : 
#     if num%2 !=0 :
#         count+=1
# print(count)


# Numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# for Numbers in Numeros :
#      if Numbers%3==0 :
#           continue
#      else :
#             print(Numbers)



# van=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# for Numeros in van :
#     if Numeros%7==0 or  Numeros%5==0 : 
#        continue
#     else :
#            print(Numeros)





# Age=int(input("Enter Youre Age here : "))
# while True:
#      if Age>18 :
#           print("You are eligible to vote")
#           break
#      else:
#         Age=int(input("Enter an age again :"))
           



# Numbers=[1,2,3,4,5,6,7,8,9,10,11,12,34,56,78]

# for Num in Numbers :
      

# names=['Pradhyun',"Proffesor","Proffesional","Norman","Suhail"]
# Pfilter=list(filter(lambda q: q.startswith("P"),names))
# Uppercase=list(map(lambda z:z.upper(),Pfilter ))
# print(names)
# print(Pfilter)
# print(Uppercase)


# numbers=[4,5,3,4,6,7,8,99,23,46,86]
# even_numbers=list(filter(lambda x:x%2==0,numbers))
# Square_Numbers=list(map(lambda y :y*y,even_numbers))
# print(Square_Numbers)

# def m1() :
#      numbers=[1,2,3,4,5,6]
#      doubled=[]
#      for num in numbers :
#         doubled.append(num*2)
#      print("doubled : ",doubled)
# m1()


# sub=str(input("Enter any name : "))
# def length(sub) :
#     t=len(sub)
#     return t
# print(length(sub))


# get_lenth= lambda gt : len(gt)
# print(get_lenth(sub))



# Numeros=[2,4,5,6,7,8,9,99,37,30]
# Threefilter=list(filter(lambda X:X%3==0,Numeros))
# Mapping_Squared=list(map(lambda Y: Y*Y,Threefilter))
# print(Numeros)
# print(Threefilter)
# print(Mapping_Squared)



# Animal_list=["pigeon","lion","Tiger","Goat","Ostritch","Jaglion"]
# Ends_with_n_filter=list(filter(lambda X: X.endswith("n"),Animal_list))
# Mapping_Lowercase=list(map(lambda Y: Y.title(),Ends_with_n_filter))
# print(Animal_list)
# print(Ends_with_n_filter)
# print(Mapping_Lowercase)

# largest=3
# Grades=[3,4,5,6,7,8,9]
# def integers() :
#     for Num in Grades :
#         if Grades>
#         return z
# print(integers())




# try :
#  with open("myfile.txt","w") as f:
#   f.write("I am Writing")
# except FileNotFoundError :
#  print("File Not Found")
# except IOError :
#  print("Error Reading File")


# try :
#  with open("myfile.txt","w") as file :
#   file.write("This is the first line.\n")
#   file.write("This is The Second Line.\n")

#  with open("myfile.txt","a") as file :
#   file.write("This is the Third Line,appended \n")
#  with open("myfile.txt","r") as file :
#   content=file.read()
#   print("file content :",content)
# except FileNotFoundError :
#  print("this file was not found")
# except IOError :
#  print("an I/O error occured")




# number=int(input("Enter Youre Number1 Here :"))
# number2=int(input("Enter Youre Number Here"))
# print(number)
# print(number2)
# assert number != "","Do Not Leave Empty"
# # assert number2 != "","Do Not Leave Empty"
 
 
 
# class Bookshop :
#     def __init__(self,Bookname,price,Quantity) :
#      self.Bookname=Bookname
#      self.price=price
#      self.Quantity=Quantity
    
#     def display(self) :
#        print("Bookname :",self.Bookname)
#        print("Quantity :",self.Quantity)
#        print("Price :" ,self.price)

#     def Buy(self) :
   
#        Quantity=int(input("Enter How many Book You want :"))
#        total=Quantity *self.price
#        print("Total Bill :",total)
# Bk=Bookshop("Text Book",500,200)
# Bk.display()
# Bk.Buy()



# number=9
# isPrime=True
# for i in range(2,number):
#     if number%i==0:
#       isPrime=False
#       break
# if(isPrime):
#    print("Number is Prime")
# else:
#    print("Number is not Prime ")






