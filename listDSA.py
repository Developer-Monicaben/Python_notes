# ===============================
# PYTHON LIST - FULL PRACTICE
# ===============================

print("---- 1) Creating Lists ----")
a = []                      # empty list
b = [10, 20, 30, 40]        # integer list
c = ["apple", "banana"]     # string list
d = [10, "hello", True, 5.5]  # mixed list
e = [[1, 2], [3, 4]]        # nested list

print(a)
print(b)
print(c)
print(d)
print(e)


print("\n---- 2) Accessing Elements (Indexing) ----")
print("b[0] =", b[0])
print("b[1] =", b[1])
print("b[-1] =", b[-1])     # last element
print("b[-2] =", b[-2])


print("\n---- 3) Slicing ----")
print("b[1:3] =", b[1:3])
print("b[:2] =", b[:2])
print("b[2:] =", b[2:])
print("b[:] =", b[:])
print("b[::-1] (reverse) =", b[::-1])


print("\n---- 4) Updating Elements ----")
b[0] = 99
print("After update b =", b)


print("\n---- 5) Adding Elements ----")
b.append(50)
print("After append:", b)

b.insert(2, 777)
print("After insert:", b)

b.extend([100, 200, 300])
print("After extend:", b)


print("\n---- 6) Removing Elements ----")
b.remove(777)   # removes first matching element
print("After remove(777):", b)

removed_item = b.pop()  # removes last element
print("After pop():", b)
print("Popped item:", removed_item)

del b[0]  # deletes by index
print("After del b[0]:", b)


print("\n---- 7) Searching & Checking ----")
print("Is 20 in b?", 20 in b)
print("Is 500 in b?", 500 in b)

print(b)
print("Index of 20:", b.index(20))
print("Count of 20:", b.count(20))


print("\n---- 8) Sorting & Reversing ----")
x = [5, 2, 9, 1, 7, 3]
print("Original x:", x)

x.sort()
print("After sort():", x)

x.sort(reverse=True)
print("After sort(reverse=True):", x)

x.reverse()
print("After reverse():", x)

print("sorted(x):", sorted(x))  # returns new list


print("\n---- 9) Copying List ----")
list1 = [1, 2, 3]
list2 = list1          # reference copy (same memory)
list3 = list1.copy()   # actual copy

list1.append(100)

print("list1:", list1)
print("list2 (reference):", list2)
print("list3 (copy):", list3)


print("\n---- 10) Traversing List ----")
nums = [10, 20, 30, 40, 50]

print("Using for loop:")
for i in nums:
    print(i)

print("Using for loop with index:")
for i in range(len(nums)):
    print("Index:", i, "Value:", nums[i])

print("Using while loop:")
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

print("Using enumerate:")
for index, value in enumerate(nums):
    print(index, value)


print("\n---- 11) List Comprehension ----")
squares = [i*i for i in range(1, 6)]
print("Squares:", squares)

even_nums = [i for i in range(1, 21) if i % 2 == 0]
print("Even numbers:", even_nums)


print("\n---- 12) Common DSA List Problems ----")

# Reverse list without built-in reverse()
arr = [1, 2, 3, 4, 5]
rev = []
for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])
print("Reverse without built-in:", rev)

# Remove duplicates
arr2 = [1, 2, 2, 3, 3, 4, 5, 5]
unique = []
for i in arr2:
    if i not in unique:
        unique.append(i)
print("Remove duplicates:", unique)

# Find max and min
arr3 = [10, 5, 30, 2, 99]
print("Max:", max(arr3))
print("Min:", min(arr3))

# Second largest
arr4 = [10, 40, 20, 50, 30]
arr4.sort()
print("Second largest:", arr4[-2])


