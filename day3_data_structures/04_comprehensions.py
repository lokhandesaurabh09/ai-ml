# List comprehension
print([x * 2 for x in range(5)])

# With a condition
print([x for x in range(10) if x % 2 == 0])

# Same thing as a normal loop, for comparison
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x)
print(result)

# Dict comprehension
print({x: x ** 2 for x in range(5)})

# Set comprehension
print({x % 3 for x in range(10)})

words = ["python", "is", "fun", "and", "powerful"]
print([w.upper() for w in words if len(w) > 3])