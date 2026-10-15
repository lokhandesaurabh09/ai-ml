# Basic function
def greet(name):
    return "Hello, " + name

# Default argument
def greet_default(name="Guest"):
    return "Hello, " + name

# Returning two values
def add_and_multiply(a, b):
    return a + b, a * b

# Function with a condition
def is_adult(age):
    return age >= 18

print(greet("Saurabh"))
print(greet_default())          # uses default "Guest"
print(greet_default("Rahul"))

s,p = add_and_multiply(4,5)
print("Sum:", s, "Product:", p)

print(add_and_multiply(a = 2, b = 3))
print(is_adult(21), is_adult(15))