print("\n---- 13) 2D List (Matrix) ----")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("Traversing matrix:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()




# ==========================================================
# PYTHON LIST - ADVANCED
# Covers: packing/unpacking, zip, key sorting, stack/queue,
# shallow/deep copy, memory, map/filter/reduce, DSA patterns
# ==========================================================

import copy
from collections import deque
from functools import reduce

print("\n================= 1) Packing & Unpacking =================")
data = [10, 20, 30]
a, b, c = data
print("a =", a, "b =", b, "c =", c)

nums = [1, 2, 3, 4, 5]
x, y, *rest = nums
print("x =", x, "y =", y, "rest =", rest)

# Swapping using list unpacking
p, q = 100, 200
p, q = q, p
print("After swap: p =", p, "q =", q)


print("\n================= 2) zip() with Lists ====================")
names = ["Asha", "Ravi", "Monica"]
marks = [80, 90, 95]

combined = list(zip(names, marks))
print("Zipped list:", combined)

for n, m in combined:
    print(n, "scored", m)


print("\n================= 3) List Memory & Reference =============")
list1 = [10, 20, 30]
list2 = list1  # reference copy

print("list1:", list1)
print("list2:", list2)
print("id(list1):", id(list1))
print("id(list2):", id(list2))

list1.append(999)
print("After list1.append(999)")
print("list1:", list1)
print("list2:", list2, "  <-- also changed because same reference")


print("\n================= 4) Shallow Copy vs Deep Copy ===========")
nested1 = [[1, 2], [3, 4]]

shallow = nested1.copy()           # shallow copy
deep = copy.deepcopy(nested1)      # deep copy

print("nested1:", nested1)
print("shallow:", shallow)
print("deep   :", deep)

nested1[0][0] = 999
print("\nAfter changing nested1[0][0] = 999")
print("nested1:", nested1)
print("shallow:", shallow, " <-- changed (because shallow copy)")
print("deep   :", deep, " <-- not changed")


print("\n================= 5) Sorting Advanced ====================")

# sort() vs sorted()
arr = [5, 1, 9, 2]
print("Original:", arr)

sorted_arr = sorted(arr)
print("sorted(arr):", sorted_arr)
print("arr still:", arr)

arr.sort()
print("arr after sort():", arr)

# Sorting with key
words = ["banana", "apple", "watermelon", "kiwi"]
words.sort(key=len)
print("\nSort words by length:", words)

# Sorting list of tuples
students = [("Ravi", 80), ("Monica", 95), ("Asha", 90)]
students.sort(key=lambda x: x[1])   # sort by marks
print("Students sorted by marks:", students)

# Sorting list of dictionaries
employees = [
    {"name": "John", "salary": 40000},
    {"name": "Monica", "salary": 70000},
    {"name": "Asha", "salary": 50000}
]

employees.sort(key=lambda x: x["salary"], reverse=True)
print("Employees sorted by salary:", employees)


print("\n================= 6) List as Stack =======================")
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

print("Pop:", stack.pop())
print("Stack after pop:", stack)


print("\n================= 7) List as Queue =======================")
# Using list (not recommended for large data)
queue = [10, 20, 30]
queue.append(40)
print("Queue:", queue)

removed = queue.pop(0)  # slow for large data
print("Removed:", removed)
print("Queue now:", queue)

# Best way: deque
dq = deque([10, 20, 30])
dq.append(40)
print("\nDeque Queue:", dq)

removed2 = dq.popleft()
print("Removed using popleft():", removed2)
print("Deque now:", dq)


print("\n================= 8) Built-in Functions ==================")
nums = [0, 5, 10, 15]

print("len:", len(nums))
print("sum:", sum(nums))
print("min:", min(nums))
print("max:", max(nums))
print("any:", any(nums))  # True if any element is True/non-zero
print("all:", all(nums))  # True if all elements are True/non-zero


print("\n================= 9) List in Functions ===================")
def update_list(lst):
    lst.append(1000)  # modifies original list
    return lst

mylist = [1, 2, 3]
print("Before function:", mylist)
update_list(mylist)
print("After function:", mylist)


print("\n================= 10) map(), filter(), reduce() ==========")
nums = [1, 2, 3, 4, 5]

# map -> apply function to each element
squares = list(map(lambda x: x * x, nums))
print("Squares using map:", squares)

# filter -> keep only matching elements
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens using filter:", evens)

# reduce -> reduce list to single value
product = reduce(lambda a, b: a * b, nums)
print("Product using reduce:", product)


print("\n================= 11) DSA Pattern: Two Sum ===============")
arr = [2, 7, 11, 15]
target = 9

found = False
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Two sum pair found:", arr[i], arr[j])
            found = True
            break
    if found:
        break


print("\n================= 12) DSA Pattern: Two Pointers ===========")
# Check if list is palindrome
arr = [1, 2, 3, 2, 1]
i = 0
j = len(arr) - 1
palindrome = True

while i < j:
    if arr[i] != arr[j]:
        palindrome = False
        break
    i += 1
    j -= 1

print("Is palindrome?", palindrome)


print("\n================= 13) DSA Pattern: Sliding Window =========")
# Maximum sum of k consecutive elements
arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]
    max_sum = max(max_sum, window_sum)

print("Max sum of", k, "consecutive elements =", max_sum)


print("\n================= 14) DSA: Rotate List ====================")
arr = [1, 2, 3, 4, 5]
k = 2

