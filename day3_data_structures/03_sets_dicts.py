# Sets
a = {1, 2, 3, 3, 4}
b = {3, 4 , 5}
a.add(6)
a.remove(1)
print("Set a:", a)
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

#Dictionaries
student = {"name": "Saurabh", "age": 21}
student["city"] = "Nashik"
student["age"] = 22
print(student)

print(student.get("marks", "Not found"))
print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, "->", value)