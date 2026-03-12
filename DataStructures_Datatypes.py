#Datatypes :
# k=10
# float 3.14
# str	"Hello"	
# bool	True, False	
# NoneType	None

#DataStructures:
#list [1, 2,3, 3] --> Ordered, changeable, allows duplicates,mutable
#tuple  (1, 2, 3) --> Ordered, unchangeable,immutable
#set  {1, 2, 3} -->Unordered, unique items,mutable
#dict  {"name": "Alice", "age": 25} -->Key-value pairs


#stack (LIFO)->
# push: Add item (use .append())
# pop: Remove last item (use .pop())
# #queue (FIFO)
# stack1 = []

# stack1.append(10)  # push

# stack1.append(20)
# print(stack1)  # [10, 20]

# top =stack1.pop() # pop
# # print(top)   # 20
# print(stack1) # [10]

#queue
# from collections import deque

# queue = deque()
# # Enqueue
# queue.append("A")
# queue.append("B")
# queue.append("C")

# # Dequeue
# print(queue.popleft())  # A
# print(queue)            # deque(['B', 'C'])

#Task: Reverse a list of numbers using a stack by pushing the numbers onto the stack and popping them off to form the reversed list.
# Original list
# numbers = [1, 2, 3, 4, 5]

# # Stack-based reversal
# stack = []
# for num in numbers:
#     stack.append(num)

# reversed_list = []

# while stack:
#     reversed_list.append(stack.pop())
# print("Reversed list:", reversed_list)



# from collections import deque

# # Original list
# numbers = [1, 2, 3, 4, 5]

# # Queue-based reversal
# queue = deque()
# for num in numbers:
#     queue.append(num)

# reversed_list = []
# while queue:
#     reversed_list.insert(0, queue.popleft())  # Insert at the beginning
# print("Reversed list:", reversed_list)