k = k % len(arr)
rotated = arr[-k:] + arr[:-k]
print("Rotated by", k, ":", rotated)


print("\n================= 15) DSA: Move Zeros to End =============")
arr = [0, 1, 0, 3, 12]
result = []
zero_count = 0

for x in arr:
    if x != 0:
        result.append(x)
    else:
        zero_count += 1

result.extend([0] * zero_count)
print("After moving zeros:", result)


print("\n================= 16) DSA: Frequency Count ===============")
arr = [1, 2, 2, 3, 3, 3, 4]
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print("Frequency:", freq)


print("\n================= 17) List vs Tuple (Quick Demo) ==========")
lst = [1, 2, 3]
tpl = (1, 2, 3)

lst[0] = 999
print("List after update:", lst)

print("Tuple:", tpl)
print("Tuple cannot be modified (immutable)")


print("\n ALL ADVANCED LIST TOPICS COMPLETED!")





# =====================================================
# PYTHON TUPLE - FULL
# Covers: creation, indexing, slicing, methods,
# packing/unpacking, nested tuple, loops, zip,
# tuple vs list, tuple in functions
# =====================================================

print("\n================= 1) Creating Tuples =================")

t1 = ()                     # empty tuple
t2 = (10, 20, 30)           # normal tuple
t3 = ("apple", "banana")    # string tuple
t4 = (10, "hello", True, 5.5)  # mixed tuple

print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("t4:", t4)

# Single value tuple (IMPORTANT)
t5 = (10)      # NOT a tuple (int)
t6 = (10,)     # tuple
print("\nt5:", t5, "type:", type(t5))
print("t6:", t6, "type:", type(t6))


print("\n================= 2) Accessing Elements ==============")

print("t2[0] =", t2[0])
print("t2[1] =", t2[1])
print("t2[-1] =", t2[-1])  # last element


print("\n================= 3) Slicing =========================")

print("t2[0:2] =", t2[0:2])
print("t2[:2] =", t2[:2])
print("t2[1:] =", t2[1:])
print("t2[:] =", t2[:])
print("t2[::-1] =", t2[::-1])  # reverse


print("\n================= 4) Tuple is Immutable ==============")

# t2[0] = 999   This will give error
print("Tuple cannot be updated like list (immutable)")


print("\n================= 5) Tuple Methods ===================")

t7 = (10, 20, 10, 30, 10, 40)
print("t7:", t7)

print("count(10):", t7.count(10))
print("index(30):", t7.index(30))


print("\n================= 6) Packing & Unpacking =============")

# Packing
pack = 10, 20, 30
print("Packed tuple:", pack)

# Unpacking
a, b, c = pack
print("Unpacked:", a, b, c)

# Unpacking with *
nums = (1, 2, 3, 4, 5)
x, y, *rest = nums
print("x:", x)
print("y:", y)
print("rest:", rest)


print("\n================= 7) Looping in Tuple ================")

t8 = (100, 200, 300, 400)

print("Using for loop:")
for i in t8:
    print(i)

print("Using for loop with index:")
for i in range(len(t8)):
    print("Index:", i, "Value:", t8[i])

print("Using enumerate:")
for index, value in enumerate(t8):
    print(index, value)


print("\n================= 8) Nested Tuple =====================")

nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)

print("Access nested[0]:", nested[0])
print("Access nested[0][1]:", nested[0][1])


print("\n================= 9) Tuple in Functions ===============")

def get_student():
    name = "anu"
    age = 78
    mark = 95
    return name, age, mark   # returns as tuple

student = get_student()
print("Returned tuple:", student)

n, a, m = student
print("Unpacked values:", n, a, m)


print("\n================= 10) zip() with Tuples ===============")

names = ("Asha", "Ravi", "Monica")
marks = (80, 90, 95)

z = tuple(zip(names, marks))
print("Zipped tuple:", z)

for name, mark in z:
    print(name, "->", mark)


print("\n================= 11) Tuple vs List ===================")

lst = [10, 20, 30]
tpl = (10, 20, 30)

lst[0] = 999
print("List after update:", lst)

print("Tuple:", tpl)
print("Tuple cannot be updated (immutable)")

print("\nTuple is faster than list for fixed data (interview point)")


print("\n================= 12) Convert Tuple <-> List ===========")

tpl2 = (1, 2, 3, 4)
lst2 = list(tpl2)
print("Tuple to List:", lst2)

lst2.append(999)
tpl3 = tuple(lst2)
print("List to Tuple:", tpl3)


