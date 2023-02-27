# Data Types in Python

# Text Type:	str
x = "Hello World"
print(x)
print(type(x))

# Numeric Types:	int, float, complex
x = 20
print(x)
print(type(x))

x = 20.5
print(x)
print(type(x))

x = 1j
print(x)
print(type(x))

# Sequence Types:	list, tuple, range
x = ["apple", "banana", "cherry"] # List is a collection which is ordered and changeable.
print(x)
print(type(x))

x = ("apple", "banana", "cherry") # Tuple is a collection which is ordered and unchangeable.
print(x)
print(type(x))

x = range(6) # Range is a collection which is ordered and unchangeable.
print(x)
print(type(x))

# Mapping Type:	dict
x = {"name" : "John", "age" : 36} # Dictionary is a collection which is unordered, changeable and indexed.
print(x)
print(type(x))

# Set Types:	set, frozenset
x = {"apple", "banana", "cherry"} # Set is a collection which is unordered and unindexed.
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"}) # Frozen set is a collection which is unordered and unindexed.
print(x)
print(type(x))

# Boolean Type:	bool
x = True
print(x)
print(type(x))

# Binary Types:	bytes, bytearray, memoryview
x = b"Hello" # Bytes is a collection which is ordered and unchangeable.
print(x)
print(type(x))

x = bytearray(5) # Bytearray is a collection which is ordered and changeable.
print(x)
print(type(x))

x = memoryview(bytes(5)) # Memoryview is a collection which is ordered and changeable.
print(x)
print(type(x))

# None Type:	NoneType
x = None
print(x)
print(type(x))