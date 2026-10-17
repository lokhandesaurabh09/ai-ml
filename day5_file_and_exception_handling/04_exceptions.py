filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

#-----------------------------------------------

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Calculation finished")