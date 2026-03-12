print("Welcome to my Contacts")
contacts={}

def Add_Contact():
    name=input("Enter contact name :")
    Phone=int(input("Enter the Phone number : "))
    contacts[name]=Phone
    print(f"{name} Added Succesfully !!")

def Search_Contacts():
    search=input("Search Here  :").lower()
    if search in contacts:
        print(f"{search} :{contacts[search]}")
        print("Contact Found !!")

def Delete_Contacts():
     name=input("Enter the Name you want to delete :").lower()
     if name in contacts:
         del contacts[name]
     print(f"{name} Contact is deleted !!")

def View_Contacts():
    print("Your Contacta are :")
    for name in contacts:
        print(f"{name} : {contacts[name]}")

def menu():
    while True :
        print("1.Add to contact")
        print("2.Search contacts")
        print("3.Delete contact ")
        print("4.View Contacts")
        print("5.Exit")
    
        choice=int(input("Enter your Choice Here !!"))
        if choice ==1:
            Add_Contact()
        elif choice ==2:
            Search_Contacts()
        elif choice ==3:
            Delete_Contacts()
        elif choice ==4:
            View_Contacts()
        elif choice ==5:
            print("Exiting")
            break
        else:
            print("Invalid choice Try again !!!")

menu()

            



