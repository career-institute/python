# Lists in Python
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:
mylist = ["apple", "banana", "cherry"]

# You access the list items by referring to the index number:
print(mylist[1]) # banana

# Change Item Value
# To change the value of a specific item, refer to the index number:
mylist = ["apple", "banana", "cherry"]

mylist[1] = "mango"
print(mylist) # ['apple', 'mango', 'cherry']

# Length of List
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3

# Add Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # ['apple', 'banana', 'cherry', 'orange']

# To add an item at the specified index, use the insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # ['apple', 'orange', 'banana', 'cherry']

# Remove Item
# There are several methods to remove items from a list:
# The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # ['apple', 'cherry']

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop() # ['apple', 'banana']