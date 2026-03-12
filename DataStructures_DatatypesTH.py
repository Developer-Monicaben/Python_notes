# ------------------ Basic Data Types ------------------
# name = "Alice"          # string
# age = 25                # integer
# height = 5.4            # float
# is_student = True       # boolean
# nickname = None         # NoneType

# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Is Student:", is_student)
# print("Nickname:", nickname)

# # print("\n==================== DATA STRUCTURES ====================\n")

# # ------------------ LIST ------------------
# fruits = ["apple", "banana", "cherry"]
# print("List:", fruits)

# # Changing value
# fruits[0] = "mango"
# print("After update:", fruits)

# # # Duplicates allowed
# fruits.append("apple")
# fruits.append("apple")
# print("After append:", fruits)

# # # Insert at index
# fruits.insert(1, "orange")
# print("After insert:", fruits)

# # # Removing values
# fruits.remove("banana")        # removes first matching item
# print("After remove:", fruits)

# fruits.pop()          # removes last element
# print("List now:", fruits)

# # # Slicing
# print("Slicing fruits[1:3]:", fruits[1:3])

# # # Sort and reverse
# fruits.sort()
# print("Sorted:", fruits)
# fruits.reverse()
# print("Reversed:", fruits)


# print("\n------------------ TUPLE ------------------")
# colors = ("red", "green", "blue", "red")
# print("Tuple:", colors)
# print("First item:", colors[0])
# # colors[0]="pink"

# # Tuple methods
# print("Count of 'red':", colors.count("red"))
# print("Index of 'blue':", colors.index("blue"))


# print("\n------------------ SET ------------------")

# unique_numbers = {5, 6, 2, 3, 3, 2}
# print("Set (no duplicates):", unique_numbers)

# unique_numbers.add(10)
# print("After add(10):", unique_numbers)

# # Set operations
# a = {1,2,3}
# b = {3,4,5}
# print("Union:", a.union(b))
# print("Intersection:", a.intersection(b))
# print("Difference:", a.difference(b))


# print("\n------------------ DICTIONARY ------------------")
# person = {"name": "Bob", "city": "Delhi" , "age": 30}
# print("Dictionary:", person)

# # # Access values
# print("Name:", person["name"])
# print("City :",person["city"])

# # # Update value
# person["age"] = 31
# print("Updated Age:", person["age"])

# # # Add new key-value pair
# person["email"] = "bob@example.com"
# print("Updated Dictionary:", person)

# # # Dictionary methods
# print("Keys:", person.keys())
# print("Values:", person.values())
# print("Items:", person.items())

# person.pop("city")
# print("After pop:", person)


# print("\n------------------ TYPE CHECK ------------------")
# ss = "67"
# print("Type of ss:", type(ss))


# # print("\n------------------ EXTRA SET EXAMPLE ------------------")
# nums = {100, 5, 25, 7, 1, 200, 3}
# # print("Set output:", nums)
# print("Sorted output:", sorted(nums))
