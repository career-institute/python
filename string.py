# Strings in Python
# Strings are immutable sequences of Unicode code points

# String can be created using single quotes or double quotes
print("Hello 1")
print('Hello 2')

# String can be created using triple quotes
print('''Hello 3''')

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Index of a string
a = "Hello, World!"
print(a[0]) # H
print(a[1]) # e

# Length of a string
a = "Hello, World!"
print(len(a)) # 13

# String slicing
a = "Hello, World!"
print(a[2:5]) # llo

# Substring check
a = "Hello, World!"
print("ell" in a) # True

# String concatenation
a = "Hello"
b = "World"
c = a + ' '+ b # Hello World

# String formatting using a person into
name = 'Usama'
txt = "{} is a Software Engineer. {} has 3 years of experience in Python."
print(txt.format(name)) # Usama is a Software Engineer. Usama has 3 years of experience in Python.

# Escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt) # We are the so-called "Vikings" from the north.

# String methods
a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!
print(a.lower()) # hello, world!
print(a.strip()) # Hello, World! (removes any whitespace from the beginning or the end)
print(a.replace("H", "J")) # Jello, World!
print(a.split(",")) # ['Hello', ' World!']