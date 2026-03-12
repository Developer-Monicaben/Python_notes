#Modes
# 'r' – Read (default mode, file must exist)
# 'w' – Write (creates file if not exists, overwrites if exists)
# 'a' – Append (creates file if not exists, adds content to end)
# 'x' – Create (fails if file exists)


# #Reading files :
# with open('Python_FileHandling.txt','r')as f:
#     content=f.read()
#     print(content)
    # print(f.read())
                                                
#Writing
# with open('Python_FileHandling.txt','w') as f:
#     f.write("Hello World!")

#apending
# with open('Python_FileHandling.txt','a') as f:
#     f.write("\nGood")

# #creating:
# with open('Python_FileHandling.txt', 'x') as f:
#     f.write("This is a new file.")

#Deleting
# import os

# # Check if file exists
# if os.path.exists("Python_FileHandling.txt"):  
#     os.remove("Python_FileHandling.txt")  # Delete the file
#     print("File deleted.")
# else:
#     print("File does not exist.")


#Handling file_Exceptions :
# try:
#     with open("myfile.txt", "w") as f:
#         # print(f.read())
#         f.write("I am writing ")
      
# except FileNotFoundError:
#     print("File not found.")
# except IOError:
#     print("Error reading file.")


# try:
#     # Writing to a file
#     with open('myfile.txt', 'w') as file:
#         file.write("This is the first line.\n")
#         file.write("This is the second line.\n")

#     # Appending to the file
#     with open('myfile.txt', 'a') as file:
#         file.write("This is the third line, appended.\n")

#     # Reading from the file
#     with open('myfile.txt', 'r') as file:
#         content = file.read()
#         print("File content:\n", content)

# except FileNotFoundError:
#     print("The file was not found.")
# except IOError:
#     print("An I/O error occurred.")
