#Creating a String
# name="Python Programming"
# print("name :",name)

# #Concat
# FirstName ="Rajini"+" "+"Kanth"
# print(FirstName)

# #formatted string literal.
# name = "Alice"
# age = 25

# message =f"My name is {name} and I am {age} years old."
# print(message)

# # #Length
# lang="Tamil"
# print(len(lang))

# # #Accessing 
# Subject ="Social Science"
# print(len(Subject))
# print(Subject[4])
# print(Subject[-4])

# # #String Methods :
# Greet ="       Happy Morning !     "
# print(Greet.upper())
# print(Greet.strip())  #trim
# print(Greet.lower())
# print(Greet.title())   #Caps4
# print(Greet.replace("Happy","Good"))

#Check-SubString
# text ="Welcome to my World !"
# print(text in "my")
# print(text not in "my")
# 
# #Splitted-Joining
# text1 ="this is my program for splitted and joining "
# Splited =text1.split(" ")
# print(Splited)
# Joining ="-".join(Splited)
# Joining1 ="-".join(text1)
# print(Joining)
# print(Joining1)

#Loop through 
# text5 ="Loop Through "

# for values in text5 :
#     print(values)

# for i in range(1,11) :
#     print(i)

# #EX:counting letters
# sentence ="abdababcaa"
# aLetterCount=0
# for t in sentence :
#     if t == "a" :
#         aLetterCount +=1
# print("ALetter Count :",aLetterCount)


# taskforVowels
# text = "banana"
# vowel_count = 0

# for char in text:
#     if char in "aeiouAEIOU":
#         vowel_count += 1
    
# print("Vowels:", vowel_count)


#Task
# def longest_word(text):
#     words = text.split(" ")  # splits the sentence into words
#     longest = ""          # stores the longest word

#     for word in words:
#         if len(word) > len(longest):
#             longest = word  # update if this word is longer

#     return longest
# print(longest_word("Good Morning word make a Happy!"))