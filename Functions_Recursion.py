#Recursion -->function calls itself continue  

# Factorial :

# n=int(input("Enter the Factorial number :"))

# def factorial(n):
#     if n==0 :
#         return 1
#     else:
#         return n*(factorial(n-1))
 
# print("Factorial",factorial(n))


# Sum 
# r=int(input("Enter the  number :"))
# def Sum_Numbers(r) :
#      if r==0:
#         return 0
#      else :
#         return (r%10)+Sum_Numbers(r//10)
        
# print("Sum of Digits",Sum_Numbers(r))



# #Count the Number of Digits in a Number (Using Recursion)

# def count_digits(number):
#     if number == 0:
#         return 0 # base case
#     else:
#         return 1 + count_digits(number // 10)  # recursive case
# number = 123
# result = count_digits(number)
# print("Number of digits:", result)
  