print("\n================= 13) Tuple DSA Use Case ===============")

# tuple used for fixed data like coordinates
point = (10, 20)
print("Point:", point)

# tuple used in dictionary keys
locations = {
    (0, 0): "Start",
    (1, 2): "Shop",
    (5, 3): "Home"
}
print("Dictionary with tuple keys:", locations)


print("\n ALL TUPLE TOPICS COMPLETED!")




# =====================================================
# PYTHON SET - FULL
# Covers: creation, add, update, remove, discard,
# pop, clear, union, intersection, difference,
# symmetric difference, subset/superset, frozenset,
# set comprehension, DSA use cases
# =====================================================

print("\n================= 1) Creating Sets ====================")

s1 = set()   # empty set (IMPORTANT)
s2 = {10, 20, 30, 40}
s3 = {"apple", "banana", "orange"}
s4 = {10, "hello", True, 5.5}  # mixed

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)

# NOTE: {} is not a set, it's a dictionary
d = {}
print("\n{} type:", type(d))

# Duplicate values automatically removed
s5 = {1, 2, 2, 3, 3, 4}
print("Duplicates removed:", s5)


print("\n================= 2) Set Properties ===================")
print("Set is unordered -> no indexing")
print("Set does not allow duplicates")
print("Set is mutable (you can add/remove elements)")


print("\n================= 3) Adding Elements ===================")

s = {10, 20, 30}
print("Original:", s)

s.add(40)
print("After add(40):", s)

s.update([50, 60, 70])
print("After update([50,60,70]):", s)

s.update("AB")  # adds characters
print("After update('AB'):", s)


print("\n================= 4) Removing Elements =================")

s.remove(10)  # error if not found
print("After remove(10):", s)

s.discard(999)  # no error if not found
print("After discard(999):", s)

removed = s.pop()  # removes random element
print("After pop():", s)
print("Popped element:", removed)


print("\n================= 5) Searching in Set ==================")

print("Is 20 in set?", 20 in s)
print("Is 500 in set?", 500 in s)


print("\n================= 6) Set Operations (DSA Important) =====")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("A:", A)
print("B:", B)

print("\nUnion (A | B):", A | B)
print("Intersection (A & B):", A & B)
print("Difference (A - B):", A - B)
print("Difference (B - A):", B - A)
print("Symmetric Difference (A ^ B):", A ^ B)

# Using methods
print("\nA.union(B):", A.union(B))
print("A.intersection(B):", A.intersection(B))
print("A.difference(B):", A.difference(B))
print("A.symmetric_difference(B):", A.symmetric_difference(B))


print("\n================= 7) Subset / Superset =================")

X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}

print("X:", X)
print("Y:", Y)

print("X is subset of Y:", X.issubset(Y))
print("Y is superset of X:", Y.issuperset(X))

print("X <= Y:", X <= Y)
print("Y >= X:", Y >= X)


print("\n================= 8) Disjoint Sets ======================")

P = {1, 2, 3}
Q = {10, 20, 30}

print("P and Q are disjoint:", P.isdisjoint(Q))


print("\n================= 9) Copying Set =======================")

sA = {1, 2, 3}
sB = sA.copy()

sA.add(999)

print("sA:", sA)
print("sB:", sB)


print("\n================= 10) Set Comprehension =================")

nums = [1, 2, 2, 3, 3, 4, 5, 5, 6]
unique_squares = {x * x for x in nums}
print("Unique squares:", unique_squares)

even_set = {x for x in range(1, 21) if x % 2 == 0}
print("Even numbers set:", even_set)


print("\n================= 11) frozenset (Immutable Set) =========")

fs = frozenset([1, 2, 3, 4])
print("frozenset:", fs)

# fs.add(5)  error (immutable)
print("frozenset cannot be modified (immutable)")


print("\n================= 12) Convert List <-> Set ==============")

lst = [10, 20, 20, 30, 30, 40]
st = set(lst)
print("List:", lst)
print("List to Set:", st)

lst_back = list(st)
print("Set to List:", lst_back)


print("\n================= 13) DSA Use Cases =====================")

# Remove duplicates
arr = [1, 2, 2, 3, 3, 4]
print("Original:", arr)
print("After removing duplicates:", list(set(arr)))

# Common elements
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = set(a) & set(b)
print("Common elements:", common)

# Missing elements
a = [1, 2, 3, 4, 5]
b = [2, 3, 1, 5]
missing = set(a) - set(b)
print("Missing element(s):", missing)


print("\n ALL SET TOPICS COMPLETED!")
