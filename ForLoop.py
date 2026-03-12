# Animals =["Cat","Dog","Elephant","Girafee"]
# print(Animals)
# for a in Animals :
#     print(a)


# sentence ="Welcome to My Class"
# for b in sentence :
#     print(b)

# for j in range(10):
#     print("Hello World :",j)

# x=4 
# y=10

# for k in range(x,y):
#     print("Hey...!",k) 

#While loop

# Flowers =["Lotus","Jasmine","Sunflower"]

# k=0
# while k < 3 :
#     print(Flowers[k])
#     k += 1


# Greetings ="Happy Morning"
# w=0
# length=len(Greetings)
# while w<length :
#     print(Greetings[w])
#     w += 1
    


# i = 1

# while i <=10:
#     print(i)
#     i += 1  # Increment i by 1

#Break 
# t=1
# while t<=5 :
#     if t==3:
#         break
#     print(t)
#     t+=1

# #Continue

# t=1
# while t<=5 :
#     if t==4:
#        continue
#     print(t)
#     t+=1
    

#Pass
# t=1
# while t<=5 :
#     if t==2:
#        pass
#     print(t)
# #     t+=1

# x = 5

# if x > 0:
#     print("x is positive")
#     for i in range(x):
#         print("i is:", i)
#     print("Loop is over")
# print("Program finished")

# for x in range(1,7) :
#     if x== 3 :
#         continue
#     print(x)

# function recursive
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# p=factorial(3)
# print(p)

# #sum
# def sum_recursion(n):
#     if n == 0:
#         return 0
#     return n + sum_recursion(n - 1)
# sum_recursion(5)

#output
# sum_recursion(5)
# = 5 + sum_recursion(4)
#               
# = 5 + (4 + sum_recursion(3))
#                 
# = 5 + (4 + (3 + sum_recursion(2)))
#                     
# = 5 + (4 + (3 + (2 + sum_recursion(1))))
#                         
# = 5 + (4 + (3 + (2 + (1 + sum_recursion(0)))))
#                             
# = 5 + (4 + (3 + (2 + (1 + 0))))  ←←←←←←← base case reached!


# i = 0                             
# while i < 6:
#   if i == 3:
#     continue
#   print(i)
#   i += 1